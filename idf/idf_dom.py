# -*- coding: utf-8 -*-
import getopt,os,sys
from os import makedirs
from os.path import join,isfile,isdir
import xml.etree.ElementTree as ET

import GEOparse as geop
from idf_contact_dom import ContactDOM
from idf_experiment_dom import ExperimentDOM
from xml_models import IdfXmlModels

idf_page_section_models=IdfXmlModels()

"""
A data model for generating both the IDF file xml draft and
the the final IDF file.

See: https://www.ebi.ac.uk/arrayexpress/help/creating_an_idf.html

IdfFileDOM:
   
Raises:
     Nothing
"""

def getXmlDocRoot(xml_file):
        doc_root=None
        if not isfile(xml_file):
            return doc_root
        try:
            xml_doc=ET.parse(xml_file)
            doc_root=xml_doc.getroot()
        except:raise
        return doc_root

class IdfFileDOM:
    def __init__(self,geo_accession,base_dir):
        self.idf_file=join(base_dir,geo_accession+".idf.txt")
        self.sdrf_file=join(base_dir,geo_accession+".sdrf.txt")
        self.cfg_file=join(base_dir,geo_accession+".cfg")
        self.idf_xml_file=join(base_dir,geo_accession+".idf.xml")
        self.geo_accession=geo_accession
        self.idf_xml_root=None
        self.idf_page_sections={}
        self.__set()

    def __set(self):
        self.idf_xml_root=getXmlDocRoot(self.idf_xml_file) 
        for section in idf_page_section_models.getIdfPage().findall("./section"):
            section_id=section.attrib["id"]
            section_rank=section.attrib["rank"]
            self.idf_page_sections[int(section_rank)]=section_id
    
    def gen_idf(self):
        header="\n"
        header+="*********************************************"
        header+="\n"
        print("%sGENERATING THE IDF FILE FOR:%s\n"%(header,self.geo_accession))
        print("File to generate: %s"%(self.idf_file))
        print("Using Input idf xml draft: %s" %(self.idf_xml_file))
        print("Using Input Config file: %s" %(self.cfg_file))
        try:
            fd=open(self.idf_file,'w')
            ## Controlled vocab target from the input config file
            target_terms=self.getCfgMap()
            for section_rank,section_id in self.idf_page_sections.items():
                section_container=self.getSectionData(section_id)
                ## filter controlled vocab targets if needed
                if section_id in target_terms:
                    section_container=self.getSectionContainer(section_container,target_terms[section_id])
                for field_name,content in section_container.items():
                    if isinstance(content,list):content=",".join(content)
                    if content is None:content=""
                    fd.write("%s\t%s\n" %(field_name,content))
            print("%s"%(header))
            print("IDF file  for %s has been generated - Check : %s"%(self.geo_accession,self.idf_file))
        except:raise
    ##
    # Controlled vocab filter from user's specified list
    #
    def getCfgMap(self):
        cfg_map={}
        if isfile(self.cfg_file):
            lines=[line.rstrip('\n') for line in open(self.cfg_file)]
            for line in lines:
                try:
                    [field_name,id_list]=line.split("\t")
                    cfg_map[field_name]=id_list.split(",")
                except:pass
        return cfg_map
    
    def getSectionData(self,section_id):
        exp_map={}
        if self.idf_xml_root is not None:
            try:
                tag_list=self.idf_xml_root.findall("./section[@id='"+section_id+"']/tag")
                term_list=self.idf_xml_root.findall("./section[@id='"+section_id+"']/term")
                if len(tag_list)>0:
                    for exp_field in tag_list: 
                        label=exp_field.attrib["label"]
                        exp_map[label]=exp_field.text
                else:
                    if term_list is not None:
                        for term in term_list:
                            term_id=term.attrib["id"]
                            exp_map[term_id]={}
                            for tag in term.findall("./tag"):
                                label=tag.attrib["label"]
                                exp_map[term_id][label]=tag.text
            except:pass
        return exp_map
    ##
    # Given a controlled vocab container and a list of term targets,
    # this function return idf-ready map of all the controlled vocab terms
    # that apply to this specific controlled vocab section
    ##
    def getSectionContainer(self,section_map,target_term_ids_list):
        vocab_terms={}
        try:
            for term_id in target_term_ids_list:
                if term_id in section_map:
                    for label,value in section_map[term_id].items():
                        if label not in vocab_terms:vocab_terms[label]=[]
                        vocab_terms[label].append(value)
        except:raise
        return vocab_terms

class IdfFileXmlDOM:
    def __init__(self,geo_accession,base_dir):
        self.gse=None
        self.geo_accession=geo_accession
        self.sdrf_file=""
        self.idf_xml_file=""
        ### These,each,have their data model
        self.contact=None
        self.experiment=None
        self.__set(base_dir)

    def __set(self,base_dir):
        if not isdir(base_dir): makedirs(base_dir)
        try:
           self.gse=geop.get_GEO(geo=self.geo_accession,destdir=base_dir, silent=True)
        except:pass
        geo_metadata=self.gse
        ##detect case experiment not in GEO database
        if geo_metadata is not None:geo_metadata=self.gse.metadata
        self.idf_xml_file=join(base_dir,self.geo_accession+".idf.xml")
        self.sdrf_file=self.geo_accession+".sdrf.txt"
        self.contact=ContactDOM(geo_metadata)
        self.experiment=ExperimentDOM(geo_metadata)

    def gen_xml(self):
        fdx=open(self.idf_xml_file,'w')
        fdx.write("<?xml version='1.0' encoding='utf-8' ?>\n")
        fdx.write("<experiment_idf>\n")
        fdx.write(self.contact.getXmlBlock())
        fdx.write(self.experiment.getXmlBlock())
        fdx.write("  <section id='experiment_sdrf'>\n")
        fdx.write("    <tag label='SDRF File'><![CDATA["+self.sdrf_file+"]]></tag>\n")
        fdx.write("  </section>\n")
        fdx.write("</experiment_idf>\n")
        header="\n"
        header+="*********************************************"
        header+="\n"
        print("%sGENERATING THE IDF DRAFT\n"%(header))
        print("IDF DRAFT: %s  - Ready"%(self.idf_xml_file))
        print("This file will be used by gen_idf.py program to create the final idf file %s"%("\n"))
        print("%s"%(header))

    def show_contact(self):
        self.contact.display(self.fd)

    def show_experiment(self):
        self.experiment.display(self.fd)


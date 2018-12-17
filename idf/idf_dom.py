# -*- coding: utf-8 -*-
import getopt,os,sys
from os import makedirs
from os.path import join,isfile,isdir
import xml.etree.ElementTree as ET

import GEOparse as geop
from idf_contact_dom import ContactDOM
from idf_experiment_dom import ExperimentDOM

"""
A data model for generating both the IDF file xml draft and
the the final IDF file.

See: https://www.ebi.ac.uk/arrayexpress/help/creating_an_idf.html

IdfFileDOM:
   
Raises:
     Nothing
"""

class IdfFileDOM:
    def __init__(self,geo_accession,base_dir):
        self.idf_file=join(base_dir,geo_accession+".idf.txt")
        self.cfg_file=join(base_dir,geo_accession+".cfg")
        self.idf_xml_file=oin(base_dir,geo_accession+".idf.xml")

class IdfFileXmlDOM:
    def __init__(self,geo_accession,base_dir):
        self.gse=None
        self.geo_accession=geo_accession
        self.idf_file=""
        self.sdrf_file=""
        self.idf_xml_file=""
        self.fd=None
        self.fdx=None
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
        self.idf_file=join(base_dir,self.geo_accession+".idf.txt")
        self.idf_xml_file=join(base_dir,self.geo_accession+".idf.xml")
        self.sdrf_file=self.geo_accession+".sdrf.txt"

        self.fdx=open(self.idf_xml_file,'w') 
        self.fd=open(self.idf_file,'w') 
        self.contact=ContactDOM(geo_metadata)
        self.experiment=ExperimentDOM(geo_metadata)

    def gen_xml(self):
        self.fdx.write("<?xml version='1.0' encoding='utf-8' ?>\n")
        self.fdx.write("<experiment_idf>\n")
        self.fdx.write(self.contact.getXmlBlock())
        self.fdx.write(self.experiment.getXmlBlock())
        self.fdx.write("  <experiment_sdrf>\n")
        self.fdx.write("    <tag label='SDRF File'><![CDATA["+self.sdrf_file+"]]></tag>\n")
        self.fdx.write("  </experiment_sdrf>\n")
        self.fdx.write("</experiment_idf>\n")
        print("%s  - Ready for review"%(self.idf_xml_file))
        print("This file is used to create the final idf file - %s "%(self.idf_file))

    def show_contact(self):
        self.contact.display(self.fd)

    def show_experiment(self):
        self.experiment.display(self.fd)


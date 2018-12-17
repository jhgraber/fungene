# -*- coding: utf-8 -*-
import getopt,os,sys
from os import makedirs
from os.path import join,isfile,isdir
import GEOparse as geop
from geoContact_dom import ContactDOM
from geoExperimentPlatform_dom import ExperimentPlatformDOM
from geoExperimentSample_dom import ExperimentSampleDOM
 
"""
A data model for GEO EXPERIMENT dataset.
See: https://geoparse.readthedocs.io/en/latest/GEOparse.html
GeoExperimentDOM:
   
Raises:
     Nothing
"""   

class GeoExperimentDOM(ContactDOM,ExperimentPlatformDOM):
    def __init__(self,geo_accession,base_dir):
        self.gse=None

        self.title=""
        self.experiment_type=""
        self.geo_accession=""
        self.overall_design=""
        self.pubmed_id=""
        self.platform_taxid=""
        self.sample_taxid=""
        self.status=""
        self.supplementary_file=""
        self.summary=""
        self.submission_date=""
        self.last_update_date=""
        self.relation=""
        ### These,each,have their data model
        self.samples={}
        self.platforms=[]
        self.contact=None
      
        self.__set(geo_accession,base_dir)

    def __set(self,geo_accession,base_dir):
        if not isdir(base_dir): makedirs(base_dir)
        self.gse=geop.get_GEO(geo=geo_accession,destdir=base_dir, silent=True)
        self.contact=ContactDOM(self.gse.metadata)
        self.load_platforms()
        self.set_experiment()
        self.load_samples()

    def set_experiment(self):
        try:
            if "title" in self.gse.metadata:
                self.title=";".join(self.gse.metadata["title"])
            if "type" in self.gse.metadata:
                self.experiment_type=";".join(self.gse.metadata["type"])
            if "geo_accession" in self.gse.metadata:
                self.geo_accession=";".join(self.gse.metadata["geo_accession"])
            if "overall_design" in self.gse.metadata:
                self.overall_design=";".join(self.gse.metadata["overall_design"])
            if "pubmed_id" in self.gse.metadata:
                self.pubmed_id=";".join(self.gse.metadata["pubmed_id"])
            if "platform_taxid" in self.gse.metadata:
                self.platform_taxid=";".join(self.gse.metadata["platform_taxid"])
            if "sample_taxid" in self.gse.metadata:
                self.sample_taxid=";".join(self.gse.metadata["sample_taxid"])
            if "status" in self.gse.metadata:
                self.status=";".join(self.gse.metadata["status"])
            if "supplementary_file" in self.gse.metadata:
                self.supplementary_file=";".join(self.gse.metadata["supplementary_file"])
            if "summary" in self.gse.metadata:
                self.summary=";".join(self.gse.metadata["summary"])
            if "submission_date" in self.gse.metadata:
                self.submission_date=";".join(self.gse.metadata["submission_date"])
            if "last_update_date" in self.gse.metadata:
                self.last_update_date=";".join(self.gse.metadata["last_update_date"])
            if "relation" in self.gse.metadata:
                self.relation=";".join(self.gse.metadata["relation"])
        except:pass

    def load_platforms(self):
         for gpls_name, gpls in self.gse.gpls.items():
             self.platforms.append(ExperimentPlatformDOM(gpls.metadata))

    def load_samples(self):
         for gsms_name, gsms in self.gse.gsms.items():
             self.samples[gsms_name]=ExperimentSampleDOM(gsms.metadata)

    def show_serie(self):
        print("")
        print("----------------")
        print("Exeperiment GEO accession:%s" % (self.geo_accession))
        print("----------------")
        for key,value in self.gse.metadata.items():
            print("- %s : %s" % (key,";".join(value)))
          
    def show_contact(self):
        print("")
        print("----------------")
        print("Exeperiment GEO accession:%s" % (self.geo_accession))
        print("----------------")
        print("Contact:")
        self.contact.display()

    def show_platforms(self):
        print("")
        print("----------------")
        print("Exeperiment GEO accession:%s" % (self.geo_accession))
        print("----------------")
        print("Platforms:")
        for platform in self.platforms:
            platform.display()

    def show_experiment(self):
        print("")
        print("----------------")
        print("Exeperiment GEO accession:%s" % (self.geo_accession))
        print("----------------")
        print("Pubmed ID: %s" % (self.pubmed_id))
        print("Title: %s" % (self.title))
        print("Submission Date: %s" % (self.submission_date))
        print("Last Update Date: %s" % (self.last_update_date))
        print("Experiment Status: %s" % (self.status))
        print("Experiment Type: %s" % (self.experiment_type))
        print("Exepriment Design: %s" % (self.overall_design))
        print("Platform Taxonomy ID: %s" % (self.platform_taxid))
        print("Sample Taxonomy ID: %s" % (self.sample_taxid))
        print("Supplementary File: %s" % (self.supplementary_file))
        print("Relation: %s" % (self.relation))
        print("")
        print("Experiment Summary: %s" % (self.summary))

    def show_samples(self,sample_id=None):
        if sample_id is None or sample_id not in self.samples:
            for sample_id,sample_obj in self.samples.items():
                sample_obj.show_protocol()
        else:self.samples[sample_id].show_sample()


# -*- coding: utf-8 -*-
import getopt,os,sys
from os.path import join
from geoContact_dom import ContactDOM
 
"""
A data model for GEO Sample dataset.
See: https://geoparse.readthedocs.io/en/latest/GEOparse.html

GeoExperimentDOM:
   
Raises:
     Nothing
"""

class ExperimentSampleDOM(ContactDOM):
    def __init__(self,gsms_obj_metadata):
        self.sample={}
        ### These,each,have their data model
        self.contact=None
        self.__set(gsms_obj_metadata)

    def __set(self,gsms_obj_metadata):
        self.contact=ContactDOM(gsms_obj_metadata)
        self.set_sample(gsms_obj_metadata)

    def set_sample(self,gsms_obj_metadata):
        try:
            for key, value in gsms_obj_metadata.items():
                self.sample[key]= "; ".join(value)   
        except:pass

    def show_contact(self):
        print("")
        print("----------------")
        print("Sample Accession:%s" % (self.sample["geo_accession"]))
        print("----------------")
        print("Contact:")
        self.contact.display()

    def show_sample(self):
        print("")
        print("----------------")
        print("Sample Accession:%s" % (self.sample["geo_accession"]))
        print("----------------")
        for key,value in self.sample.items():
            print("- %s: %s" % (key,value))

    def show_protocol(self):
        print("")
        print("----------------")
        print("Sample Accession:%s" % (self.sample["geo_accession"]))
        print("----------------")
        for key,value in self.sample.items():
            if "protocol" in key or "library" in key or "status" in key or "date" in key or "_ch" in key or "title" in key:
                print("- %s: %s" % (key,value))
            

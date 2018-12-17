# -*- coding: utf-8 -*-
from os.path import join

"""
A data model for GEO Platform dataset.
See: https://geoparse.readthedocs.io/en/latest/GEOparse.html

ExperimentPlatformDOM:
   
Raises:
     Nothing
"""
class ExperimentPlatformDOM:
    def __init__(self,gpls_obj_metadata):
        self.status=""
        self.submission_date=""
        self.title=""
        self.technology=""
        self.taxid=""
        self.geo_accession=""
        self.contact_country=""
        self.last_update_date=""
        self.distribution=""
        self.organism=""
        self.contact_name=""
        self.__set(gpls_obj_metadata)

    def __set(self,gpls_obj_metadata):
        try:
            if "status" in gpls_obj_metadata:
                self.status=";".join(gpls_obj_metadata["status"])
            if "submission_date" in gpls_obj_metadata:
                self.submission_date=";".join(gpls_obj_metadata["submission_date"])
            if "title" in gpls_obj_metadata:
                self.title=";".join(gpls_obj_metadata["title"])
            if "technology" in gpls_obj_metadata:
                self.technology=";".join(gpls_obj_metadata["technology"])
            if "taxid" in gpls_obj_metadata:
                self.taxid=";".join(gpls_obj_metadata["taxid"])
            if "geo_accession" in gpls_obj_metadata:
                self.geo_accession=";".join(gpls_obj_metadata["geo_accession"])
            if "contact_country" in gpls_obj_metadata:
                self.contact_country=";".join(gpls_obj_metadata["contact_country"])
            if "last_update_date" in gpls_obj_metadata:
                self.last_update_date=";".join(gpls_obj_metadata["last_update_date"])
            if "distribution" in gpls_obj_metadata:
                self.distribution=";".join(gpls_obj_metadata["distribution"])
            if "organism" in gpls_obj_metadata:
                self.organism=";".join(gpls_obj_metadata["organism"])
            if "contact_name" in gpls_obj_metadata:
                self.contact_name=";".join(gpls_obj_metadata["contact_name"])
        except:pass

    def display(self):
        print("=================" )
        print("Platform Geo Accession ID:%s" % (self.geo_accession))
        print("Platform Title:%s" % (self.title))
        print("Thecnology:%s" % (self.technology))
        print("Contact Name:%s" % (self.contact_name))
        print("Taxonomy ID:%s" % (self.taxid))
        print("Organism:%s" % (self.organism))
        print("Country:%s" % (self.contact_country))
        print("Submission Date:%s" % (self.submission_date))
        print("Last Update Date:%s" % (self.last_update_date))
        print("Status:%s" % (self.status))
        print("=================" )


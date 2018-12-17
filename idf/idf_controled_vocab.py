# -*- coding: utf-8 -*-
from os.path import join

"""
A data model for controled vocab.
See: https://www.ebi.ac.uk/ols/ontologies

   
Raises:
     Nothing
"""
from xml_models import IdfXmlModels
idf_models=IdfXmlModels()

class ContactDOM:
    def __init__(self,geo_obj_metadata):
        self.geo_metadata=geo_obj_metadata
        self.idf_contact_model=idf_models.getExperimentContact()
        self.idf_contact_role_model=idf_models.getExperimentContactRole()
        self.contact={}
        self.contact_name=None
        self.__set()

    def set_contact_name(self):
        try:
            person=";".join(self.geo_metadata["contact_name"])
            persons=person.split(";")
            person_name=persons[0]
            fields= person_name.split(",")
            if len(fields)>2:
                self.contact["first_name"]=fields[0]
                self.contact["mid_name"]=fields[1]
                self.contact["last_name"]=fields[2]
            else:
                self.contact["first_name"]=fields[0]
                self.contact["last_name"]=fields[1]
        except:pass

    def set_address(self):
        try:
           self.contact["address"]=";".join(self.geo_metadata["contact_address"])
           self.contact["address"]+=", "+";".join(self.geo_metadata["contact_city"])
           self.contact["address"]+=", "+";".join(self.geo_metadata["contact_state"])
           self.contact["address"]+=" "+";".join(self.geo_metadata["contact_zip/postal_code"])
           self.contact["address"]+=", "+";".join(self.geo_metadata["contact_country"])
        except:pass

    def __set(self):
        try:
            contact_fields= self.idf_contact_model.findall("./node")
            for node in contact_fields:
                field_id=node.attrib["id"] 
                self.contact[field_id]=""

            for node in contact_fields:
                geo_key=node.attrib["geo_key"]  
                if geo_key =="contact_name":
                    if self.contact_name is not None:continue
                    if geo_key not in self.geo_metadata: continue
                    self.set_contact_name() 
                elif "contact_address" in geo_key:self.set_address()               
                elif geo_key == "contact_email":
                    self.contact["email"]=";".join(self.geo_metadata["contact_email"]) 
                elif geo_key == "contact_phone":
                    self.contact["phone"]=";".join(self.geo_metadata["contact_phone"])
                elif geo_key == "contact_institute":
                    self.contact["affiliation"]=";".join(self.geo_metadata["contact_institute"])
        except:pass

    def get_contact(self):
        contact={}
        for node in self.idf_contact_model.findall("./node"):
            field_id=node.attrib["id"]
            field_label=node.attrib["label"]
            contact[field_label]=self.contact[field_id]
        return contact
    
    def get_contact_role(self):
        contact={}
        for node in self.idf_contact_role_model.findall("./node"):
            field_id=node.attrib["id"]
            field_label=node.attrib["label"]
            contact[field_label]=""
        return contact
 
    def display(self):
        print("" )
        contact=self.get_contact()
        contact_role=self.get_contact_role()
        for label,content in contact.items():
            print("%s: %s" % (label,content))
        for label,content in contact_role.items():
            print("%s: %s" % (label,content))
        print("" )


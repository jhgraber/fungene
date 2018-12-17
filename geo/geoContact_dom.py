# -*- coding: utf-8 -*-
from os.path import join

"""
A data model for GEO Contact dataset.
See: https://geoparse.readthedocs.io/en/latest/GEOparse.html

ContactDOM:
   
Raises:
     Nothing
"""

class ContactDOM:
    def __init__(self,geo_obj_metadata):
        self.contributor=""
        self.contact_country=""
        self.contact_state=""
        self.contact_city=""
        self.contact_zip=""
        self.contact_name=""
        self.contact_address=""
        self.contact_department=""
        self.contact_institute=""
        self.contact_email=""
        self.contact_phone=""
        self.contact_laboratory=""
        self.__set(geo_obj_metadata)

    def __set(self,geo_obj_metadata):
        try:
            if "contributor" in geo_obj_metadata:
                self.contributor=";".join(geo_obj_metadata["contributor"])
            if "contact_country" in geo_obj_metadata:
                self.contact_country=";".join(geo_obj_metadata["contact_country"])
            if "contact_state" in geo_obj_metadata:
                self.contact_state=";".join(geo_obj_metadata["contact_state"])
            if "contact_city" in geo_obj_metadata:
                self.contact_city=";".join(geo_obj_metadata["contact_city"])
            if "contact_zip/postal_code" in geo_obj_metadata:
                self.contact_zip=";".join(geo_obj_metadata["contact_zip/postal_code"])
            if "contact_name" in geo_obj_metadata:
                self.contact_name=";".join(geo_obj_metadata["contact_name"])
            if "contact_address" in geo_obj_metadata:
                self.contact_address=";".join(geo_obj_metadata["contact_address"])
            if "contact_department" in geo_obj_metadata:
                self.contact_department=";".join(geo_obj_metadata["contact_department"])
            if "contact_institute" in geo_obj_metadata:
                self.contact_institute=";".join(geo_obj_metadata["contact_institute"])
            if "contact_email" in geo_obj_metadata:
                self.contact_email=";".join(geo_obj_metadata["contact_email"])
            if "contact_phone" in geo_obj_metadata:
                self.contact_phone=";".join(geo_obj_metadata["contact_phone"])
            if "contact_laboratory" in geo_obj_metadata:
                self.contact_laboratory=";".join(geo_obj_metadata["contact_laboratory"])
        except:pass

    def display(self):
        print("=================" )
        print("Contributor(s):%s" % (self.contributor))
        print("Contact Name:%s" % (self.contact_name))
        print("Contact Country:%s" % (self.contact_country))
        print("Contact State:%s" % (self.contact_state))
        print("Contact City:%s" % (self.contact_city))
        print("Contact Zip/Postal Code:%s" % (self.contact_zip))
        print("Contact Address:%s" % (self.contact_address))
        print("Contact Email:%s" % (self.contact_email))
        print("Contact Phone:%s" % (self.contact_phone))
        print("Contact Institution:%s" % (self.contact_institute))
        print("Contact Department:%s" % (self.contact_department))
        print("Contact Laboratory:%s" % (self.contact_laboratory))
        print("=================" )




# -*- coding: utf-8 -*-
from os.path import join,isfile
import io,json
"""
Sets path to json models containing
data models for different controled vocab

Raises:
     Nothing
"""

class IdfCVocabModels:
    def __init__(self):
       
        self.efo_models_base="./../efo"

        self.organization_role_file=join(self.efo_models_base,"organization_role.json")
        self.publication_status_file=join(self.efo_models_base,"publication_status.json")
        self.protocol_file=join(self.efo_models_base,"protocol.json")
        self.replicat_terms_file=join(self.efo_models_base,"replicat_terms.json")
        self.exp_design_file=join(self.efo_models_base,"exp_design-biological-variation-design.json")
      

    def getJsonObj(self,json_file):
        json_obj={}
        if not isfile(json_file): 
            return json_obj
        try:
            json_obj=json.load(open(json_file))
        except:pass
        return json_obj

    def getRoles(self):
        return self.getJsonObj(self.organization_role_file)
    def getPubStatus(self):
        return self.getJsonObj(self.publication_status_file)
    def getProtocols(self):
        return self.getJsonObj(self.protocol_file)
    def getReplicat(self):
        return self.getJsonObj(self.replicat_terms_file)
    def getExpDesign(self):
        return self.getJsonObj(self.exp_design_file)
    
    ## this function generates all the controlled vocab terms
    ## of the user's specified category
    ##
    def getCVocabTermsList(self,vocab_fields,terms_container):
        terms_obj={}
        try:
            idf_term_label= vocab_fields["term"]
            idf_term_source_label= vocab_fields["term_source"]
            idf_term_accession_label= vocab_fields["term_accession"]
            for cat,cat_data in terms_container.items():
                if "terms" not in cat_data:continue
                terms=cat_data["terms"]
                for term_obj in terms:
                    term=term_obj["label"]
                    term_source=term_obj["ontology_prefix"]
                    is_obsolete=term_obj["is_obsolete"]
                    term_accession=term_obj["obo_id"]
                    if is_obsolete:continue
                    terms_obj[term_accession]={}
                    terms_obj[term_accession][idf_term_label]=term
                    terms_obj[term_accession][idf_term_source_label]=term_source
                    terms_obj[term_accession][idf_term_accession_label]=term_accession
        except:pass
        return terms_obj

    ## This function set user's specifed ontology terms
    ## for the targeted vocab
    ##
    def getCVocabTerms(self,title_prompt,vocab_fields,terms_container):
        terms_obj={}
        try:
            idf_term_label= vocab_fields["term"]
            idf_term_source_label= vocab_fields["term_source"]
            idf_term_accession_label= vocab_fields["term_accession"]
            acceptable=["y","n"]
            print("--------------------------")
            print("%s"%(title_prompt))
            print("--------------------------")
            for cat,cat_data in terms_container.items():
                if "terms" not in cat_data:continue
                terms=cat_data["terms"]
                for term_obj in terms:
                    term=term_obj["label"]
                    term_source=term_obj["ontology_prefix"]
                    is_obsolete=term_obj["is_obsolete"]
                    term_accession=term_obj["obo_id"]
                    if is_obsolete:continue
                    role_status=""
                    try:
                        role_status=input("%s (y/n):"%(term))
                    except:
                        role_status=raw_input("%s (y/n):"%(term))
                    if role_status.lower() not in acceptable:continue
                    if role_status.lower() == "n":continue
                    terms_obj[term_accession]={}
                    for field_id,field_label in vocab_fields.items():
                        if "term" not in field_id:
                            terms_obj[term_accession][field_label]=""
                    terms_obj[term_accession][idf_term_label]=term
                    terms_obj[term_accession][idf_term_source_label]=term_source
                    terms_obj[term_accession][idf_term_accession_label]=term_accession
                    

        except:pass
        return terms_obj


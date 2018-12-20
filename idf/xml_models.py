# -*- coding: utf-8 -*-
from os.path import join,isfile
import xml.etree.ElementTree as ET

"""
Sets path to xml models containing
data models for different sections of an IDF file

Raises:
     Nothing
"""

class IdfXmlModels:
    def __init__(self):
       
        self.models_base="./xml"

        self.idf_file=join(self.models_base,"idf.xml")
        self.experiment_file=join(self.models_base,"experiment.xml")
        self.experiment_contact_file=join(self.models_base,"experiment_contact.xml")
        self.experiment_contact_role_file=join(self.models_base,"experiment_contact_role.xml")
        self.experiment_design_file=join(self.models_base,"experiment_design.xml")
        self.experiment_factor_file=join(self.models_base,"experiment_factor.xml")
        self.experiment_normalization_file=join(self.models_base,"experiment_normalization.xml")
        self.experiment_protocol_file=join(self.models_base,"experiment_protocol.xml")
        self.experiment_publication_file=join(self.models_base,"experiment_publication.xml")
        self.experiment_publication_status_file=join(self.models_base,"experiment_publication_status.xml")
        self.experiment_qc_file=join(self.models_base,"experiment_qc.xml")
        self.experiment_replicat_file=join(self.models_base,"experiment_replicat.xml")
        self.experiment_terms_file=join(self.models_base,"experiment_terms.xml")
        self.experiment_comments_file=join(self.models_base,"experiment_comments.xml")
      

    def getXmlDocRoot(self,xml_file):
        doc_root=None
        if not isfile(xml_file): 
            return doc_root
        try:
            xml_doc=ET.parse(xml_file)
            doc_root=xml_doc.getroot()
        except:raise
        return doc_root

    def getIdfPage(self):
        return self.getXmlDocRoot(self.idf_file)
    def getExperiment(self):
        return self.getXmlDocRoot(self.experiment_file)
    def getExperimentContact(self):
        return self.getXmlDocRoot(self.experiment_contact_file)
    def getExperimentContactRole(self):
        return self.getXmlDocRoot(self.experiment_contact_role_file)
    def getExperimentDesign(self):
        return self.getXmlDocRoot(self.experiment_design_file)
    def getExperimentFactor(self):
        return self.getXmlDocRoot(self.experiment_factor_file)
    def getExperimentNormalization(self):
        return self.getXmlDocRoot(self.experiment_normalization_file)
    def getExperimentProtocol(self):
        return self.getXmlDocRoot(self.experiment_protocol_file)
    def getExperimentPublication(self):
        return self.getXmlDocRoot(self.experiment_publication_file)
    def getExperimentPublicationStatus(self):
        return self.getXmlDocRoot(self.experiment_publication_status_file)
    def getExperimentQc(self):
        return self.getXmlDocRoot(self.experiment_qc_file)
    def getExperimentReplicat(self):
        return self.getXmlDocRoot(self.experiment_replicat_file)
    def getExperimentTerms(self):
        return self.getXmlDocRoot(self.experiment_terms_file)
    def getExperimentComments(self):
        return self.getXmlDocRoot(self.experiment_comments_file)

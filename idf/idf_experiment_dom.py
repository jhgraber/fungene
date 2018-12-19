# -*- coding: utf-8 -*-
from os.path import join

"""
A data model for IDF Experiment/Experiment Design/Experiment Factor datasets.
See: https://www.ebi.ac.uk/arrayexpress/help/creating_an_idf.html

ContactDOM:
   
Raises:
     Nothing
"""
from xml_models import IdfXmlModels
from json_models import IdfCVocabModels

idf_models=IdfXmlModels()
controled_vocab_models=IdfCVocabModels()

class ExperimentDOM:
    def __init__(self,geo_obj_metadata):
        self.geo_metadata=geo_obj_metadata
        self.idf_experiment_model=idf_models.getExperiment()
        self.idf_experiment_design_model=idf_models.getExperimentDesign()

        self.idf_experiment_factor_model=idf_models.getExperimentFactor()
        self.idf_experiment_qc_model=idf_models.getExperimentQc()
        self.idf_experiment_norm_model=idf_models.getExperimentNormalization()

        self.idf_experiment_replicate_model=idf_models.getExperimentReplicat()
        self.idf_experiment_protocol_model=idf_models.getExperimentProtocol()
        self.idf_experiment_pub_status_model=idf_models.getExperimentPublicationStatus()

        self.idf_experiment_pub_model=idf_models.getExperimentPublication()

        self.idf_experiment_terms_model=idf_models.getExperimentTerms()
        self.idf_experiment_comments_model=idf_models.getExperimentComments()
        self.experiment={}
        self.__set()

    def set_experiment(self):
        try:
            fields= self.idf_experiment_model.findall("./node")
            for node in fields:
                field_id=node.attrib["id"]
                geo_key=node.attrib["geo_key"]
                title=node.attrib["label"]
                if self.geo_metadata is not None:
                    if geo_key in self.geo_metadata:
                       self.experiment[title]=";".join(self.geo_metadata[geo_key])
                else:self.experiment[title]=""
        except:pass

    def __set(self):
        try:
            self.set_experiment()
        except:pass
    def get_experiment_pub(self):
        container={}
        try:
            for node in self.idf_experiment_pub_model.findall("./node"):
                field_id=node.attrib["id"]
                field_label=node.attrib["label"]
                geo_key=node.attrib["geo_key"]
                if self.geo_metadata is not None:
                    if geo_key in self.geo_metadata:
                        container[field_label]=";".join(self.geo_metadata[geo_key])
                else:container[field_label]=""
        except:pass
        return container

    def get_experiment_comments(self):
        container={}
        try:
            for node in self.idf_experiment_comments_model.findall("./node"):
                field_label=node.attrib["label"]+"["+node.attrib["user_defined_tag"]+"]"
                geo_key=node.attrib["geo_key"]
                if self.geo_metadata is not None:
                    if geo_key in self.geo_metadata:
                        container[field_label]=";".join(self.geo_metadata[geo_key])
                else:container[field_label]=""
        except:pass
        return container
    ## Controled vocabulary
    def get_experiment_pub_status(self):
        container={}
        fields={}
        try:
            for node in self.idf_experiment_pub_status_model.findall("./node"):
                field_id=node.attrib["id"]
                fields[field_id]=node.attrib["label"]
            terms_container=controled_vocab_models.getPubStatus()
            title_prompt="Specify The Publication Status" 
            #container=controled_vocab_models.getCVocabTerms(title_prompt,fields,terms_container)
            container=controled_vocab_models.getCVocabTermsList(fields,terms_container)
        except:pass
        return container
    ## Controled vocabulary
    def get_experiment_design(self):
        container={}
        fields={}
        for node in self.idf_experiment_design_model.findall("./node"):
            field_id=node.attrib["id"]
            fields[field_id]=node.attrib["label"]
        terms_container=controled_vocab_models.getExpDesign()
        title_prompt="Specify the experiment design types which are applicable to this study"
        #container=controled_vocab_models.getCVocabTerms(title_prompt,fields,terms_container)
        container=controled_vocab_models.getCVocabTermsList(fields,terms_container)
        return container
    ## Controled vocabulary 
    def get_experiment_factor(self):
        container={}
        for node in self.idf_experiment_factor_model.findall("./node"):
            field_id=node.attrib["id"]
            field_label=node.attrib["label"]
            container[field_label]=""
        return container
    ## Controled vocabulary 
    def get_experiment_qc(self):
        container={}
        for node in self.idf_experiment_qc_model.findall("./node"):
            field_id=node.attrib["id"]
            field_label=node.attrib["label"]
            container[field_label]=""
        return container
    ## Controled vocabulary 
    def get_experiment_replicate(self):
        container={}
        replicate_fields={}
        try: 
            for node in self.idf_experiment_replicate_model.findall("./node"):
                field_id=node.attrib["id"]
                replicate_fields[field_id]=node.attrib["label"]
            terms_container=controled_vocab_models.getReplicat()
            title_prompt="Specify The Replicate Strategies Used"
            container=controled_vocab_models.getCVocabTermsList(replicate_fields,terms_container)
        except:pass
        return container

    ## Controled vocabulary 
    def get_experiment_norm(self):
        container={}
        for node in self.idf_experiment_norm_model.findall("./node"):
            field_id=node.attrib["id"]
            field_label=node.attrib["label"]
            container[field_label]=""
        return container

    ## Controled vocabulary 
    def get_experiment_protocol(self):
        container={}
        fields={}
        for node in self.idf_experiment_protocol_model.findall("./node"):
            field_id=node.attrib["id"]
            fields[field_id]=node.attrib["label"]
            
        terms_container=controled_vocab_models.getProtocols()
        title_prompt="Specify The Protocol(s) Used"
        container=controled_vocab_models.getCVocabTermsList(fields,terms_container)
        return container

    ## Controled vocabulary 
    def get_experiment_terms(self):
        container={}
        for node in self.idf_experiment_terms_model.findall("./node"):
            field_id=node.attrib["id"]
            field_label=node.attrib["label"]
            container[field_label]=""
        return container

    def getXmlBlock(self):
        container=[]
        container.append("  <section id='experiment'>\n")
        for label,content in self.experiment.items():
             container.append('    <tag label="'+label+'"><![CDATA['+content+']]></tag>'+"\n")
        container.append("  </section>\n")
        container.append("  <section id='experiment_design'>\n")
        for  term_id,terms in self.get_experiment_design().items():
            container.append('    <term id="'+term_id+'">\n')
            for label,content in terms.items():
                container.append('      <tag label="'+label+'"><![CDATA['+content+']]></tag>'+"\n")
            container.append("    </term>\n")
        container.append("  </section>\n")
        container.append("  <section id='experiment_factor'>\n")
        for label,content in self.get_experiment_factor().items():
            container.append('    <tag label="'+label+'"><![CDATA['+content+']]></tag>'+"\n")
        container.append("  </section>\n")
        container.append("  <section id='experiment_qc'>\n")
        for label,content in self.get_experiment_qc().items():
            container.append('    <tag label="'+label+'"><![CDATA['+content+']]></tag>'+"\n")
        container.append("  </section>\n")
        container.append("  <section id='experiment_replicate'>\n")
        for term_id,terms in self.get_experiment_replicate().items():
            container.append('    <term id="'+term_id+'">\n')
            for label,content in terms.items():
                container.append('      <tag label="'+label+'"><![CDATA['+content+']]></tag>'+"\n")
            container.append("    </term>\n")
        container.append("  </section>\n")
        container.append("  <section id='experiment_normalization'>\n")
        for label,content in self.get_experiment_norm().items():
            container.append('    <tag label="'+label+'"><![CDATA['+content+']]></tag>'+"\n")
        container.append("  </section>\n")
        container.append("  <section id='experiment_publication'>\n") 
        for label,content in self.get_experiment_pub().items():
            container.append('    <tag label="'+label+'"><![CDATA['+content+']]></tag>'+"\n")
        container.append("  </section>\n") 
        container.append("  <section id='experiment_publication_status'>\n") 
        for term_id,terms in self.get_experiment_pub_status().items():
            container.append('    <term id="'+term_id+'">\n')
            for label,content in terms.items():
                container.append('      <tag label="'+label+'"><![CDATA['+content+']]></tag>'+"\n")
            container.append('    </term>\n')
        container.append("  </section>\n") 
        container.append("  <section id='experiment_protocol'>\n")
        for term_id,terms in self.get_experiment_protocol().items():
            container.append('    <term id="'+term_id+'">\n')
            for label,content in terms.items():
                container.append('      <tag label="'+label+'"><![CDATA['+content+']]></tag>'+"\n")
            container.append('    </term>\n')
        container.append("  </section>\n")
        container.append("  <section id='experiment_terms'>\n")
        for label,content in self.get_experiment_terms().items():
            container.append('    <tag label="'+label+'"><![CDATA['+content+']]></tag>'+"\n")
        container.append("  </section>\n")
        container.append("  <section id='experiment_comments'>\n")
        for label,content in self.get_experiment_comments().items():
            container.append('    <tag label="'+label+'"><![CDATA['+content+']]></tag>'+"\n")
        container.append("  </section>\n")
        return "".join(container)

    def display(self,fd):
        for label,content in self.experiment.items():
            fd.write("%s\t%s\n" % (label,content))
        fd.write("\n")
        for term_id,terms in self.get_experiment_design().items():
            for label,content in terms.items():
                fd.write("%s\t%s\n" % (label,content))
        fd.write("\n")
        for label,content in self.get_experiment_factor().items():
            fd.write("%s\t%s\n" % (label,content))
        fd.write("\n")
        for label,content in self.get_experiment_qc().items():
            fd.write("%s\t%s\n" % (label,content))
        fd.write("\n" )
        for term_id,terms in self.get_experiment_replicate().items():
            for label,content in terms.items():
                fd.write("%s\t%s\n" % (label,content))
        fd.write("\n")
        for label,content in self.get_experiment_norm().items():
            fd.write("%s\t%s\n" % (label,content))
        fd.write("\n")
        for label,content in self.get_experiment_pub().items():
            fd.write("%s\t%s\n" % (label,content))
        for term_id,terms in self.get_experiment_pub_status().items():
            for label,content in terms.items():
                fd.write("%s\t%s\n" % (label,content))
        fd.write("\n" )
        for term_id,terms in self.get_experiment_protocol().items():
            for label,content in terms.items():
                fd.write("%s\t%s\n" % (label,content))
        fd.write("\n")
        for label,content in self.get_experiment_terms().items():
            fd.write("%s\t%s\n" % (label,content))
        fd.write("\n")
        for label,content in self.get_experiment_comments().items():
            fd.write("%s\t%s\n" % (label,content))
        fd.write("\n")

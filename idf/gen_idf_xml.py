# -*- coding: utf-8 -*-
import getopt,os,sys,re
from idf_dom import IdfFileXmlDOM

def prog_usage():
    usage='''
       ****************** gen_idf_xml ********************************************************

           The tool generates an intermediary idf file in xml format in which
           each field that is a controlled vocabulary has a list of non-obsolute 
           EFO controled vocab terms for a given idf field.

           In addition to controlled vocab, for experiment found in GEO database, 
           the tool also extracts the metadata from the GEO database to pre-fill 
           the corresponding idf fields.

           The generated xml file is edited to filter out un-needed vocab terms and
           fill in empty fields. 

       ***************************************************************************************
       Usage: PROG [-h] --geoid=gse_accession --destdir=path2/experiment_base
       Where:
           -h To show the usage
           -i gse_accession Or --geoid=gse_accession  ... required, specifies the Experiment Geo id or user's specified id
           -d experiment_base Or  --destdir=experiment_base ... optional default working directory
      
      
       Example 1: The experiment has a GEO GSE ID (experiment is in GEO database)
           python gen_idf_xml  -i GSE64403 -d /data/projects/Biocore/regendb/experiments_staging
           OR python gen_idf_xml --geoid=GSE64403 --destdir=/data/projects/Biocore/regendb/experiments_staging
           
           THIS will store the idf file for this experiment under /data/projects/Biocore/regendb/experiments_staging/GSE64403/
      
       Example 2: The experiment does not have a GEO ID (private or non-published)
           python gen_idf_xml  -i EXPA -d /data/projects/Biocore/regendb/experiments_staging
           OR python gen_idf_xml --geoid=EXPA --destdir=/data/projects/Biocore/regendb/experiments_staging
          
           THIS will store the idf file  for this experiment under /data/projects/Biocore/regendb/experiments_staging/auto_EXPA/
    '''
    print("%s"%(usage))

if __name__== "__main__":
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hi:d:", 
                    ["help", "geoid=","destdir="])
    except(getopt.GetoptError, err):
        # print help information and exit:
        log.write(str(err)) # will print something like "option -a not recognized"
        print("ERROR:%s" % (str(err) )) # will print something like "option -a not recognized"
        prog_usage()
        sys.exit(1)
    #set program arguments
    experiment_geo_acc=None
    experiment_dir=None
    for o, a in opts:
        if o in ("-i", "--geoid"):experiment_geo_acc = a
        elif o in ("-d", "--destdir"):experiment_dir = a
        elif o in ("-h", "--help"):
            prog_usage()
            sys.exit(1)
        else:
            assert False, "unhandled option"
   
    if experiment_geo_acc is None:
        prog_usage()
        sys.exit(1)
    if experiment_dir is None:
        experiment_dir="."
    gp= re.compile(r'^gse\d+$',re.IGNORECASE)
    m = gp.match(experiment_geo_acc)
    if m is None:
        experiment_geo_acc="auto_"+experiment_geo_acc
    experiment_dir=experiment_dir+"/"+experiment_geo_acc
    try:
        ## Create an experiment object
        experiment=IdfFileXmlDOM(experiment_geo_acc,experiment_dir)
        ## Generate the idf xml file draft to be used  to generate the final idf file
        experiment.gen_xml()
        sys.exit(0)
    except:raise

# -*- coding: utf-8 -*-
import getopt,os,sys,re
from os.path import isdir, isfile,join
from idf_dom import IdfFileDOM

def prog_usage():
    usage='''
       ****************** gen_idf ********************************************************

       The tool generates and stores the experiment idf file under the specified destdir  .

       ***************************************************************************************

       Usage: PROG [-h] --geoid=gse_accession --destdir=path2/experiment_base 
       Where:
           -h To show the usage
           -i gse_accession Or --geoid=gse_accession  ... required, specifies the ExperimentID
           -d experiment_base Or  --destdir=experiment_base ... optional default working directory
      
      
       Example: 
           python PROG  -i GSE64403 -d /data/projects/Biocore/regendb/experiments_staging
           OR python PROG --geoid=GSE64403 --destdir=/data/projects/Biocore/regendb/experiments_staging
           
      ASSUMPTIONS: PROG expects to find the following two files under --destdir:
      1) ExperimentID.idf.xml
      2) ExperimentID.cfg
   
     PROG generates ExperimentID.idf.txt file under --destdir

    '''
    print("%s"%(usage))

if __name__== "__main__":
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hi:d:", 
                    ["help", "geoid=","destdir="])
    except getopt.GetoptError  as err:
        # print help information and exit:
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
            sys.exit()
        else:
            assert False, "unhandled option"
    if experiment_geo_acc is None:
        prog_usage()
        sys.exit()
    if experiment_dir is None:
        experiment_dir="."
    gp= re.compile(r'^gse\d+$',re.IGNORECASE)
    m = gp.match(experiment_geo_acc)
    if m is None:
        experiment_geo_acc="auto_"+experiment_geo_acc
    experiment_dir=experiment_dir+"/"+experiment_geo_acc
    ## Create an experiment object
    idf_obj=IdfFileDOM(experiment_geo_acc,experiment_dir)
    ##check input files
    if not isfile(idf_obj.cfg_file):
        print("FAILED: Controlled vocab config file missing - expected: %s"%(idf_obj.cfg_file))
        sys.exit(1)
    if not isfile(idf_obj.idf_xml_file):
        print("FAILED: Idf xml draft file missing - expected: %s"%(idf_obj.idf_xml_file))
        sys.exit(1)
    idf_obj.gen_idf()
    sys.exit()

# -*- coding: utf-8 -*-
import getopt,os,sys
from geoExperiment_dom import GeoExperimentDOM

def browsegeo_usage():
    usage='''
       Usage: PROG [-h] --geoid=gse_accession --destdir=path2/exeperiment_base
       Where:
           -h To show the usage
           -i gse_accession Or --geoid=gse_accession  ... required, specifies the Experiment Geo id
           -d exeperiment_base Or  --destdir=exeperiment_base ... optional default working directory
           -x  Or  --experiment to display the experiment metadata including contact ... optional
           -c  Or  --contact to display the experiment's contact info ... optional
           -p  Or  --platform to display the experiment's platform info ... optional     
           -s  Or  --samples to display the experiment's samples ... optional
      
       Example:
           python PROG -i GSE64403 -d /path2experiments/GSE64403
           OR python PROG --geoid=GSE64403 --destdir=/path2experiments/GSE64403
           OR python PROG --geoid=GSE64403 --destdir=/path2experiments/GSE64403 -c
              to display the contact info
    '''
    print("%s"%(usage))

if __name__== "__main__":
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hi:d:cxps", 
                    ["help", "geoid=","destdir=","experiment","contact","platform","samples","sid="])
    except(getopt.GetoptError, err):
        # print help information and exit:
        log.write(str(err)) # will print something like "option -a not recognized"
        print("ERROR:%s" % (str(err) )) # will print something like "option -a not recognized"
        browsegeo_usage()
        sys.exit(1)
    #set program arguments
    show_contact=False
    show_experiment=False
    show_platform=False
    show_samples=False
    experiment_geo_acc=None
    sample_geo_acc=None
    experiment_dir=None
    for o, a in opts:
        if o in ("-c","--contact"):show_contact = True
        elif o in ("-x","--experiment"):show_experiment = True
        elif o in ("-p","--platform"):show_platform = True
        elif o in ("-s","--samples"):show_samples = True
        elif o in ("-i", "--geoid"):experiment_geo_acc = a
        elif o in ("-d", "--destdir"):experiment_dir = a
        elif o in ("--sid"):sample_geo_acc = a
        elif o in ("-h", "--help"):
            browsegeo_usage()
            sys.exit()
        else:
            assert False, "unhandled option"
   
    if experiment_geo_acc is None:
        browsegeo_usage()
        sys.exit()
    if experiment_dir is None:
        experiment_dir="./"
    ## Create an experiment object
    experiment=GeoExperimentDOM(experiment_geo_acc,experiment_dir)
    if show_contact:
        experiment.show_contact()
    elif show_platform:
        experiment.show_platforms()
    elif show_experiment:
        experiment.show_experiment()
    elif show_samples:
        experiment.show_samples(sample_geo_acc) 
    else:
        experiment.show_serie()
            
    sys.exit()

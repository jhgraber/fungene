# -*- coding: utf-8 -*-
import getopt,os,sys
from os import makedirs
from os.path import isdir,dirname,abspath,basename
from glob import glob
from file_dom import MatrixDOM

def prog_usage():
    usage='''
       ****************** gen_matrix ********************************************************

       The tool generates a matrix file under the specified destdir  .

       ***************************************************************************************

       Usage: PROG [-h] --infiles=files --outdir=path2/output_prefix --jindex=indexOfColumnValues \
                        [--vindex=indexOfRowIDs] [--round]
       Where:
           -h To show the usage
           -i path2/files Or --infiles=path2/files  ... required, specifies a commas-separated(or a wildcard)list of input files 
                        (takes wildcard)
           -o path2/output_prefix Or  --outdir=path2/output_prefix ... required, default results dir is working directory
           -j indexOfColumnValues or --jindex=indexOfColumnValues ... required, specifies the column index of the values  
           -v indexOfRowIDs or --vindex=indexOfRowIDs ... optional default first column(index=0)  
           --round or -r   
      
       Output: Generate a matrix file under the path2 part of --outdir - 
               where the format of the results file is output_prefix.jindex_column_name.matrix.txt 

       Example: 
           python PROG  -i input_path2/project1/*.genes.resutls -o out_path2/project1/genes -j 4 
           OR 
           python PROG --infiles=input_path2/project1/*.genes.results --outdir=out_path2/project1/genes --jindex=4
           
      ASSUMPTIONS: 
           1) User has full permission to create the results directory specified in --outdir
    '''
    print("%s"%(usage))

if __name__== "__main__":
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hi:o:j:v:r", 
                    ["help", "infiles=","outdir=","jindex","vindex","round"])
    except getopt.GetoptError as err:
        # print help information and exit:
        print("ERROR:%s" % (str(err) )) # will print something like "option -a not recognized"
        prog_usage()
        sys.exit(1)
    #set program arguments
    input_files=None
    output_dir=None
    _jindex=None
    _vindex=0
    _round=False
    for o, a in opts:
        if o in ("-i", "--infiles"):input_files = a
        elif o in ("-o", "--outdir"):output_dir = a
        elif o in ("-j","--jindex"):_jindex=a
        elif o in ("-v","--vindex"):_vindex=a 
        elif o in ("-r","--round"):_round=True
        elif o in ("-h", "--help"):
            prog_usage()
            sys.exit()
        else:
            assert False, "unhandled option"
    ## Create output directory as needed
    destdir_base=dirname(abspath(output_dir))
    output_prefix=basename(output_dir)
    if not isdir(destdir_base):
        makedirs(destdir_base,mode=0777)
    ## Get a list of input files
    input_files_list=[]
    if '*' in input_files:
        input_files_list=glob(input_files)
    else:
        input_files_list=input_files.split(',')
    ## Create a matrix object
    matrix_obj=MatrixDOM(input_files_list,_vindex,_jindex,_round)
    sys.exit()

from os.path import dirname,abspath,isfile
from glob import glob
from file_dom import MatrixDOM
# -*- coding: utf-8 -*-
import getopt,os,sys,re
from os.path import isdir, isfile,join
from idf_dom import IdfFileDOM

def prog_usage():
    usage='''
       ****************** gen_matrix ********************************************************

       The tool generates and a matrix file under the specified destdir  .

       ***************************************************************************************

       Usage: PROG [-h] --infiles=files --outdir=path2/output_prefix --jindex=indexOfColumnValues \
                        [--vindex=indexOfRowIDs] [--round]
       Where:
           -h To show the usage
           -i files Or --infiles=files  ... required, specifies the commas-separated(or a wildcard)list of input files 
           -o path2/output_prefix Or  --outdir=path2/output_prefix ... required, default results dir is working directory
           -j indexOfColumnValues or --jindex=indexOfColumnValues ... required, specifies the column index of the values  
           -v indexOfRowIDs or --vindex=indexOfRowIDs ... optional default first column(index=0)  
           --round or -r   
      
      
       Example: 
           python PROG  -i GSE64403 -d /data/projects/Biocore/regendb/experiments_staging
           OR python PROG --geoid=GSE64403 --destdir=/data/projects/Biocore/regendb/experiments_staging
           
      ASSUMPTIONS: PROG expects to find the following two files under --destdir:
      1) ExperimentID.idf.xml
      2) ExperimentID.cfg
   
     PROG generates ExperimentID.idf.txt file under --destdir

    '''


#input_files="test.matrix doc.matrix log.matrix"
input_files="*test.matrix"
file_list=input_files.split(' ')
dir_base=dirname(abspath(input_files))
print(file_list,dir_base)
for filename in file_list:
    print (filename)


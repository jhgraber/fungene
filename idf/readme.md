# IDF GENERATOR

A python package that generates the idf file for a given experiment.
The main shell script - idfGenerator - is a wrapper script that calls 
the main pyhton scripts after setting some global environment variables.

## Usage: ./idfGenerator experimentID [experiment_base_dir]
```
  WHERE:
  experimentID        -- (Required) is the iddentifier of the experiment(could be a geo ID, ...)
  experiment_base_dir -- (Optional) is the root directory of the experiment - default working directory 

  Example1: ./idfGenerator GSE64403  /data/projects/Biocore/regendb/experiments_staging
  Example2: ./idfGenerator GSE64403 
 
  Example1 stores the resulting files under /data/projects/Biocore/regendb/experiments_staging/GSE64403
  Example2 stores the resulting files under the working directory ./GSE64403

```

## Dependencies

### Pyhton Modules
```
 1) xml.etree.ElementTree
 2) json
 3) GEOparse

```

## Pyhton Scritps

The following two scripts are expected to be in the same directory as the wrapper script
```
  1) gen_idf_xml.py
  2) gen_idf.py
```

### gen_idf_xml.py

The tool generates an intermediary idf xml file using the idf defined data model.
Each field that is a controlled vocabulary has the associated list of non-obsolute EFO controled vocab terms.
           
In addition to controlled vocab, for experiment found in GEO database, 
the tool also extracts the metadata from the GEO database to pre-fill the corresponding idf fields.

The generated xml file is edited by the gen_idf.py program to filter out un-needed vocab terms and
fill in empty fields. 

'''
 Usage: PROG [-h] --geoid=gse_accession --destdir=path2/experiment_base
 Where:
      -h To show the usage
      -i gse_accession Or --geoid=gse_accession  ... required, specifies the Experiment Geo id or user s specified id
      -d experiment_base Or  --destdir=experiment_base ... optional default working directory
      
 Example 1: The experiment has a GEO GSE ID (experiment is in GEO database)
 cmd: python gen_idf_xml  -i GSE64403 -d /data/projects/Biocore/regendb/experiments_staging
      OR 
      python gen_idf_xml --geoid=GSE64403 --destdir=/data/projects/Biocore/regendb/experiments_staging

 THIS will store the idf file for this experiment under /data/projects/Biocore/regendb/experiments_staging/GSE64403/

 Example 2: The experiment does not have a GEO ID (private or non-published)
 cmd:  python gen_idf_xml  -i EXPA -d /data/projects/Biocore/regendb/experiments_staging
       OR 
       python gen_idf_xml --geoid=EXPA --destdir=/data/projects/Biocore/regendb/experiments_staging
          
 THIS will store the idf file  for this experiment under /data/projects/Biocore/regendb/experiments_staging/auto_EXPA/
'''
### gen_idf.py

The tool generates and stores the experiment idf file under the specified destdir  .

```
 Usage: PROG [-h] --geoid=gse_accession --destdir=path2/experiment_base 
 Where:
      -h To show the usage
      -i gse_accession Or --geoid=gse_accession  ... required, specifies the ExperimentID
      -d experiment_base Or  --destdir=experiment_base ... optional default working directory
      
 Example: 
 cmd: python PROG  -i GSE64403 -d /data/projects/Biocore/regendb/experiments_staging
      OR 
      python PROG --geoid=GSE64403 --destdir=/data/projects/Biocore/regendb/experiments_staging
           
```

ASSUMPTIONS: PROG expects to find the following two files under --destdir:
      1) ExperimentID.idf.xml
      2) ExperimentID.cfg
   
The program generates ExperimentID.idf.txt file under --destdir

## Configuration files

The experiment controled vacabulary configuration file.
This file is key/value pair tab-separated file where each controlled vocabulary
has the assocated list of term IDs that apply to the currrent experiment.

The file is stored under the root directory of the experiment.

```
Example of the file content:

experiment_contact_role EFO:0001741,EFO:0001739
experiment_design       EFO:0001779,EFO:0001750,EFO:0001759
experiment_replicate    EFO:0002091
experiment_publication_status   EFO:0001796
experiment_protocol     EFO:0003788,EFO:0005518
```


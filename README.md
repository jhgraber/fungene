# Functional Genomic Experiments Utilities

A set of utilities to parse and process data
from different types of Functional Genomic Experiments

Clone this repos locally to use the tools
```
  1) git clone https://github.com/mdibl/fungene.git
  2) then cd to fungene

```
## idfGenerator

To run the idfGenerator:

```Usage: ./idfGenerator experimentID [experiment_base_dir] ```

1) cd to fungene/idf
2) then run ./idfGenerator 
```
 The above command will check for the required python modules and show you the usage - 
```
```
     Usage: ./idfGenerator experimentID [experiment_base_dir]
  
     WHERE:
         experimentID        -- (Required) is the iddentifier of the experiment(could be a geo ID, ...)
         experiment_base_dir -- (Optional) is the root directory of the experiment - default working directory 
         
         Example1: ./idfGenerator GSE64403  /data/projects/Biocore/regendb/experiments_staging
         Example2: ./idfGenerator GSE64403
  
         Example1 stores the resulting files under /data/projects/Biocore/regendb/experiments_staging/GSE64403
         Example2 stores the resulting files under the working directory ./GSE64403
```




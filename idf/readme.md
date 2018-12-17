## Steps To Generate The IDF File

### 1) Generate The experiment idf.xml file 

cd to regendb_loader/idf and run python gen_idf_xml.py
```
 Usage: python gen_idf_xml.py -i experiment_id -d experiment_base_directory
 
 Run the program with -h option or without any argument to see the usage
 
 Example: pyhton gen_idf_xml.py 
               OR
          pyhton gen_idf_xml.py -h
    
```
#### What the program does:
1) Create a local id for this experiment if the provided experiment id is not a GEO ID
2) Creates a base directory for this experiment  if not exist
3) Fetches the experiment data from GEO database if exists 
4) Creates an idf data model for this experiment - with current controlled vocabs 
5) Generates a draft of the idf file in xml format each experiment sub-process containing
   a list of current EFO controlled vocab terms 

### 2)  Edit The experiment *.idf.xml file (Done by someone familar with the experiment)
Update each section of the xml file as needed.
```
 <experiment_contact />
 <experiment_contact_role />
 <experiment />
 <experiment_design />
 <experiment_factor />
 <experiment_qc />
 <experiment_replicate />
 <experiment_normalization />
 <experiment_publication />
 <experiment_publication_status />
 <experiment_protocol />
 <experiment_terms />
 <experiment_comments />
```

### 3) Generate The IDF text file

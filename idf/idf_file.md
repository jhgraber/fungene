## IDF, SDRF, and ADF Specs

See: http://www.fged.org/site_media/pdf/MAGE-TABv1.1_2011_07_28.pdf

## Creating an IDF

1) Experiment
  - Investigation Title : geo_exp.title?
  - Experiment Description: geo_exp.summary?
  - Date of Experiment: geo_exp.submission_date?
  
2) Exeperiment Design:(Controled vocab - EFO)
   - Experimental Design
   - Experimental Design Term Source REF
   - Experimental Design Term Accession Number
   
   See: https://www.ebi.ac.uk/ols/api/ontologies/efo/terms/http%253A%252F%252Fwww.ebi.ac.uk%252Fefo%252FEFO_0004667/children
   
3) Experimental Factor: (Controled vocab - EFO)
   - Experimental Factor Name
   - Experimental Factor Type
   - Experimental Factor Term Source REF
   
   - Experimental Factor Term Accession Number
4) Contact
   - Person Last Name
   - Person First Name
   - Person Mid Initials
   - Person Email
   - Person Phone
   - Person Fax
   - Person Address
   - Person Affiliation
   
   - Person Roles: (Controled vocab - EFO)
   - Person Roles Term Source REF
   - Person Roles Term Accession Number
  ``` -- See https://www.ebi.ac.uk/ols/api/ontologies/efo/terms/http%253A%252F%252Fwww.ebi.ac.uk%252Fefo%252FEFO_0002012/children
  ```
 5) Quality Control: (Controled vocab - EFO)
   - Quality Control Type
   - Quality Control Term Source REF
   - Quality Control Term Accession Number
   ```
   Notes: Quality Control Type category is obsolete -- 
   See: https://www.ebi.ac.uk/ols/ontologies/efo/terms?short_form=EFO_0004107
   ```
 6) Replicate: (Controled vocab - EFO)
   - Replicate Type 
   - Replicate Term Source REF
   - Replicate Term Accession Number
  
  ```
   -- see: https://www.ebi.ac.uk/ols/ontologies/efo/terms?short_form=EFO_0000683
  ```
  
 7) Normalization
   - Normalization Type
   - Normalization Term Source REF
   - Normalization Term Accession Number 
 8) Publication
   - Public Release Date
   - PubMed ID
   - Publication DOI
   - Publication Author List
   - Publication Title
   - Publication Status -- see : https://www.ebi.ac.uk/ols/api/ontologies/efo/terms/http%253A%252F%252Fwww.ebi.ac.uk%252Fefo%252FEFO_0001742/children
   - Publication Status Term Source REF
   - Publication Status Term Accession Number
 9) Protocol
   - Protocol Name
   - Protocol Type --- see: https://www.ebi.ac.uk/ols/api/ontologies/efo/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FOBI_0000272/children
   - Protocol Description
   - Protocol Parameters
   - Protocol Hardware
   - Protocol Software
   - Protocol Contact
   - Protocol Term Source REF
   - Protocol Term Accession Number
 10) SDRF File
 11) Term
   - Term Source Name
   - Term Source File
   - Term Source Version
 12) Comment[< user-defined tag >]
 
 
See: https://www.ebi.ac.uk/arrayexpress/help/creating_an_idf.html

```
 
bash-4.2$ head -80 /data/projects/Biocore/regendb/experiments/REGENE25/REGENE25.idf.txt 
MAGE-TAB Version	1.1		
Investigation Title	mRNA expression profiling during zebrafish caudal fin regeneration		
Comment[Submitted Name]	mRNA expression profiling during zebrafish caudal fin regeneration		
Experimental Design	time_series_design	co-expression_design	transcription profiling by array
Experimental Design Term Source REF	mo	mo	EFO
Experimental Design Term Accession Number			
Experimental Factor Name	Time	Tissue Class	Organism Part
Experimental Factor Type	time	organism part	organism part
Experimental Factor Term Source REF	EFO	EFO	EFO
Experimental Factor Term Accession Number	EFO_0000721	EFO_0000635	EFO_0000635

Person Last Name	King		
Person First Name	Benjamin		
Person Mid Initials	L		
Person Email	bking@mdibl.org		
Person Phone	2072883605		
Person Fax	
Person Address	"Mount Desert Island Biological Laboratory, PO Box 35, Salisbury Cove, ME, USA"
Person Affiliation	Mount Desert Island Biological Laboratory
Person Roles	submitter
Person Roles Term Source REF	EFO
Person Roles Term Accession Number	EFO_0001741

Quality Control Type	
Quality Control Term Source REF	
Quality Control Term Accession Number	
Replicate Type	
Replicate Term Source REF	
Replicate Term Accession Number	
Normalization Type	
Normalization Term Source REF	
Normalization Term Accession Number	

Date of Experiment			
Public Release Date	2016-06-01

PubMed ID	27355827		
Publication DOI	doi: 10.1371/journal.pone.0157106		
Publication Author List	"King BL, Yin VP"		
Publication Title	A conserved gene regulatory circuit is dynamically controlled during limb/appendage regeneration in three vertebrates		
Publication Status	published		
Publication Status Term Source REF	EFO		
Publication Status Term Accession Number	EFO_0001796		
Experiment Description	<p>Previous studies of zebrafish caudal fin regeneration have shown that multiple genetic programs are moduled through regulatory factors.  We characterized mRNA expression during zebrafish caudal fin regeneration at 0 and 4 days post amputation.</p><p>Experiment Overall Design: Zebrafish caudal fin tissues were gathered at 0 and 4dpa.</p>		

Protocol Name	P-G3667-7	P-G3667-1	P-G3667-3
Protocol Type	grow	specified_biomaterial_action	nucleic_acid_extraction
Protocol Description	Fish were maintained at 27oC until under standard conditions.	Adult Ekkwill (EK) zebrafish were housed and maintained in tanks at 22oC and exposed to a 12:12 hour light:dark cycle.	"Total RNA was isolated using TRI Reagent (Molecular Research Center, Inc., Cincinnati, OH) following manufacturer̢???s protocol. Illumina TruSeq small RNA and strand-specific PolyA+ mRNA libraries."
Protocol Software									
Protocol Hardware									
Protocol Contact									
Protocol Term Source REF						The MGED Ontology			
Protocol Term Accession Number									

SDRF File	REGENE24.sdrf.txt								

Term Source Name	mo		NCI_thesaurus	The MGED Ontology	ArrayExpress	nci_meta	mo	EFO	The MGED Ontology
Term Source File	http://mged.sourceforge.net/ontologies/MGEDontology.php		ncithesaurus.obo.alt	http://mged.sourceforge.net/ontologies/MGEDontology.php	http://www.ebi.ac.uk/arrayexpress	http://ncimeta.nci.nih.gov/indexMetaphrase.html	http://mged.sourceforge.net/ontologies/MGEDontology.php	http://www.ebi.ac.uk/efo/	http://mged.sourceforge.net/ontologies/MGEDontology.php
Term Source Version									

Comment[BlastDbName]									

Comment[RnaSegmentAccessionSource]	ENS								

Comment[ArrayExpressAccession]	E-GEOD-74415
Comment[GEOAccession]	GSE74415
Comment[RegenAccession]	REGENE:24
```

## Representing experimental variables with EFO
  See: https://www.ebi.ac.uk/efo/efo.obo
```
  EFO:
  id: string
  name: string
  def: text
  synonymn: string
  property_value: string
  .....
  property_value:string
  is_a: string

[term]
id: EFO:0000635
name: organism part
def: "The part of organism's anatomy or substance arising from an organism from which the biomaterial was derived, excludes cells. E.g. tissue, organ, system, sperm, blood or body location (arm)." []
synonym: "organism_part" EXACT []
property_value: bioportal:provenance "organism_part[accessedResource: MO_954][accessDate: 05-04-2011]" xsd:string
property_value: branch:class "true" xsd:string
property_value: http://www.ebi.ac.uk/efo/MO_definition_citation MO:954 xsd:string
property_value: http://www.ebi.ac.uk/efo/NCI_Thesaurus_definition_citation NCIt:C103199 xsd:string
property_value: IAO:0000112 "tissue, organ, system, sperm, blood or body location (arm)." xsd:string
property_value: IAO:0000117 "James Malone" xsd:string
property_value: IAO:0000117 "Jie Zheng" xsd:string
property_value: IAO:0000117 "Tomasz Adamusiak" xsd:string
is_a: BFO:0000040 ! material entity

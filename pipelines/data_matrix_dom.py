# -*- coding: utf-8 -*-
"""
A data model for resem epression results files (isoforms/genes).results.
RsemExpResultsDOM: defines data model for each line in resem epression results file
   Args: a line 
  
Returns:
     Sets global  
Raises:
     Nothing
"""
from os.path import isfile

class Field:
    def __init__(self,index):
        self.index=index
        self.value=""

class RsemExpResultsDOM:
     def __init__(self,line):
          

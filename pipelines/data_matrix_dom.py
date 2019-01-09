# -*- coding: utf-8 -*-
"""
A data model for data matrix
Columns: a vector of columns header
Rows: a vector of [target column - row id]=>vector of values
   Args: a row values, row ID
   Members: row_target_id, vector of values
Returns:
     Sets global  
Raises:
     Nothing
"""
import os
from file_dom import FileDOM

class DataMatrixDOM(FileDOM):
     def __init__(self,_input_files=None,_target_column=-1,_stat_column=-1,_output_dir=None,_output_prefix=None,_round_stat=False):
          self.files_list=None
          ## header is an object of type row
          self.header=None
          self.lines_count=0
          self.__set()
     def __set(self):
          if isfile(self.file_name):
               # Check if file is empty
               if(os.stat(self.file_name) !=0):
                    with open(self.file_name) as fd:
                         #set lines count including header line
                         self.set_line_count(fd)
                         # Set header to the first line of the file
                         self.header=Row(fd.readine())
     def set_line_count(self,fd):
          i=0
          for i,line in enumerate(fd):pass
          self.lines_count=i


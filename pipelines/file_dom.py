# -*- coding: utf-8 -*-
"""
A data model for the input file
Field: defines data model for a cell/field within a row
   Args: the index of the field
   Members: index, value
Row: defined a data model for a row within a file
   Args: a line, a field delimiter
   Members: array of fields

FileDOM: defines a data model for the file 
   Args: file_name
   Members: header , file_name

Returns:
     Sets global  
Raises:
     Nothing
"""
import os
from os.path import isfile

class Field:
    def __init__(self,_index=-1,_value=None):
        self.index=_index
        self.value=_value

class Row(Field):
     def __init__(self,_line=None,_delimit="\t"):
          self.content=[]
          self.__set(_line,_delimit)
     def __set(self,line,delimit):
          try:
               fields=line.split(delimit)
               for i, value in enumerate(fields):
                    self.content.append(Field(i,value))
          except:
               print("ERROR in line: %\s \n"%(line))

class FileDOM(Row):
     def __init__(self,_file_name):
          self.file_name=_file_name
          ## header is an object of type rowdom
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


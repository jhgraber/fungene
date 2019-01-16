# -*- coding: utf-8 -*-
"""
Data models for the row, input file,and matrix
Row: defined a data model for a row within a file
   Args: a line, a field delimiter
   Members: array of fields

FileDOM: defines a data model for the file 
   Args: file_name
   Members: header , file_name

MatrixDOM: 
Returns:
     Sets global  
Raises:
     Nothing
"""
import os
from os.path import isfile
#
# Stores the line content into an array of fields
# Split the line using the user's specified delimitter
# Default delimitter "\t"
class Row():
     def __init__(self,_line=None,_delimit="\t"):
          self.content=[]
          self.__set(_line,_delimit)
     def __set(self,line,delimit):
          try:
               self.content=line.strip().split(delimit)
               #for i, value in enumerate(fields):
               #     self.content.append(Field(i,value))
          except:
               print("ERROR in line: %s \n"%(line))
               pass 
#
# Create an object for the input file
# Object members:
#   1) file_name
#   2) Header (Row)
#   3) lines_count
#   4) file_obj (file pointer)
#
# An underscore denotes private variables in python
class FileDOM(Row):
     def __init__(self,file_name=None,delimiter="\t"):
          self._file_name=file_name
          ## header is an object of type rowdom
          self._header=None
          self._delimiter=delimiter
          self._lines_count=0
          self._file_obj=None        # file handler
          self.__set()
     def __set(self):
          if isfile(self._file_name):
               try:
                   # Check if file is empty
                   if(os.stat(self._file_name) !=0):
                       with open(self._file_name) as fd:
                           # Set this file descriptor
                           self._file_obj=fd
                           #set lines count including header line
                           self._set_line_count()
                           # Set header to the first line of the file
                           self.header=self.get_line()
               except:pass
                         
     def _set_line_count(self):
          i=0
          for i,line in enumerate(self._file_obj):pass
          self._lines_count=i
     def get_lines_count(self):return self._lines_count
     def get_file_pointer(self):return self._file_obj
     def get_file_header(self): return self._header
     def get_file_name(self):return self._file_name
     def get_line(self):
          return Row(self._file_obj.readline(),self._delimiter)

class MatrixDOM(FileDOM):
     def __init__(self,file_list=None,vIndex=0,jIndex=None,roundValue=False,delimiter="\t"):
          self._input_files=file_list          # An array of input files
          self._rowVectorColumnIndex=vIndex    # Index of the colunm that has ids 
          self._targetColumnIndex=jIndex       # Index of the column that has values
          self._round2NearestInt=roundValue    # True -> round to the nearest integer , False -> do not round (default)
          self.file_objects=[]                 # A container of file objects
          self._delimiter=delimiter

     def _set(self):
          if self._input_files is not None:
               for input_file in self._input_files: 
                    self.file_objects.append(FileDOM(input_file,self._delimiter))
     #
     # Returns a matrix of files with the associated rows count
     def get_rows_count(self):
          files={}
          for file_obj in self.file_objects:
               files[file_obj.get_file_name]=file_obj.get_lines_count()
          return files
     #
     # Returns a matrix of files with the associated colunm header fields count
     def get_header_columns_count(self):
          files={}
          for file_obj in self.file_objects:
               files[file_obj.get_file_name]=len(file_obj.get_file_header())
          return files
     #
     # Generate colunmCount, rowCount matrix
     def gen_columns_rows_count(self):
          colunms_rows={}
          for file_name,row_count in self.get_rows_count().items():
               colunms_rows[file_name]=[]
               colunms_rows[file_name].append(self.get_header_columns_count()[file_name])
               colunms_rows[file_name].append(row_count)
          return colunms_rows
     #
     # get a matrix rows_count x file_count f
     def get_matrix(self):
          #vector_matrix={}
          for i, file_obj in enumerate(self.file_objects):
               print("%d\t%s\t%d\t%d"%(i,file_obj.get_file_name(),file_obj.get_header_columns_count(),file_obj.gen_columns_rows_count())) 

          

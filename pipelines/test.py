from os.path import dirname,abspath,isfile
from file_dom import MatrixDOM

#input_files="test.matrix doc.matrix log.matrix"
input_files="*test.matrix"
file_list=input_files.split(' ')
dir_base=dirname(abspath(input_files))
print(file_list,dir_base)
for filename in file_list:
    print (filename)


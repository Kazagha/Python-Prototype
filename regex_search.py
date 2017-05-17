from collections import namedtuple
import re
import sys
import os
import glob

Match = namedtuple('Match','file_name,search_term,result')

def _load_files_in_dir(directory):
    files_in_dir = glob.glob(os.path.join(directory,'*'))

    for f in files_in_dir:
        with open(f) as file:
            yield Match(os.path.basename(f'{file}'), '', file.read())

def _search_files(files, REGEX):
    for f in files:
        search_result = REGEX.findall(f.result)
        print(REGEX.findall(f.result))
        if(len(search_result) > 0):
            yield Match(f.file_name, REGEX, search_result)

def _search_text(text):
    pass

def _write_to_csv(data ,filename):
    pass

def search_files(search_dir, regex, output=None):
    files = _load_files_in_dir(search_dir)
    #REGEX = re.compile(r'Application_Tasks.(Task_Code|Task_Description)')
    REGEX = re.compile(r'Application_Task\.Task_Description.{0,3}=.{0,2}".+?"')
    #print('Search' , REGEX.findall(r'Application_Task.Task_Description = "Test"'))

    results = _search_files(files, REGEX)

    for r in results:
        print (r)


if __name__ == '__main__':
    #in_dir, out_dir = sys.argv[1:2]
    search_dir = 'C:\\temp\\Access'
    regex = ''

    search_files(search_dir=search_dir, regex=regex)
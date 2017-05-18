from collections import namedtuple
import re
import sys
import os
import glob
import csv

Match = namedtuple('Match','file_name,search_term,result')

def _load_files_in_dir(directory):
    files_in_dir = glob.glob(os.path.join(directory,'*'))

    for f in files_in_dir:
        with open(f) as file:
            yield Match(os.path.basename(f'{file}'), '', file.read())

def _search_files(files, REGEX):
    for f in files:
        search_result = REGEX.findall(f.result)
        #print(f.result, REGEX.findall(f.result))
        if(len(search_result) > 0):
            for result in search_result:
                yield Match(f.file_name, REGEX, result)

def _search_text(text):
    pass

def _write_to_csv(data ,filename):
    with open(f'{filename}', 'w', newline='', encoding='utf8') as csvfile:
        field_names = Match._fields

        writer = csv.DictWriter(csvfile, fieldnames=field_names)

        writer.writeheader()
        for match in data:
            #print(match)
            writer.writerow({'file_name':match.file_name,'search_term':match.search_term,'result':match.result})

def search_files(search_dir, regex, output=None):
    files = _load_files_in_dir(search_dir)
    REGEX = re.compile(r'Application_Tasks.(Task_Description|Task_Code).{0,3}(=|Like).{0,3}".+?"')

    results = _search_files(files, REGEX)

    #for r in results:
    #    print (r)

    _write_to_csv(results, output)


if __name__ == '__main__':
    #in_dir, out_dir = sys.argv[1:2]
    search_dir = 'C:\\temp\\Access'
    regex = ''

    search_files(search_dir=search_dir, regex=regex, output=r'C:\temp\outfile.csv')

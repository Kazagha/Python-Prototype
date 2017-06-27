from collections import namedtuple
import re
import sys
import os
import glob
import csv
from os.path import basename


Match = namedtuple('Match','file_name,search_term,result')

def _load_files_in_dir(directory):
    files_in_dir = glob.glob(os.path.join(directory,'*'))

    for f in files_in_dir:
        with open(f) as file:
            yield Match(basename(file.name), '', file.read())

def _load_csv_file(csv_file_path):
    with open(f'{csv_file_path}', 'r', newline='', encoding='utf8') as f:

        reader = csv.DictReader(f, delimiter='|')
        for row in reader:
            #print(row['ReportName'] + ' - ' + row['DataSetName'])
            #print(row['DataSetName'])
            #print(row['CommandText'])
            #yield Match()
            yield Match(row['ReportName'] + ' - ' + row['DataSetName'], '', row['CommandText'])

def _search_files(files, REGEX):
    for f in files:
        search_result = REGEX.finditer(f.result)

        for result in search_result:
            yield Match(f.file_name, REGEX, result.group(0))

def _search_text(rows, REGEX):

    for row in rows:
        search_result = REGEX.finditer(row.result)

        for result in search_result:
            yield Match(row.file_name, REGEX, result.group(0))

def _write_to_csv(data ,filename):
    with open(f'{filename}', 'w', newline='', encoding='utf8') as csvfile:
        field_names = Match._fields

        writer = csv.DictWriter(csvfile, fieldnames=field_names)

        writer.writeheader()
        for match in data:
            writer.writerow({'file_name':match.file_name,'search_term':match.search_term,'result':match.result})

def search_files(search_dir, regex, output=None):
    files = _load_files_in_dir(search_dir)

    pattern = r'(Application_Tasks.(Task_Code|Task_Description).{0,3}(=|Like|LIKE).{0,3}".+?")'
    REGEX = re.compile(pattern=pattern)

    results = _search_files(files, REGEX)

    _write_to_csv(results, output)

def search_csv(csv_file_path, regex, output=None):
    rows = _load_csv_file(csv_file_path)

    pattern = r'((Task_Code|Task_Description).{0,3}(=|Like|LIKE|IN \(|in \().{0,3}\'.+?\')'
    REGEX = re.compile(pattern=pattern)

    results = _search_text(rows, REGEX)

    _write_to_csv(results, output)

if __name__ == '__main__':
    #in_dir, out_dir = sys.argv[1:2]
    search_dir = 'C:\\temp\\Access'
    csv_file_path = 'C:\Temp\CSV\SSRS_Query_Text_CSV.csv'
    out_file = 'C:\Temp\CSV\SSRS_out.csv'
    regex = ''

    search_csv(csv_file_path=csv_file_path,
               regex=regex, output=out_file)
    #search_files(search_dir=search_dir, regex=regex, output=r'C:\temp\outfile.csv')

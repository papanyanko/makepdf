from pathlib import Path
import fitz
import csv

def setToC(resource, dist_file):
  toc_file_path = Path(resource, 'toc.tsv')
  if not toc_file_path.is_file():
    print('toc.tsv does not exist')
    return  
  pdf = fitz.open(dist_file)
  pdf.set_toc(makeToc(toc_file_path))
  pdf.saveIncr()
  print(f'set toc')

def makeToc(toc_file_path):
  toc = []
  with open(toc_file_path, 'r', encoding='utf-8') as text:
    for row in csv.reader(text, delimiter='\t', lineterminator='\n'):
      toc.append(makeTocItem(row))
  return toc

def makeTocItem(row):
  page = int(row.pop())
  name = row.pop()
  level = len(row) + 1
  return [level, name, page]

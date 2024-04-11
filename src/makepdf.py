from pathlib import Path
import sys
import img2pdf
from PIL import Image
import fitz
import csv

def main(path):
  dist_dir = Path.cwd() / 'dist'
  if not dist_dir.is_dir():
    Path.mkdir(dist_dir, mode=711)

  global pdf_file_path
  pdf_file_path = getPdfFilePath(path, dist_dir)

  if pdf_file_path.is_file():
    print(f'{pdf_file_path} already exists')
  else:
    convertImagesToPdf(path)
    setTableOfContents(path)

def getPdfFilePath(path, dist_dir):
  pdf_file_name = Path(path.name + '.pdf')
  return dist_dir / pdf_file_name

def convertImagesToPdf(path):
  img_list = [
    img_file_path
    for img_file_path in path.iterdir()
    if img_file_path.suffix.lower() == '.png'
  ]

  if not len(img_list):
    print(f'{path} has no images')
    sys.exit(1)

  for img_path in img_list:
    preprocess(img_path)
  print('preprocessing completed')

  data = img2pdf.convert(sorted(img_list))
  pdf_file_path.write_bytes(data)
  print('made pdf')

def preprocess(img_path):
  img = Image.open(img_path)
  if img.mode == 'RGBA':
    img = img.convert('RGB')
    img.save(img_path, 'PNG')

def setTableOfContents(path):
  toc_file_path = path / 'toc.tsv'
  if not toc_file_path.is_file():
    print('toc.tsv does not exist')
    return  
  pdf = fitz.open(pdf_file_path)
  pdf.set_toc(makeToc(toc_file_path))
  pdf.saveIncr()
  print(f'set toc to {pdf_file_path}')

def makeToc(toc_file_path):
  toc = []
  text = toc_file_path.read_text(encoding='utf-8')
  for row in csv.reader(text, delimiter='\t'):
    toc.append(makeTocItem(row))
  return toc

def makeTocItem(row):
  page = int(row.pop())
  name = row.pop()
  level = len(row) + 1
  return [level, name, page]

def resolvePathArg():
  if len(sys.argv) <= 1:
    print('please set resource directory path argument')
    exit(1)
  path_arg = Path(sys.argv[1])
  if path_arg.is_absolute():
    relative_path = path_arg.relative_to(Path.cwd())
  else:
    relative_path = path_arg
  return (Path.cwd() / relative_path).resolve()

if __name__ ==  '__main__':
  main(resolvePathArg())
  
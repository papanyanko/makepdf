import img2pdf
from PIL import Image
import sys


def convert(resource, dist_file):
  img_list = [
    img_file_path
    for img_file_path in resource.iterdir()
    if img_file_path.suffix.lower() == '.png'
  ]

  if not len(img_list):
    print(f'{resource} has no images')
    sys.exit(1)

  print('processing...')
  for img_path in img_list:
    preprocess(img_path)
  print('preprocessing completed')

  data = img2pdf.convert(sorted(img_list))
  dist_file.write_bytes(data)
  print('made pdf')

def preprocess(img_path):
  img = Image.open(img_path)
  if img.mode == 'RGBA':
    img = img.convert('RGB')
    img.save(img_path, 'PNG')

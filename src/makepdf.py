from pathlib import Path
import os
import glob
import image
import toc
import sys

def main(base_path):
  resource_path = Path(base_path, 'resource')
  dist_path = Path(base_path, 'dist')

  for target_name in getTargets(resource_path, dist_path):
    print(target_name)
    resource_target_path = Path(resource_path, target_name)
    dist_target_filepath = Path(dist_path, target_name + '.pdf')
    image.convert(resource_target_path, dist_target_filepath)
    toc.setToC(resource_target_path, dist_target_filepath)
    print(f'file created: {dist_target_filepath}')

def getTargets(resource_path, dist_path):
  tmp_target_names = [os.path.basename(path) for path in resource_path.iterdir() if path.is_dir()]
  target_names = []
  for target_name in tmp_target_names:
    if glob.glob(os.path.join(dist_path, target_name + '.pdf')):
      print(f'{target_name}.pdf already exists')
    else:
      target_names.append(target_name)
  return target_names

if __name__ ==  '__main__':
  main(Path(sys.argv[1]))
  
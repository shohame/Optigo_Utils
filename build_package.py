
import os
from pathlib import Path
import shutil

cmd_str = 'python setup.py build --build-base ../outputs egg_info --egg-base ../outputs bdist_wheel --universal --dist-dir ../outputs'
#os.chdir('OptigoUtils')
os.system(cmd_str)


src_path = Path(r'../outputs')

src_file_path = list(src_path.glob('OptigoUtils*.whl'))[0]

dest_path = Path(r'N:/Optigoprj/pip')

dest_file_path = dest_path / src_file_path.name

if dest_file_path.exists():
    ans = input(f'\n\n{src_file_path.name} already exists on pip folder. Do you what to rewrite it (y/n)? - ')
    if ans=='y' or ans =='Y':
        os.remove(dest_file_path)
        shutil.move(src_file_path,dest_file_path)
else:
    shutil.move(src_file_path,dest_file_path)
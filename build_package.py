
import os
from pathlib import Path
import shutil

out_path_str = '../outputs'
optigo_pip_path = 'N:/Optigoprj/pip'
package_name = 'OptigoUtils'

out_path = Path(out_path_str)
if out_path.exists():
    shutil.rmtree(out_path, ignore_errors=True)

cmd_str = f'python setup.py build --build-base {out_path_str} ' + \
          f'egg_info --egg-base {out_path_str} ' + \
          f'bdist_wheel --universal --dist-dir {out_path_str}'
os.system(cmd_str)

src_path = out_path

src_file_path = list(src_path.glob(f'{package_name}*.whl'))[0]

dest_path = Path(optigo_pip_path)

dest_file_path = dest_path / src_file_path.name

if dest_file_path.exists():
    ans = input(f'\n\n{src_file_path.name} already exists on pip folder. Do you what to rewrite it (y/n)? - ')
    if ans=='y' or ans =='Y':
        os.remove(dest_file_path)
        shutil.move(src_file_path,dest_file_path)
else:
    shutil.move(src_file_path,dest_file_path)
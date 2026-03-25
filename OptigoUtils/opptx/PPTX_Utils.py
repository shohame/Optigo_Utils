import os
import shutil
from pathlib import Path
import time
import uuid
import zipfile
from xml.dom.minidom import parse


def create_new_temp_directory_and_remove_old_dirs() -> Path:

    my_path = Path(os.path.dirname(os.path.abspath(__file__)))
    temp_path = my_path / '_temp_'
    temp_path.mkdir(exist_ok=True)

    # remove old files and directories
    list_of_path = list(temp_path.glob('*'))
    now = time.time()
    for path in list_of_path:
        if path.is_dir():
            list_of_files = list(path.rglob('*'))
            if len(list_of_files) == 0:
                file_old = -1
            else:
                latest_file = max(list_of_files, key=os.path.getmtime)
                file_old = now - os.path.getmtime(latest_file)
            if file_old > (60 * 60) or file_old < 0:
                shutil.rmtree(path, ignore_errors=True)
        else:
            os.remove(path)

    new_dir_name = str(uuid.uuid4())
    new_path = temp_path / new_dir_name
    new_path.mkdir(exist_ok=True)

    return new_path


def delete_path(path: Path):
    shutil.rmtree(path, ignore_errors=True)


def unzip_file(file_path: Path):
    with zipfile.ZipFile(file_path, 'r') as h_zip:
        h_zip.extractall(file_path.parent)
    os.remove(file_path)

def zip_folder(path: Path, zip_filepath: Path):
    with zipfile.ZipFile(zip_filepath, 'w') as h_zip:
        for file in path.rglob('*'):
            if file.is_file():
                h_zip.write(file, file.relative_to(path))


def update_action_to_program(path: Path):

    slides_path = path / 'ppt' / 'slides'
    xml_slides_files = list(slides_path.glob('*.xml'))

    for xml_silies_file in xml_slides_files:
        dom = parse(xml_silies_file.as_posix())
        rels_fn = xml_silies_file.parent / '_rels' / (xml_silies_file.name + '.rels')
        rels_dom = parse(rels_fn.as_posix())

        hlinkClick_list = dom.getElementsByTagName("a:hlinkClick")

        rs_list = rels_dom.getElementsByTagName('Relationship')
        rs_dict = dict()
        for rs in rs_list:
            key = rs.getAttribute('Id')
            target = rs.getAttribute('Target')
            rs_dict[key] = target

        for hlinkClick in hlinkClick_list:

            r_id = hlinkClick.getAttribute('r:id')

            target = rs_dict[r_id]

            if target.count('.exe') > 0:

                hlinkClick.setAttribute('action', "ppaction://program")

        with open(xml_silies_file.as_posix(), 'w') as f_id:
            dom.writexml(f_id)



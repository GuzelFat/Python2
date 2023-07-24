import csv
import json
import pickle
from os import walk
from os.path import getsize, join


def folders_info(path: str) -> None:
    result = []

    for dir_path, dir_name, file_name in walk(path):
        for folder in dir_name:
            folder_size = 0
            for f_path, folders, files in walk(f'{dir_path}\\{folder}'):
                for f in files:
                    fp = join(f_path, f)
                    folder_size += getsize(fp)
            result.append({'dir': dir_path, 'name': folder, 'type': 'folder', 'size': folder_size})

        for file in file_name:
            result.append({'dir': dir_path, 'name': file, 'type': 'file', 'size': getsize(f'{dir_path}\\{file}')})

    with (open('folder_info.json', 'w', encoding='utf-8') as f_json,
          open('folder_info.csv', 'w', encoding='utf-8') as f_csv,
          open('folder_info.pickle', 'wb') as file_pickle
          ):
        json.dump(result, f_json, ensure_ascii=False, indent=2)

        csv_writer = csv.DictWriter(f_csv, dialect='excel',
                                    fieldnames=('dir', 'name', 'type', 'size'),
                                    lineterminator='\n')
        csv_writer.writeheader()
        csv_writer.writerows(result)

        pickle.dump(result, file_pickle)
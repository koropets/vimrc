#!/usr/bin/env python

import zipfile
import shutil
import tempfile
import requests

from os import path

github_zip = '%s/archive/master.zip'

source_dir = path.join(path.dirname(__file__), '..', 'bundle')

def download_extract_replace(plugin_name, zip_path, temp_dir):
    print('Updated {0}'.format(plugin_name))

    temp_zip_path = path.join(temp_dir, plugin_name)

    # Download and extract file in temp dir
    req = requests.get(zip_path)
    open(temp_zip_path, 'wb').write(req.content)

    zip_f = zipfile.ZipFile(temp_zip_path)
    zip_f.extractall(temp_dir)

    tmp_dir_full_name = path.join(temp_dir, '%s-master' % plugin_name)
    plugin_temp_path = path.join(temp_dir, tmp_dir_full_name)

    # Remove the current plugin and replace it with the extracted
    plugin_dest_path = path.join(source_dir, plugin_name)

    try:
        shutil.rmtree(plugin_dest_path)
    except OSError:
        pass

    shutil.move(plugin_temp_path, plugin_dest_path)


if __name__ == '__main__':
    temp_directory = tempfile.mkdtemp()

    try:
        with open(path.join(source_dir, 'plugins.txt'), 'r') as f:
            for line in f:
                name, github_url = line.rstrip().split(' ')
                zip_path = github_zip % github_url
                download_extract_replace(name, zip_path, temp_directory)
    finally:
        print (temp_directory)
        # shutil.rmtree(temp_directory)

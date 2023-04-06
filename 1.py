#!/usr/bin/python3
"""Fabfile to create a .tgz archive"""
from datetime import datetime
<<<<<<< HEAD
from fabric import Connection
=======
import os
>>>>>>> 69c782bcc8b6295666974cd8ac4f7a577eb0ad74
from fabric.api import local


def do_pack():
	folder_name = 'web_static'
	time = datetime.now().strftime('%Y%m%d%H%M%S')
	archive_path = 'versions/web_static_{}.tgz'.format(time)
<<<<<<< HEAD

	local('mkdir -p versions')
	result = local('tar -czvf {} {}'.format(archive_path, folder_name))
	if result.failed:
=======
	if not os.path.exists('versions/'):
		local('mkdir -p versions')
	result = 'tar -czvf {} web_static'.format(archive_path)
	tar_file = local(result)
	if tar_file.failed:
>>>>>>> 69c782bcc8b6295666974cd8ac4f7a577eb0ad74
		return None
	return archive_path

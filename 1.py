#!/usr/bin/python3
"""Fabfile to create a .tgz archive"""
from datetime import datetime
import os
from fabric.api import local


def do_pack():
	folder_name = 'web_static'
	time = datetime.now().strftime('%Y%m%d%H%M%S')
	archive_path = 'versions/web_static_{}.tgz'.format(time)
	if not os.path.exists('versions/'):
		local('mkdir -p versions')
	result = 'tar -czvf {} web_static'.format(archive_path)
	tar_file = local(result)
	if tar_file.failed:
		return None
	return archive_path

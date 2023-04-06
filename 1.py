#!/usr/bin/python3
"""Fabfile to create a .tgz archive"""
from datetime import datetime
from fabric import Connection
from fabric.api import local


def do_pack():
	folder_name = 'web_static'
	time = datetime.now().strftime('%Y%m%d%H%M%S')
	archive_path = 'versions/web_static_{}.tgz'.format(time)

	local('mkdir -p versions')
	result = local('tar -czvf {} {}'.format(archive_path, folder_name))
	if result.failed:
		return None
	return archive_path

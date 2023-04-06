#!/usr/bin/python3
""" Fabric script that generates a .tgz archive from the contents
of the web_static folder of your AirBnB Clone repo,
using the function do_pack. """
from datetime import datetime
import os
from fabric.api import local


def do_pack():
    """Creates archive from web_static directory"""
    time = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_path = "versions/web_static_{}.tgz".format(time)
    if not os.path.exists("versions/"):
        local("mkdir -p versions")
    result = "tar -czvf {} web_static".format(archive_path)
    tar_file = local(result)
    if tar_file.failed:
        return None
    return archive_path

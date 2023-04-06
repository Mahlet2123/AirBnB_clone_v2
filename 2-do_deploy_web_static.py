#!/usr/bin/python3
""" Fabric script (based on the file 1-pack_web_static.py)
that distributes an archive to your web servers,
using the function do_deploy """
from os.path import exists
from fabric.api import *
from fabric import Connection


env.hosts = ['54.90.3.149', '75.101.217.125']
env.user = 'ubuntu'

def do_deploy(archive_path):
    """ distributes an archive to your web servers """
    c = Connection(host=env.hosts, user=env.user)
    if not exists(archive_path):
        return False

    # Upload the archive to the
    # /tmp/ directory of the web server
    # put(local_path, remote_path)
    c.put(archive_path, "/tmp/")

    # Extract the archive to /data/web_static/releases/<archive
    # filename without extension> on the web server
    archive_filename = archive_path.split('/')[-1]
    archive_path_no_ext = "/data/web_static/releases/" + archive_filename.split('.')[0]
    c.run("mkdir -p {}".format(archive_path_no_ext))
    c.run("tar -xzf /tmp/{} -C {}/".format(archive_filename, archive_path_no_ext))
    c.run("rm /tmp/{}".format(archive_filename))

    # Delete the symbolic link /data/web_static/current from the web server
    c.run("rm -f /data/web_static/current")

    # Create a new symbolic link /data/web_static/current on the web server, linked to the new version of your code
    c.run("ln -s {} /data/web_static/current".format(archive_path_no_ext))

    print("New version deployed!")
    return True	

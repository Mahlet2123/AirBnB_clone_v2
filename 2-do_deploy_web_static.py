#!/usr/bin/python3
""" Fabric script (based on the file 1-pack_web_static.py)
that distributes an archive to your web servers,
using the function do_deploy """
from fabric.network import ssh_config
import os
from fabric.api import env, put, run


env.hosts = ["34.207.222.16", "52.207.125.221"]
env.user = "ubuntu"
env.key_filename = "/root/.ssh/id_rsa"
env.use_ssh_config = True


def do_deploy(archive_path):
    """
    distributes an archive to your web servers
    """
    if os.path.exists(archive_path) is False:
        return False
    try:
        put(archive_path, "/tmp/")
        _filename = archive_path.split("/")[-1]
        filename = _filename.split(".")[0]
        run("mkdir -p /data/web_static/releases/{}".format(filename))
        run(
            "tar -xzf /tmp/{} -C /data/web_static/releases/{}".format(
                _filename, filename
            )
        )
        run("rm /tmp/{}".format(_filename))
        run(
            "mv /data/web_static/releases/{}/web_static/* \
            /data/web_static/releases/{}/".format(
                filename, filename
            )
        )
        run("rm -rf /data/web_static/releases/{}/web_static".format(filename))
        run("rm -rf /data/web_static/current")
        run(
            "ln -s /data/web_static/releases/{}".format(filename)
            + " /data/web_static/current"
        )
        return True
    except (IOError, OSError) as e:
        return False

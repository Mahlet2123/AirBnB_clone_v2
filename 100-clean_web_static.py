#!/usr/bin/python3
""" Fabric script (based on the file 1-pack_web_static.py)
that distributes an archive to your web servers,
using the function do_deploy """
from fabric.network import ssh_config
import os
from datetime import datetime
from fabric.api import *
from fabric.api import env, put, run


env.hosts = ["54.172.89.19", "75.101.217.125"]
env.user = "ubuntu"
env.key_filename = "/root/.ssh/id_rsa"
env.use_ssh_config = True


def do_pack():
    """Creates archive from web_static directory"""
    local("mkdir -p versions")
    file = "versions/web_static_{}.tgz".format(
        datetime.strftime(datetime.now(), "%Y%m%d%I%M%S")
    )
    comp = "tar -cvzf {} web_static".format(file)
    tar_file = local(comp)
    if tar_file.failed:
        return None
    else:
        return file


def do_deploy(archive_path):
    """Deploys an archive"""
    if not os.path.exists(archive_path):
        return False
    arch = archive_path.split("/")[1]
    name = arch.split(".")[0]
    tar_file = put(archive_path, "/tmp/{}".format(arch))
    if tar_file.failed:
        return False
    tar_file = run("mkdir -p /data/web_static/releases/{}".format(name))
    if tar_file.failed:
        return False
    tar_file = run(
        "tar -xzf /tmp/{} -C /data/web_static/releases/{}/".format(arch, name)
    )
    if tar_file.failed:
        return False
    tar_file = run("rm /tmp/{}".format(arch))
    if tar_file.failed:
        return False
    comp = "mv /data/web_static/releases/{0}/web_static/*"
    comp += " /data/web_static/releases/{0}/"
    tar_file = run(comp.format(name))
    if tar_file.failed:
        return False
    tar_file = run("rm -rf /data/web_static/releases/{}/web_static".format(
        name))
    if tar_file.failed:
        return False
    tar_file = run("rm -rf /data/web_static/current")
    if tar_file.failed:
        return False
    tar_file = run(
        "ln -s /data/web_static/releases/{}/ /data/web_static/current".format(
            name)
    )
    if tar_file.failed:
        return False
    print("New version deployed!")
    return True


def deploy():
    """Fabric script (based on the file 2-do_deploy_web_static.py)
    that creates and distributes an archive to your web servers,
    using the function deploy"""
    archive = do_pack()
    if archive is None:
        return False
    tar_file = do_deploy(archive)
    return tar_file

def do_clean(number=0):
    """ deletes out-of-date archives, using the function do_clean """
    number = int(number)
    if number < 1:
        """ keep only the most recent version"""
        number = 1
    with cd("/data/web_static/releases"):
        archives = sorted(run("ls -xtr").split())
        archives_to_delete = archives[:-number]
        if len(archives_to_delete) > 0:
            for archive in archives_to_delete:
                run("rm -rf {}".format(archive))

    with cd("/data/web_static/versions"):
        archives = sorted(run("ls -xtr").split())
        archives_to_delete = archives[:-number]
        if len(archives_to_delete) > 0:
            for archive in archives_to_delete:
                run("rm -rf {}".format(archive))

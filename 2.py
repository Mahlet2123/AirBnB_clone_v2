#!/usr/bin/python3
""" Fabric script (based on the file 1-pack_web_static.py)
that distributes an archive to your web servers,
using the function do_deploy """
from fabric.network import ssh_config
from os.path import exists
from fabric.api import env, put, run


env.hosts = ["54.172.89.19", "75.101.217.125"]
env.user = "ubuntu"
env.key_filename = "/root/.ssh/id_rsa"
env.use_ssh_config = True


def do_deploy(archive_path):
    """distributes an archive to your web servers"""
    if not exists(archive_path):
        return False
    try:
        # Upload the archive to the
        # /tmp/ directory of the web server
        # put(local_path, remote_path)
        put(archive_path, "/tmp/", use_sudo=True)

        # Extract the archive to /data/web_static/releases/<archive
        # filename without extension> on the web server
        a_filename = archive_path.split("/")[-1]
        filename = a_filename.split(".")[0]
        archive_path_no_ext = "/data/web_static/releases/{}".format(filename)

        if not exists (archive_path_no_ext):
            run("sudo mkdir -p {}".format(archive_path_no_ext))
            run(
                "sudo tar -xzf /tmp/{} -C {}/".format(a_filename, archive_path_no_ext),
                shell=True,
            )
            run(
                "sudo mv /data/web_static/releases/{}/web_static/* \
                    /data/web_static/releases/{}/".format(
                    filename, filename
                )
            )
            run("sudo rm -rf /data/web_static/releases/{}/web_static".format(filename))
            run("sudo rm /tmp/{}".format(a_filename))

            # Delete the symbolic link /data/web_static/current from the web server
            run("sudo rm -f /data/web_static/current")

            # Create a new symbolic link /data/web_static/current on the web server,
            # linked to the new version of your code
            run("sudo ln -s {} /data/web_static/current".format(archive_path_no_ext))
  
            print("New version deployed!")
            return True
        return True
    except:
        return False

#!/usr/bin/python3
from fabric.api import run, put, env
import os


env.hosts = ['23.20.133.240', '18.234.214.85']
env.user = os.getenv('USER')


def do_deploy(archive_path):
    if not os.path.isfile(archive_path):
        return False

    # Upload the archive to the /tmp/ directory of the web server
    put(archive_path, "/tmp/")

    # Uncompress the archive to the folder /data/web_static/releases/<archive filename without extension> on the web server
    filename = os.path.basename(archive_path)
    directory = "/data/web_static/releases/" + filename.split(".")[0]
    run("mkdir -p {}".format(directory))
    run("tar -xzf /tmp/{} -C {} ".format(filename, directory))

    # Delete the archive from the web server
    run("rm /tmp/{}".format(filename))

    # Delete the symbolic link /data/web_static/current from the web server
    run("rm -rf /data/web_static/current")

    # Create a new the symbolic link /data/web_static/current on the web server, linked to the new version of your code (/data/web_static/releases/<archive filename without extension>)
    run("ln -s {} /data/web_static/current".format(directory))

    return True

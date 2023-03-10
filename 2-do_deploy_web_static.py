#!/usr/bin/python3
"""
Fabric script that distributes an archive to your web servers
"""
from fabric.api import *
from os.path import exists
env.user = 'ubuntu'
env.hosts = ['23.20.133.240', '18.234.214.85']


def do_deploy(archive_path):
    """Deploys the archive to the web servers"""
    if not exists(archive_path):
        return False
    archive_name = archive_path.split('/')[-1]
    remote_path = '/tmp/{}'.format(archive_name)
    # Upload the archive to the /tmp/ directory of the web server
    put(archive_path, remote_path)
    # Uncompress the archive to the folder /data/web_static/releases/<archive
    # filename without extension>
    archive_folder = '/data/web_static/releases/{}'.format(
        archive_name.split('.')[0])
    run('mkdir -p {}'.format(archive_folder))
    run('tar -xzf {} -C {}'.format(remote_path, archive_folder))
    # Delete the archive from the web server
    run('rm {}'.format(remote_path))
    # Delete the symbolic link /data/web_static/current from the web server
    run('sudo rm -rf /data/web_static/current')
    # Create a new the symbolic link /data/web_static/current on the web server
    run('sudo ln -s {} /data/web_static/current'.format(archive_folder))
    return True

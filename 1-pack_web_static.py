#!/usr/bin/python3
"""Fabric script to generate a tgz archive"""

from datetime import datetime
from fabric.api import *


def do_pack():
    """
   Generates a .tgz archive from the contents of the web_static folder
    """

    time = datetime.now()
    archive = 'web_static_' + time.strftime("%Y%m%d%H%M%S") + '.' + 'tgz'
    local('mkdir -p versions')
    create = local('tar -cvzf versions/{} web_static'.format(archive))
    if create.succeeded:
        return 'versions/{}'.format(archive)
    else:
        return None

 

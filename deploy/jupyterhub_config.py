# Configuration file for jupyterhub.

import os

# Setup some variables
network_name              = os.environ['DOCKER_NETWORK_NAME']
ff_data_dir               = os.environ['FF_DATA_DIR']
ff_image_name             = os.environ['FF_IMAGE_NAME']
ff_container_name         = os.environ['FF_CONTAINER_NAME']
hub_container_name        = os.environ['HUB_CONTAINER_NAME']

jupyterhub_config_dir     = os.path.join(ff_data_dir, 'config', 'jupyterhub')
ff_config_dir             = os.path.join(ff_data_dir, 'config', 'featurefactory')

# Spawned containers
c.JupyterHub.spawner_class          = 'dockerspawner.SystemUserSpawner'
c.SystemUserSpawner.container_image = ff_image_name
c.DockerSpawner.container_prefix    = ff_container_name
c.DockerSpawner.remove_containers   = True

# Networking
c.JupyterHub.port                 = 443
c.JupyterHub.hub_ip               = hub_container_name
c.JupyterHub.hub_port             = 8080
c.DockerSpawner.use_internal_ip   = True
c.DockerSpawner.network_name      = network_name
c.DockerSpawner.extra_host_config = {
    'network_mode': network_name,
}

# Security
c.JupyterHub.ssl_key = os.path.join(jupyterhub_config_dir, 'key.pem')
c.JupyterHub.ssl_cert = os.path.join(jupyterhub_config_dir, 'cert.pem')
# c.Authenticator.whitelist = {''}

# Data/directories
c.Spawner.notebook_dir = '~/notebooks'
c.DockerSpawner.read_only_volumes = {
    ff_config_dir                     : '/etc/featurefactory',
    os.path.join(ff_data_dir, 'data') : '/data',
}
c.SystemUserSpawner.host_homedir_format_string = os.path.join(ff_data_dir, 'users', '{username}')

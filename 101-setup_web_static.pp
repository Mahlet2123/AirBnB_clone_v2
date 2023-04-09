# puppet manifest preparing a server for static content deployment
exec {'update package list':
  command => '/usr/bin/env apt-get -y update',
} -> 
exec {'install nginx':
  command => '/usr/bin/env apt-get -y install nginx',
} -> 
exec {'create required directories':
  command => '/usr/bin/env mkdir -p /data/web_static/releases/test/ && /usr/bin/env mkdir -p /data/web_static/shared/',
} -> 
exec {'write "Hello Puppet" to index.html':
  command => '/usr/bin/env echo "Hello Puppet" | sudo tee /data/web_static/releases/test/index.html',
} -> 
file {'/data/web_static/current':
  ensure => link,
  target => '/data/web_static/releases/test/',
} -> 
exec {'add new configuration to NGINX':
  command => '/usr/bin/env sed -i "/listen 80 default_server;/a location /hbnb_static/ { alias /data/web_static/current/;}" /etc/nginx/sites-available/default',
} -> 
file { '/data/':
  owner   => 'ubuntu',
  group   => 'ubuntu',
  recurse => true
} -> 
exec {'restart nginx':
  command => '/usr/bin/env service nginx restart',
}

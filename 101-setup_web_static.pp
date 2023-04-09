#sets up your web servers for the deployment of web_static.

exec {'/usr/bin/env apt-get -y update':}
exec {'/usr/bin/env apt-get -y install nginx':}

package { 'nginx':
  ensure => installed,
}

# Create required directories if they don't already exist
exec { '/usr/bin/env sudo mkdir -p /data/web_static/releases/test/':}
exec { '/usr/bin/env sudo mkdir -p /data/web_static/shared/':}

# Create index.html file with random content
file { '/data/web_static/releases/test/index.html':
  ensure  => 'file',
  content => '<html><head></head><body>Holberton School</body></html>',
  mode    => '0755'
}

# Create a symbolic link /data/web_static/current linked to the
# /data/web_static/releases/test/ folder.
file { '/data/web_static/current':
  ensure => 'link',
  target => '/data/web_static/releases/test/',
}

# Give ownership of the /data/ folder to the ubuntu user AND group
file { '/data/':
  owner   => 'ubuntu',
  group   => 'ubuntu',
  recurse => true
}

# Update the Nginx configuration
file { '/etc/nginx/sites-available/default':
  ensure => present,
}->
file_line { 'Append a line to /etc/nginx/sites-available/default':
  path => '/etc/nginx/sites-available/default',
  line => '\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t\tautoindex off;\n\t}',
}

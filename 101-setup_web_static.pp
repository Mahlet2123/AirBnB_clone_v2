# sets up your web servers for the deployment of web_static.

package { 'nginx':
  ensure => installed,
}

# Create required directories if they don't already exist
file { '/data/web_static/shared/':
  ensure => 'directory',
  mode   => '755',
}

file { '/data/web_static/releases/test/':
  ensure => 'directory',
  mode   => '755',
}

# Create index.html file with random content
file { '/data/web_static/releases/test/index.html':
  ensure  => 'filie',
  content => '<html><head></head><body>Holberton School</body></html>',
  mode    => '755'
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

# Handle Nginx server traffic
# Increase the ULIMIT of the default file
exec { 'fix--for-nginx':
  # Modify the value of ULIMIT and specifiy the path for the sed command
  command => '/bin/sed -i "s/25/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/',
  before  => Exec['nginx-restart'],
}

# Configure Nginx settings for handling 1000 requests with 100 at a time
file { '/etc/nginx/nginx.conf':
  ensure  => file,
  content => "worker_processes 4;\nevents {\n\tworker_connects 100;\n}",
  notify  => Exec['nginx-reload'],
}

# Reload Nginx configuration
exec { 'nginx-reload':
  command     => '/etc/init.d/nginx reload',
  path        => '/etc/init.d/',
  refreshonly => true,
}

# Restart web server
exec { 'nginx-restart':
  command => '/etc/init.d/nginx restart',
  path    => '/etc/init.d/',
}

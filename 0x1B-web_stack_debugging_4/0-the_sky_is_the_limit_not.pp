# Handle Nginx server traffic
# Increase the ULIMIT of the default file
exec { 'fix--for-nginx':
  # Modify the value of ULIMIT and specifiy the path for the sed command
  command => '/bin/sed -i "s/25/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/',
}

# Restart web server
exec { 'nginx-restart':
  command => '/etc/init.d/nginx restart',
  path    => '/etc/init.d/',
}

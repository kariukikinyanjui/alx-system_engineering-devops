# Creates a manifest that killds a proecess named killmenow using Puppet
exec { 'kill':
  command  => 'pkill -f killmenow',
  path     => ['/bin', 'usr/bin'],
}

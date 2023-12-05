#!/usr/bin/env bash
# Configuration file with (w/Puppet)

file { 'etc/ssh/ssh_config':
        ensure => present,

content =>"
        #SSH client configuration
        host*
	IdentityFile ~/.ssh/school
	PasswordAuthentication no
	",
}

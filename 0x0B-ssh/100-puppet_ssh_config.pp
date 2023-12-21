#!/usr/bin/env bash
# Configuration file with (w/Puppet)

file { '/etc/ssh/ssh_config':
  ensure  => present,
  content => 'PasswordAuthentication no\nIdentityFile ~/.ssh/school',
  }

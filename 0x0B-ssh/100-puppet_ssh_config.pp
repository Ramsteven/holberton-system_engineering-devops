#pupet to ssh_config
file_line {  'Turn off passwd auth':
  #ensure check if the file is present	
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => 'PasswordAuthentication no'
}
file_line {  'Declare identity file':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => 'IdentityFile ~/ssh/holberton'
}

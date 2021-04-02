# killing process name killmenow
exec { 'killmenow':
  command  => 'pkill killmenow',
  provider => 'shell'
}

file { '/tmp':
	path => '/tmp/holberton'
	mode => 0744
	owner => www-data
	group => ww-data
	content => I love pupet
}

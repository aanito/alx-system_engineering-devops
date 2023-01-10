file {  ‘/tmp/school’ : 
	path => ‘/tmp/school’,
	ensure => ‘present’,
	content => ‘I love Puppet’,
	group => ‘www.data’,
	owner => ‘www.data’,
	permission => ‘use: 0744’,
} 


#Create a file with puppet


file { ‘school’: 
	path    => ‘/tmp/school’,
	mode    => '0744',
	owner   => 'www-data',
	group   => 'www-data',
	content => ‘I love Puppet’,
} 

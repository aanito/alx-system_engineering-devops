#Installing the flask

class { 'python':
  ez_setup => true,
}

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}  

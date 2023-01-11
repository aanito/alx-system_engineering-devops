#Installing the flask
package { 'flask':
  ensure   => '2.1.0', 'installed',
  provider => 'pip3',
}

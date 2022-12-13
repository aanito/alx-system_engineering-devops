You must be able to explain some specifics about this infrastructure:
	What is a server:
		A server is a software or hardware device that accepts and responds to requests made over a network
	What is the role of the domain name
		It serves to identify Internet resources, such as computers, networks, and services, with a text-based label that is easier to memorize than the numerical addresses used in the Internet protocols.
	What type of DNS record www is in www.foobar.com
		It is using the A record which uses the IPV4 addresses
	What is the role of the web server
		The role of the web server is  to store, process, and deliver requested information or webpages to end users.
	What is the role of the application server
		The role of the application server is to act as host (or container) for the user's business logic while facilitating access to and performance of the business application.
	What is the role of the database
		The databse stores the end-user data, which is a raw data relevant to the end user and metadata, which is the data which integrates and manages the end-user data
  
	What is the server using to communicate with the computer of the user requesting the website


You must be able to explain what the issues are with this infrastructure:
SPOF
	Downtime when maintenance needed (like deploying new code web server needs to be restarted)
	Cannot scale if too much incoming traffic

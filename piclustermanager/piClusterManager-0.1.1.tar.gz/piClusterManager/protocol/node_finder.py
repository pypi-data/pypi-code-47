import threading, time, socket

class node_finder:
	'''
	init function
	@param self
	@param config varaible with config
	@return None
	'''
	def __init__(self, config):
		self.config = config
		
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)

        # Enable port reusage so we will be able to run multiple clients and servers on single (host, port). 
        # Do not use socket.SO_REUSEADDR except you using linux(kernel<3.9): goto https://stackoverflow.com/questions/14388706/how-do-so-reuseaddr-and-so-reuseport-differ for more information.
        # For linux hosts all sockets that want to share the same address and port combination must belong to processes that share the same effective user ID!
        # So, on linux(kernel>=3.9) you have to run multiple servers and clients under one user to share the same (host, port).
        # Thanks to @stevenreddie
		self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)

        # Enable broadcasting mode
		self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

		self.sock.bind(("", config.finder_port))
		
		# create listener as new theard
		self.listener = threading.Thread(target=self.listener_hello)
		# set theard as deamon
		self.listener.daemon = True
		# start theard
		self.listener.start()
		
		# empty list for finded nodes
		self.nodes = []

	'''
	send find broarcast
	@param self
	@param retry number of sended packets
	@return None
	'''
	def find_nodes(self, retry = 1):
		for trying in range(retry):
			self.sock.sendto(self.config.find_packet, ('<broadcast>', self.config.broadcast_port))
			# wait 1s to send next
			time.sleep(1)
			
	'''
	add new node to list
	@param self
	@param ip of node
	@return None
	'''
	def add_node(self, ip):
		if ip not in self.nodes:
			self.nodes.append(ip)

	'''
	listener for hello packets
	@param self
	@return None
	'''	
	def listener_hello(self):
		print("theard")
		while True:
			data, addr = self.sock.recvfrom(1024)
			if data == self.config.hello_packet:
				self.add_node(addr[0])

import threading, socket

class agent:
	'''
	init function
	@param self
	@param config varaible with config
	@return None
	'''
	def __init__(self, config):
		self.config = config
		
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		# Enable port reusage so we will be able to run multiple clients and servers on single (host, port). 
        # Do not use socket.SO_REUSEADDR except you using linux(kernel<3.9): goto https://stackoverflow.com/questions/14388706/how-do-so-reuseaddr-and-so-reuseport-differ for more information.
        # For linux hosts all sockets that want to share the same address and port combination must belong to processes that share the same effective user ID!
        # So, on linux(kernel>=3.9) you have to run multiple servers and clients under one user to share the same (host, port).
        # Thanks to @stevenreddie
		self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)

        # Enable broadcasting mode
		self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

		self.sock.bind(("", self.config.broadcast_port))
		
		# create listener as new theard
		self.broadcast_listener = threading.Thread(target=self.broadcast_listener)
		# start theard
		self.broadcast_listener.start()

	'''
	send hello packet to target or broadcast
	@param self
	@param addr address of target or None for broadcast
	@return None
	'''	
	def send_hello(self, addr = None):
		if addr == None:
			addr = ('<broadcast>', self.config.finder_port)
			
		self.sock.sendto(self.config.hello_packet, addr)
	
	'''
	listener for find packets
	@param self
	@return None
	'''	
	def broadcast_listener(self):
		while True:
			data, addr = self.sock.recvfrom(1024)
			if data == self.config.find_packet:
				print("[INFO] find packet from " + str(addr))
				self.send_hello(addr)

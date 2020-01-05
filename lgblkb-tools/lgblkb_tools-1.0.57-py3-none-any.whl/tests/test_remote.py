from contextlib import contextmanager

import diskcache
from fabric.runners import Result
from typing import Union

from lgblkb_tools.common.proxies import RecursiveProxy
from invoke import Responder

from lgblkb_tools import logger,Folder
from fabric import Connection

cache=diskcache.Cache(Folder('lgblkb_cache').path)

# noinspection PyAbstractClass
class RemoteConnection(RecursiveProxy):
	
	def _proxy_setup(self,*args,**kwargs):
		self.res: Result=None
		self.hide=False
		self.backup_tag='_lgblkb_backup'
	
	@classmethod
	def using(cls,host,user=None,port=None,config=None,gateway=None,forward_agent=None,
	          connect_timeout=None,connect_kwargs=None,inline_ssh_env=None,):
		return cls(_get_remcon(host,user=user,port=port,config=config,gateway=gateway,forward_agent=forward_agent,
		                       connect_timeout=connect_timeout,connect_kwargs=connect_kwargs,inline_ssh_env=inline_ssh_env,))
	
	@logger.trace()
	def apt_install(self,command,**kwargs):
		return self.run('sudo apt-get install -y --no-install-recommends '+command,**kwargs)
	
	def run(self,command,**kwargs):
		res: Result=self.__wrapped__.run(command,**dict(dict(warn=True,hide=self.hide),**kwargs))
		if res.failed: raise RuntimeError(res.stderr)
		self.res=res
		return self
	
	def _backup(self,filepath,**kwargs):
		try:
			return self.run(f'cp {filepath} {filepath}_lgblkb_backup',**dict(dict(hide=True),**kwargs))
		except RuntimeError as exc:
			if exc.args[0].rstrip().endswith('Permission denied'):
				return self.run(f'sudo cp {filepath} {filepath}_lgblkb_backup',**kwargs)
			else:
				raise exc
	
	@logger.trace()
	def backup(self,filepath,**kwargs):
		if self.exists_file(filepath+self.backup_tag):
			logger.debug('Backup file already exists. Skipping.')
			return
		else:
			return self._backup(filepath,**kwargs)
	
	def exists_file(self,filepath):
		return bool(int(self.run(f'test -f {filepath} && echo 1 || echo 0',hide=True).res.stdout.strip()))
	
	def exists_folder(self,folderpath):
		return bool(int(self.run(f'test -d {folderpath} && echo 1 || echo 0',hide=True).res.stdout.strip()))
	
	def _cat(self,filepath,file_contents,append):
		file_contents=file_contents.replace('"','""')
		return self.run(f"""sudo bash -c "cat <<EOF {'>>' if append else '>'} {filepath}\n{file_contents}\nEOF" """)
	
	@logger.trace(skimpy=True)
	def create_file(self,filepath,file_contents):
		# file_contents=file_contents.replace('"','""')
		# return self.run(f'sudo bash -c "cat <<EOF > {filepath}\n{file_contents}\nEOF"')
		return self._cat(filepath,file_contents,False)
	
	@logger.trace(skimpy=True)
	def append_to_file(self,filepath,file_contents):
		# file_contents=file_contents.replace('"','""')
		# return self.run(f'sudo bash -c "cat <<EOF >> {filepath}\n{file_contents}\nEOF"')
		return self._cat(filepath,file_contents,True)
	
	@logger.trace(skimpy=True)
	def replace(self,filepath,old,new,delim='/'):
		return self.run(f"""sudo sed -i 's{delim}{old}{delim}{new}{delim}' {filepath}""")

# region RemoteConnection typing fixtures:
RemConn=Union[RemoteConnection,Connection]

def _get_remcon(*args,**kwargs) -> RemConn:
	return Connection(*args,**kwargs)

# endregion


def main():
	conn=RemoteConnection.using(host='10.1.142.180',user='pi')
	conn.hide=False
	# conn.apt_install('dnsmasq')
	# conn.backup('/etc/network/interfaces')
	# 	conn.append_to_file("/etc/network/interfaces",f"""
	# # interfaces(5) file used by ifup(8) and ifdown(8)
	#
	# # Please note that this file is written to be used with dhcpcd
	# # For static IP, consult /etc/dhcpcd.conf and 'man dhcpcd.conf'
	#
	# # Include files from /etc/network/interfaces.d:
	# source-directory /etc/network/interfaces.d
	# allow-hotplug eth0
	# iface eth0 inet static
	#     address 192.168.2.1
	#     netmask 255.255.255.0
	#     network 192.168.2.0
	#     broadcast 192.168.2.255
	# """)
	# 	conn.backup('/etc/dnsmasq.conf')
	# 	conn.create_file('/etc/dnsmasq.conf',"""interface=eth0      # Use interface eth0
	# listen-address=192.168.2.1 # listen on
	# # Bind to the interface to make sure we aren't sending things
	# # elsewhere
	# bind-interfaces
	# server=8.8.8.8       # Forward DNS requests to Google DNS
	# domain-needed        # Don't forward short names
	# # Never forward addresses in the non-routed address spaces.
	# bogus-priv
	# # Assign IP addresses between 192.168.2.2 and 192.168.2.100 with a
	# # 12 hour lease time
	# dhcp-range=192.168.2.2,192.168.2.100,12h""")
	# conn.replace('/etc/sysctl.conf','#net.ipv4.ip_forward=1','net.ipv4.ip_forward=1')
# 	conn.run(f"""
# sudo iptables -t nat -A POSTROUTING -o wlan0 -j MASQUERADE
# sudo iptables -A FORWARD -i wlan0 -o eth0 -m state --state RELATED,ESTABLISHED -j ACCEPT
# sudo iptables -A FORWARD -i eth0 -o wlan0 -j ACCEPT
# """)
# 	conn.run(f"""
# sudo sh -c "iptables-save > /etc/iptables.ipv4.nat"
# """)
# 	conn.backup('/etc/rc.local')
# 	conn.replace('/etc/rc.local','exit 0','iptables-restore < /etc/iptables.ipv4.nat','#').append_to_file('/etc/rc.local','exit 0')
	
	
	pass

if __name__=='__main__':
	main()

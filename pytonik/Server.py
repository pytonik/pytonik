from pytonik.cmd import server


class Server():

	@staticmethod
	def serve(host, path, port, server_pro="HTTP/1.1"):
		server.serv(host, path, port, server_pro)

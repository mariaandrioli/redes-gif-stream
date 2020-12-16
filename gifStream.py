# coding=utf-8
#!/usr/bin/python
import socket, time, sys, logging
import client, server, giphy

PORT = 5050 # porta de comunicação
ADDRESS = ('255.255.255.255', PORT) # endereço (ip broadcast, porta)

def main(argv):
	logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO, datefmt='%d-%b-%y %H:%M:%S')

	SOCK = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #cria socket 
	logging.info("Socket criado")
	SOCK.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1) # habilita operacao de mandar para broadcast
	logging.info("Broadcast setado")

	if argv[0] == "servidor": # caso seja servidor
		logging.info("Sou um servidor, ip: %s", socket.gethostname())
		server.server(ADDRESS, SOCK, float(argv[1])) 
	elif argv[0] == "cliente": # caso seja cliente
		logging.info("Sou um cliente, ip: %s", socket.gethostname())
		SOCK.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # permite reutilizar endereços
		SOCK.bind(("", PORT)) # conecta ao endereço
		client.client(ADDRESS, SOCK)

if __name__ == '__main__':
	try:
		sys.argv[1]
		if (sys.argv[1] != "servidor" and sys.argv[1] != "cliente"): # Se na linha de comando nao tiver nem cliente nem servidor
			print("Execução: python gifStream.py <servidor/cliente> <tempo (em segundos)>")
			sys.exit()
	except IndexError:
		print("Execução: python gifStream.py <servidor/cliente> <tempo (em segundos)>")
		sys.exit()
	try:
		# Verifica se o tempo é valido
		if (sys.argv[1] == "servidor"):	
			try:
				sys.argv[2]
			except IndexError:
				print("Argumento inválido, o tempo é obrigatorio no caso do servidor")
				sys.exit()
			float(sys.argv[2])
	except ValueError: # tempo não é numero
		print("Argumento inválido, o tempo deve ser um número")
		sys.exit()

	print ("===================================================================")
	print ("Redes de Computadores II - Turma 2019/1 - Prof. Elias P. Duarte Jr.")
	print ("Maria Teresa Kravetz Andrioli - GRR20171602 - mtka17")
	print ("Ana Carolina Faria Magnoni - GRR20166808 - acfm16")
	print ("===================================================================\n")
	main(sys.argv[1:])
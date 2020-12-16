# coding=utf-8
from socket import socket
from collections import namedtuple
import time, giphy, json, sys, logging

def server(address, sock, interval):
	beforeTime = 0 # tempo inicial
	seq = 0 # variavel que controla sequencia
	package = namedtuple('package', 'seq data type') # padroniza pacote

	while True:
		try:
			nowTime = time.clock() # tempo agora
			if (nowTime-beforeTime >= interval): # caso o intervalo de tempo definido tenha passado
				url, gifType = giphy.gifUrl() # obtem url e tipo de gif
				msg = package(seq, url, gifType) # cria pacote

				beforeTime = time.clock() # novo tempo anterior

				logging.info("Mandando nova mensagem")

				sock.sendto(json.dumps(msg), address) # manda pacote
				seq += 1 # atualiza sequencia
		except KeyboardInterrupt:
			logging.info("Houve interrupção do teclado, vou finalizar")

			print("\nDesconectando servidor, fechando socket, desconectando clientes...")
			
			sock.sendto("fim", address)
			sock.close()
			sys.exit(0)

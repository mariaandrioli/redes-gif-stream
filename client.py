# coding=utf-8
from socket import socket
import json, webbrowser, giphy, sys, logging

def handleException(outOfOrder, seq, packets, stickers): # lida a exception
	lost = 0 # pacotes perdidos
	logging.info("Quantidade de pacotes fora de ordem: %d", outOfOrder)

	for i in range(seq):
		if i not in packets:
			lost += 1

	logging.info("Quantidade de pacotes perdidos: %d", lost)
	logging.info("Quantidade de Stickers: %d", len(stickers))
	logging.info("Porcentagem de stickers em relação ao total: " + "{:.2%}".format(float(len(stickers))/float((seq-lost+1))))
	logging.info("Stickers: \n%s", stickers)
	print("\nDesconectando cliente...") # mostra logs?
	sys.exit(1)

def client(adress, sock):
	seq = -1 # para comparar com a sequencia que vai vir no socket
	outOfOrder = 0 # qtd de pacotes fora de ordem
	stickers = []  # lista de gifs que sao stickers
	packets = {} # dicionario para controlar pacotes perdidos

	while True:
		try:
			data, addr = sock.recvfrom(128)

			logging.info("Recebi data: %s do servidor", data)

			if (data == "fim"): # caso o servidor tenha se desligado
				logging.info("Recebi interrupcão do servidor, vou finalizar conexão")
				handleException(outOfOrder, seq, packets, stickers)

			if json.loads(data)[0] != seq+1 and seq != -1: # se nao estiver na order certa ou se nao for o primeiro (sequencia == 0)
				outOfOrder+= (json.loads(data)[0]-seq+1)

			seq = json.loads(data)[0] # atualiza seq
			packets[seq] = 1 # marca pacote com numero de sequencia seq como recebido

			if json.loads(data)[1] == '': # se a url vier vazia (por causa da api do giphy)
				logging.info("Url vazia")
			else:
				if json.loads(data)[2] == 'sticker': # se for sticker, para contabiliza-los
					stickers.append(json.loads(data)[1].encode())
				# print(packets)
				# webbrowser.open(json.loads(data)[1], 1)				
		except KeyboardInterrupt:
			handleException(outOfOrder, seq, packets, stickers)
	return
import socket
import time
import hashlib
import struct
import os
import thread

MAX_KEY_SIZE = 255

def abre_arquivo(nome):
	arquivo  = open('arquivos/'+nome, "rb")
	arquivo.seek(0)
	alfabeto = arquivo.read()
	return alfabeto

def gravar_arquivo(nome, conteudo):    
    #inicio = int(tam_parte) * (int(parte)-1)
    arquivo = open('arquivos/'+nome, 'ab+')
    arquivo.truncate() # limpa arquivo, para caso de salvar arquivo ja existente
    arquivo.seek(0)
    arquivo.write(conteudo)
    arquivo.close()

def criptografia(textoInicial, chave):
    cifra = ''
    for x in textoInicial:
        ord_c = (ord(x) + chave) % 256
        cifra += chr(ord_c)
    return cifra
	
'''def descriptografia(texto_cesar, chave):
	#texto_list = list(texto_cesar)
	texto = ''
	for x in texto_cesar:
		ord_c = (ord(x) + (chave*(-1)))%256
        texto += chr(ord_c)
	return texto'''

def inverte_sinal(chave):
	ch_= chave *-1
	return ch_
	
def getKey():
    key = 0
    while True:
        print('Enter the key number (1-%s)' %(MAX_KEY_SIZE))
        key = int(input())
        if (key >= 0 and key <= MAX_KEY_SIZE):
            return key

'''import pdb
pdb.set_trace()'''
chave = getKey()
textoInicial = abre_arquivo('textoinicial.txt')
cifrado = criptografia(textoInicial, chave)
gravar_arquivo('criptografado.txt', cifrado)


texto_cesar = abre_arquivo('criptografado.txt')
descriptografado = criptografia(texto_cesar, inverte_sinal(chave))
gravar_arquivo('descriptografado.txt', descriptografado)

print(textoInicial)
print(cifrado)
print(descriptografado)
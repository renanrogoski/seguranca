import socket
import time
import hashlib
import struct
import os
import thread

def abre_arquivo(nome):  
    arquivo  = open('arquivos3/'+nome, "rb")
    alfabeto = arquivo.read()    
    return alfabeto

def gravar_arquivo(nome, conteudo):    
    #inicio = int(tam_parte) * (int(parte)-1)
    arquivo = open('arquivos3/'+nome, 'ab+')
    arquivo.truncate() # limpa arquivo, para caso de salvar arquivo ja existente
    arquivo.seek(0)
    arquivo.write(conteudo)
    arquivo.close()

def cria_chave(chave, texto):
	
	if len(chave) < len(texto):
		#novaChave = chave * (len(texto)/len(chave))%
		mult = len(texto)/len(chave)
		modi = len(texto)%len(chave)
		lista = list()
		for i in range(0, mult):
			lista.append(chave)
		lista.append(chave[:modi])
		novaChave = ''.join(lista)
		return novaChave
	return chave
	
def criptografia_vigenere(chave, texto):
	ord_texto=[]
	ord_chave=[]
	ch_=[]
	for t in texto:
		ord_texto.append(ord(t))
	for c in chave:
		ord_chave.append(ord(c))
	#print(ord_texto)
	#print(ord_chave)
	i=0
	j = len(texto)
	while i < j:
		ch_.append(chr((ord_texto[i] + ord_chave[i])%256))
		i += 1
	cifra = ''.join(ch_)
	return cifra

def inverte_sinal(chave):
	ch_=[]
	for x in chave:
		ch_.append(chr((ord(x)*-1)%256))
	chave = ''.join(ch_)
	return chave

'''chave = abre_arquivo('chavevigenere.txt')
texto = abre_arquivo('textoinicial.txt')
chaveCompl = cria_chave(chave, texto)
crypt = criptografia_vigenere(chaveCompl, texto)
gravar_arquivo('criptografado.txt', crypt)

decrypt = criptografia_vigenere(inverte_sinal(chaveCompl), crypt)
gravar_arquivo('descriptografado.txt', decrypt)
print(texto)
print(chaveCompl)

print(crypt)
print(decrypt)'''
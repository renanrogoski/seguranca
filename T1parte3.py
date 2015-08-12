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

'''def cria_chave(chave, texto):
	
	if len(chave) < len(texto):
		novaChave = chave * (len(texto)/len(chave))
		if len(novaChave):
			return novaChave
	return chave'''



'''def cria_chave(chave, texto):
	
	if len(chave) < len(texto):
		novaChave = chave * (len(texto)/len(chave))
		if len(novaChave) < len(texto):
			i= (len(texto)-len(novaChave))
			for i in novaChave:
				novaChave[i] = 
				return novaChave
				
			 
			
			return novaChave
		if len(novaChave):
			return novaChave
	return chave'''

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
	print(ord_texto)
	print(ord_chave)
	i=0
	j = len(texto)
	while i < j:
		ch_.append(chr(ord_texto[i] + ord_chave[i]))
		i += 1
	cifra = ''.join(ch_)
	return cifra
	
chave = abre_arquivo('chavevigenere.txt')
texto = abre_arquivo('textoinicial.txt')
chaveCompl = cria_chave(chave, texto)
print(texto)
print(chaveCompl)

crypt = criptografia_vigenere(chaveCompl, texto)
print(crypt)
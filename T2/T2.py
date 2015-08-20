import socket
import time
import hashlib
import struct
import os
import thread
import T1cesar
import T1vigenere

def abre_arquivo_in(nome):
	arquivo  = open('arquivos/inputs/'+nome, "rb")
	arquivo.seek(0)
	alfabeto = arquivo.read()
	return alfabeto

def abre_arquivo_out(nome):
	arquivo  = open('arquivos/outputs/'+nome, "rb")
	arquivo.seek(0)
	alfabeto = arquivo.read()
	return alfabeto

def descobre_cesar(textoinicial, textocripto):
	vlrini = ord(textoinicial[0])
	vlrcry = ord(textocripto[0])
	chave = (vlrcry - vlrini)%256
 
	cesar = T1cesar.criptografia(textoinicial,chave)

	if((vlrcry - chave) == vlrini):
		print "pode ser cesar"

	'''tam = len(textoinicial)
	j=0
	for r in textoinicial:
		if ( (ord(textocripto[j]) - chave)  != ord(textoinicial[j])):
			print "diferente"
			return 0
		j += 1

	if (j >= tam ):
		print "sim eh cesar"
		return 1'''	

	if(cesar == textocripto):
		print("cesar")
		
		return chave
	else:
		return 0

def descobre_vigenere(textoinicial, textocripto):
	chave_compl = descobre_chave_completa(textoinicial, textocripto)

	chave = ''
	i=0
	for x in chave_compl:
		
		ord_c = ord(chave_compl[i])
		chave += chr(ord_c)
		chave_completa = T1vigenere.cria_chave(chave , textoinicial)
		if(chave_compl == chave_completa):
			print "vigenere"
			return chave
		i += 1
	return chave_completa

def descobre_chave_completa(textoinicial, textocripto):
	chave_com = ''
	i = 0
	for x in textoinicial:
		ord_ch = (ord(textocripto[i]) - ord(textoinicial[i]))%256
		chave_com += chr(ord_ch)
		i +=1
	return chave_com



textoinicial = abre_arquivo_in("pg27827.txt")

textocripto = abre_arquivo_out("pg27827.txt.enc")


cesar = descobre_cesar(textoinicial,textocripto)
print cesar


vigenere = descobre_vigenere(textoinicial, textocripto)
print vigenere
#print(textoinicial)
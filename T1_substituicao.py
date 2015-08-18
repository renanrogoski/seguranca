import time
import struct
import os
import math
import random

def abre_arquivo(nome):  
    arquivo  = open('arquivos3/'+nome, "rb")
    alfabeto = arquivo.read()    
    return alfabeto

def gravar_arquivo(nome, conteudo):    
    #inicio = int(tam_parte) * (int(parte)-1)
    arquivo = open('arquivos5/'+nome, 'ab+')
    arquivo.truncate() # limpa arquivo, para caso de salvar arquivo ja existente
    arquivo.seek(0)
    arquivo.write(conteudo)
    arquivo.close()
	
def random_not_repeat(conteudo):	
	count = 0
	myList = list(xrange(256))	
	num_random = []
	random.shuffle(myList)
	
	# Criando matriz
	matriz = []
	for l in range(len(conteudo)):      
		linha = []
		for c in range(2):			
			if(c == 0): 
				if(count > (len(conteudo)-1)): 
					campo = ' '
				else:
					campo = conteudo[l]

				linha = linha + [campo]
				count += 1
			else:
				campo = myList.pop()
				linha = linha + [campo]			

		matriz = matriz + [linha]		
	return matriz    

def substituicaoEncrypt(matriz, size):
	matrizRetorno=[]
	for i in range(size):
		linha=[]		
		for j in range(2):
			if(j == 1):
				linha.append(matriz[i][j])
		matrizRetorno.append(linha)
	return matrizRetorno

def substituicaoDecrypt(matriz_original, matriz_crip):
	result = ''	
	for i in range(len(matriz_crip)):
		linha=[]		
		for j in range(2):
			if(j == 1):				
				result = result + matriz_original[i][j-1]
	return result

entrada = abre_arquivo("textoinicial.txt")
print(entrada)
tabela = random_not_repeat(entrada)
print(tabela)

size = len(entrada)
crypt = substituicaoEncrypt(tabela,size)
#gravar_arquivo("cryptografado.txt", crypt)

print("\n\n\n")
print("\n\n\n")
print(crypt)

decrypt = substituicaoDecrypt(tabela,crypt)

print("\n\n\n")
print(decrypt)
gravar_arquivo("descryptografado.txt", decrypt)


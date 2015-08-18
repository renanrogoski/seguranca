import time
import struct
import os
import math

def abre_arquivo(nome):  
    arquivo  = open('arquivos3/'+nome, "rb")
    alfabeto = arquivo.read()    
    return alfabeto

def gravar_arquivo(nome, conteudo):    
    #inicio = int(tam_parte) * (int(parte)-1)
    arquivo = open('arquivos4/'+nome, 'ab+')
    arquivo.truncate() # limpa arquivo, para caso de salvar arquivo ja existente
    arquivo.seek(0)
    arquivo.write(conteudo)
    arquivo.close()
	
def cria_matriz(conteudo, key):
	count = 0 
	tamanho = len(conteudo)	
	linhas = int(math.ceil(float(tamanho)/float(key)))
	coluna = key #quantidade de colunas
	
	#transforma mensagem em uma matriz a partir da chave
	matriz = []
	for l in range(linhas):      
		linhas = []
		for c in range(coluna):			
			if(count > (len(conteudo)-1)): 
				chr = ' '
				linhas = linhas + [chr]
			else:
				chr = conteudo[count]
				linhas = linhas + [chr]
			count += 1

		matriz = matriz + [linhas]
	return matriz



def MatrizTransposta(matriz): #traspoe a matriz
	matrizRetorno=[]
	for j in range(len(matriz[0])):
		linha=[]
		for i in range(len(matriz)):
			linha.append(matriz[i][j])
		matrizRetorno.append(linha)
	return matrizRetorno

def printMatrix(matrix): # retorna cifra da matriz trasposta
	text_decrypt = '' #em uma string
	for i, element in enumerate(matrix):
		text_decrypt = text_decrypt+''.join(element)
	return text_decrypt

def monta_matriz_Transp(conteudo, key):
	count = 0
	tamanho = len(conteudo)	
	coluna = int(math.ceil(float(tamanho)/float(key))) #pega teto
	linha = key         #da divisao
	
	# Cria
	matriz = []
	for l in range(linha):      
		linha = []
		for c in range(coluna):			
			if(count > (len(conteudo)-1)): 
				campo = ' '
				linha = linha + [campo]
			else:
				campo = conteudo[count]
				linha = linha + [campo]
			count += 1

		matriz = matriz + [linha]
	return matriz
	
def transposicaoEncrypt(conteudo, key):
	matriz = cria_matriz(conteudo, key)
	Tmatriz = MatrizTransposta(matriz)
	
	return printMatrix(Tmatriz)

def transposicaoDecrypt(conteudo, key):	
	matriz = monta_matriz_Transp(conteudo, key)	
	Tmatriz = MatrizTransposta(matriz)	
	
	return printMatrix(Tmatriz)


message = abre_arquivo("textoinicial.txt")
print(message)

chave = 15


transposta = transposicaoEncrypt(message, chave)
print("\n")
print(transposta)

gravar_arquivo("cryptografado.txt", transposta)


decrypt = transposicaoDecrypt(transposta, chave)
print("\n")
print(decrypt)

gravar_arquivo("descryptografado.txt", decrypt)










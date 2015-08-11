import socket
import time
import hashlib
import struct
import os
import thread

letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def abre_arquivo(nome):  
    arquivo  = open('arquivos/'+nome, "rb")
    alfabeto = arquivo.read()    
    return alfabeto

def gravar_arquivo(nome, conteudo):    
    #inicio = int(tam_parte) * (int(parte)-1)
    arquivo = open('arquivos/'+nome, 'ab+')
    arquivo.truncate() # limpa arquivo, para caso de salvar arquivo ja existente
    arquivo.seek(0)
    arquivo.write(conteudo)
    arquivo.close()    

def criptografa(texto_limpo, chave):
    cifra = ''
    texto_limpo = texto_limpo.upper()

    for ch in texto_limpo:
        if ch in letters:
            idx = letters.find(ch) + int(chave)
            if idx >= 26:
                idx -= 26
            cifra += letters[idx]
    
    return cifra
 
def descriptografa(texto_cifrado, chave):    
    texto_limpo = ''
    texto_cifrado = texto_cifrado.upper()
    for ch in texto_cifrado:
        if ch in letters:
            idx = letters.find(ch) - int(chave)
            texto_limpo += letters[idx]
    return texto_limpo.upper()



	
################################ INICIA #####################################################
chave_cesar = raw_input('Cifra de Cesar - Insira a chave: ') 
# Criptografa   
texto_limpo = abre_arquivo('descriptografado.txt')
cifra = criptografa(texto_limpo, chave_cesar)  
gravar_arquivo('criptografado.txt', cifra)    
# Descriptografa
texto_cript = abre_arquivo('criptografado.txt')
texto_limpo = descriptografa(texto_cript, chave_cesar)  
gravar_arquivo('descriptografado.txt', texto_limpo)    



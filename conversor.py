import os
from time import sleep
from gtts import gTTS
import playsound
print('\t CONVERSOR DE TEXTO EM VOZ')


decisao = input(
    'Digite 1 para digitar texto para que eu leia ou 2 para ler a partir de um arquivo existente: ')
if decisao == '1':
    texto = input('Insira o texto: ')
    criacao_texto = gTTS(texto, lang='pt')
    print('Criando seu arquivo...')
    sleep(2)
    criacao_texto.save('arquivo.mp3')
    print('Arquivo Salvo!')
    print('Aqui está o seu aquivo:')
    playsound("arquivo.mp3")
else:
    decisao == '2'
with open('leitor de texto em voz/frase.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    criacao_texto2 = gTTS(conteudo, lang='pt-br')
    criacao_texto2.save('frase.mp3')
    playsound('frase.mp3')

import os
from tkinter import *
from tkinter import filedialog
import subprocess, sys


video = []
cam = ""
arquivoName = ""

janela = Tk()
janela.title("Create playlist for MPV")


directory_text_button = StringVar(value="Select")

def select_diretory():
     global cam
     diretorio = filedialog.askdirectory()
     cam = diretorio
     directory_text_button.set(cam)
     return diretorio

def programn():
    def criaArquivo(file):
        try:
            a = open(file, 'wt+')
            a.close()
        except:
            print('Erro na criação do arquivo')
        else:
            print('Arquivo {} criado com sucesso'.format(str(a.name)))
            
            
    def arquivoExiste(file):
        try:
            a = open(file, 'rt')
            a.close()
        except FileNotFoundError:
            return False
        else:
            return True

    def colocarVideo(video, arquivo):
        try:
            a = open(arquivo, 'at')
        except:
            print('Erro ao cadastar jogo')
        else:
            print(video)
            for v in video:
                print(v)
                a.write('{}\n'.format(v))
            path_dir = cam
            os.startfile(path_dir)
            print('Arquivo criado com sucesso')
            
            
    print(arquivoName)
    
    arquivo = '{}\{}.m3u'.format(cam, arquivoName.get())

    if arquivoExiste(arquivo):
        print('Arquivo localizado no computador')
    else:
        print('Arquivo inexistente, criando um novo...')
        criaArquivo(arquivo)



    os.chdir(cam)
    print(os.getcwd())

    for c in os.listdir():
        a, extensao = os.path.splitext(c)
        if extensao != '.m3u':
            video.append(c)
        
    colocarVideo(video, arquivo)




texto_orientacao = Label(janela, text="Select Directory").grid(column=0, row=0)
botao_diretorio = Button(janela, textvariable=directory_text_button, command=select_diretory).grid(column=1, row=0)

texto_orientacao2 = Label(janela, text="Name Playlist").grid(column=0, row=1)
arquivoName = Entry(janela, width=20)
arquivoName.grid(column=1, row=1)

botao = Button(janela, text="Generate Playlist", command=programn).grid(column=1, row=3)

#mainloop não deixa fechar a janela
janela.mainloop()



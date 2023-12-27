import time
import os
from os import *
import shutil

print("                               ############-- ROBOZINHO DO BEM --############")
print("\n\n\n    ---------------------> ATENÇÃO <--------------------")

print("\n SERÁ APAGADO TODOS OS ARQUIVOS (DOCUMENTOS, DOWNLOADS,FOTOS E AREA DE TRABALHO) NÃO PODERÃO SER RECUPERADOS!!!")
time.sleep(2)
resposta =  input('\n\nDeseja continuar? (Responda sim ou não)')

while True:

    if resposta not in ('sim','s','SIM'):
        print('Finalizado com sucesso')
        time.sleep(2)
        break


    
    print("Iniciando....")
    time.sleep(2)

    caminho = r'C:/Users'
    lista_arquivos = os.listdir(caminho)

    for c in lista_arquivos:

                    #Apagando Downloads
            try: 
                nome_completo = f'{caminho}/{c}/Downloads'
                print(F'\n{nome_completo}')
                chdir(nome_completo)
                arquivos = listdir(nome_completo)

                for d in arquivos:
                    if d != 'teste':
                        print(f"Arquivo {d} foi deletado com sucesso")
                        time.sleep(0.5)
                        try:
                            remove(d)
                        except:
                            
                            pass
                        try:
                            os.removedirs(d)
                        except:
                            
                            pass
                        try:
                            shutil.rmtree(d)
                        except:

                            pass
            except:
                print(f'O arquivo {nome_completo} não foi encontrado')
            #-----------------#
                
            #Apagando documentos
            try: 
                nome_completo = f'{caminho}/{c}/Documents'
                print(F'\n{nome_completo}')
                chdir(nome_completo)
                arquivos = listdir(nome_completo)

                for d in arquivos:
                    if d != 'teste':
                        print(f"Arquivo {d} foi deletado com sucesso")
                        time.sleep(0.5)
                        try:
                            remove(d)
                        except:
                            
                            pass
                        try:
                            os.removedirs(d)
                        except:
                            
                            pass
                        try:
                            shutil.rmtree(d)
                        except:

                            pass
            except:
                print(f'O arquivo {nome_completo} não foi encontrado')
            #-----------------#

            #Apagando Pictures
            try:
                nome_completo = f'{caminho}/{c}/Pictures'
                print(F'\n{nome_completo}')
                chdir(nome_completo)
                arquivos = listdir(nome_completo)

                for d in arquivos:
                    if d != 'teste':
                        print(f"Arquivo {d} foi deletado com sucesso")
                        time.sleep(0.5)
                        try:
                            remove(d)
                        except:
                            
                            pass
                        try:
                            os.removedirs(d)
                        except:
                            
                            pass
                        try:
                            shutil.rmtree(d)
                        except:

                            pass
            except:
                print(f'O arquivo {nome_completo} não foi encontrado')        
            #-----------------#

            #Apagando Desktop "COM EXCEÇÃO DOS ARQUIVOS"
            try:
                nome_completo = f'{caminho}/{c}/Desktop'
                print(F'\n{nome_completo}')
                chdir(nome_completo)
                arquivos = listdir(nome_completo)
               
                for d in arquivos:
                    while  True:
                        if d == 'Ghost Toolbox.lnk':
                            break
                        if d == 'Navegador Opera GX.lnk':
                            break
                        if d == 'AnyDesk.lnk':
                            break
                        if d == 'setup.exe':
                            break
                        
                        print(f"Arquivo {d} foi deletado com sucesso")
                        time.sleep(0.5)
                        try:
                            remove(d)
                        except:
                            
                            pass
                        try:
                            os.removedirs(d)
                        except:
                            
                            pass
                        try:
                            shutil.rmtree(d)
                        except:

                            pass
                        break
            except:
                print(f'O arquivo {nome_completo} não foi encontrado')        
            #-----------------#
                            
                        

    print('\nFinalizado com sucesso')

    print('\n\n\n\n\n\n                                    Desenvolvido por LEONARDO RAMOS =D ')

    time.sleep(20)

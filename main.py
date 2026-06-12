import os
import getpass

from datetime import datetime

usuario = getpass.getuser()

#chama as horas do sistema
data = datetime.now()

print("MankShell")
print("VERSÃO 1.0.0")

print
print("Digite 'ajuda' para mostrar uma lista de comandos")

def ajuda():
    print("""
    limpar: limpa o seu terminal mas continua no caminho atual
    sair: sai do terminal.
    date: mostra a data de hoje. ex:  16:00 12/04/2026
                            _________________________________
    \n
                        ---- COMANDOS DE CONTROLE DE ARQUIVOS ----
    ls: mostra os arquivos dentro do diretório atual.
    mkdir: cria um novo diretório * mkdir nomedapasta
    cd: Entra em um diretório * cd nomedapasta
    pwd: Mostra o caminho da pasta Atual. exemplo: home/user/documentos
    rm: Remove o diretório * rm meudiretorio
    rmdir: enomeia um diretorio * rnmdir projeto > meusite  
    touch: Cria um arquivo * touch main.jar
          
    """)




while True:
        diretorio = os.getcwd()
        cmd = input(f"{diretorio}~$ ")

        #comandos principais
        if cmd == "ajuda":
                ajuda()

        elif cmd == "limpar":
                os.system('cls')
                os.system('clear')


        elif cmd == "sair":
                print("Tchaaau")
                break
                
        elif cmd == "date":
                
                print(data.strftime("%H:%M %d/%m/%Y"))


        elif cmd == "whoami":
                print(usuario)

        #comandos de diretório e navegação
        elif cmd == "pwd":
                print(diretorio)
        
        elif cmd == "ls":
                arquivos = os.listdir();
                for arquivos in arquivos:
                        print(arquivos)

       
        elif cmd.startswith("cd "):
                pasta = cmd[3:]
                try:
                        os.chdir(pasta);
                except:
                        print("Diretório não encontrado");
        
        elif cmd.startswith("mkdir "):
                pasta = cmd[6:]
                os.mkdir(pasta);
                

        elif cmd.startswith("touch "):
                nome = cmd[6:]

                open(nome, "w").close()


        else:
                print("Comando não encontrado. deve estar errado")
    
        
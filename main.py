import os
import getpass
import subprocess

from datetime import datetime

usuario = getpass.getuser()

#chama as horas do sistema
data = datetime.now()

print("MankShell")
print("VERSÃO 1.0.0")

print
print("Digite 'help' para mostrar uma lista de comandos que você pode usar.")

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
    rmdir: remove um diretório vazio
    rename: renomeia um diretório
    touch: Cria um arquivo * touch main.jar
          
    """)




while True:

        #usuário e pastas
        user = getpass.getuser()
        diretorio = os.getcwd()

        cmd = input(f"{user}@Mankshell:{diretorio}~$ ")
        subprocess.run(cmd, shell=True)

        #comandos principais do terminal
        if cmd == "help":
                ajuda()

        elif cmd == "clear":
                os.system('cls')
                os.system('clear')


        elif cmd == "exit":
                print("Tchaaau")
                break
                
        elif cmd == "date":
                data = datetime.now()
                print(data.strftime("%H:%M %d/%m/%Y"))


        elif cmd == "whoami":
                print(usuario)

        #comandos de diretório e navegação
        elif cmd == "pwd":
                print(diretorio)
        
        elif cmd == "ls":
                arquivos = os.listdir();
                for arquivo in arquivos:
                        print(arquivo)

       
        elif cmd.startswith("cd "):
                pasta = cmd[3:]
                try:
                        os.chdir(pasta);
                except:
                        print("Diretório não encontrado");
        
        elif cmd.startswith("mkdir "):
                pasta = cmd[6:]
                try:
                        os.mkdir(pasta)
                except FileExistsError:
                        print("Essa pasta já existe")
                

        elif cmd.startswith("touch "):
                nome = cmd[6:]

                open(nome, "w").close()


        else:
                print("Comando não encontrado. deve estar errado")
    
        
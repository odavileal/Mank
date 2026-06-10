import os

print("MankShell")
print("VERSÃO 1.0.0")

print
print("Digite Ajuda para mostrar uma lista de comandos")

def ajuda():
    print("""
                            ---- COMANDOS ----
           
    ajuda: mostra isso que você tá vendo.
          
    limpar: limpa o seu terminal mas continua no caminho atual
    
    sair: sai do terminal.
          
    data: mostra o dia mês e hora, assim : 00/00/2026 
          
    hora: mostra as horas do seu sistema,inicialmente assim 00:00 mas você pode mudar 
          
    changeHourFormat: Muda o formato do horário de 00:00 pra 00pm/am e vice versa
          
                                __________________
    \n
                    ---- COMANDOS DE CONTROLE DE ARQUIVOS ----
          OBS: os comandos que estão com * no final da sinose se usam da seguinte forma: comando nome do diretório

    ls: mostra os arquivos dentro do diretório atual.
    mkdir: cria um novo diretório * mkdir nomedapasta
    cd: Entra em um diretório * cd nomedapasta
    pwd: Mostra o caminho da pasta Atual. exemplo: home/user/documentos
    rnmdir: renomeia um diretorio * rnmdir projeto > meusite
    rmdir: remove um arquivo * rmdir nomedapasta 
    
    """)

while True:
    cmd = input("~$ ")

    if cmd == "ajuda":
        ajuda()

    elif cmd == "limpar":
        os.system('cls')
        os.system('clear')

    elif cmd == "sair":
            print("Tchaaau")
            break

    else:
        print("Comando não encontrado. Escreveu errado não?")
    
        
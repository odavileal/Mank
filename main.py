import os
import getpass
import subprocess
import json
import readline
import platform
import psutil
import sys
from pathlib import Path
from datetime import datetime



os.system("clear")



def header():
    print(f"""
        ███╗   ███╗ █████╗ ███╗   ██╗██╗  ██╗     ██╗    ██████╗     ██████╗ 
        ████╗ ████║██╔══██╗████╗  ██║██║ ██╔╝    ███║   ██╔═████╗   ██╔═████╗
        ██╔████╔██║███████║██╔██╗ ██║█████╔╝     ╚██║   ██║██╔██║   ██║██╔██║
        ██║╚██╔╝██║██╔══██║██║╚██╗██║██╔═██╗      ██║   ████╔╝██║   ████╔╝██║
        ██║ ╚═╝ ██║██║  ██║██║ ╚████║██║  ██╗     ██║██╗╚██████╔╝██╗╚██████╔╝
        ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝     ╚═╝╚═╝ ╚═════╝ ╚═╝ ╚═════╝ 
      
      VERSÃO 1.1.0, para garantir atualizações vá em 'https://github.com/odavileal/Mank'
           Digite 'help' para mostrar uma lista de comandos que você pode usar.
           Use as SETAS PARA CIMA/BAIXO para navegar no histórico! ⬆️⬇️
      """)
header()


# ═══════════════════════════════════════════════════════════
# CONFIGURAÇÃO DO HISTÓRICO
# ═══════════════════════════════════════════════════════════

# Arquivo onde o histórico será salvo
HISTORY_FILE = Path.home() / ".mankshell_history"
READLINE_HISTORY = Path.home() / ".mankshell_readline"

# Lista para armazenar histórico da sessão atual
historico_sessao = []

# ═══════════════════════════════════════════════════════════
# FUNÇÕES DE HISTÓRICO
# ═══════════════════════════════════════════════════════════

def carregar_historico():
    """Carrega o histórico do arquivo se existir"""
    global historico_sessao
    
    if HISTORY_FILE.exists():
        try:
            with open(HISTORY_FILE, 'r', encoding='utf-8') as f:
                historico_sessao = json.load(f)
        except:
            historico_sessao = []
    else:
        historico_sessao = []
    
    # Carrega histórico no readline para usar com setas
    if READLINE_HISTORY.exists():
        try:
            readline.read_history_file(READLINE_HISTORY)
        except:
            pass


def salvar_historico():
    """Salva o histórico no arquivo"""
    try:
        with open(HISTORY_FILE, 'w', encoding='utf-8') as f:
            json.dump(historico_sessao, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"⚠️  Erro ao salvar histórico: {e}")


def salvar_readline_history():
    """Salva histórico do readline para usar com setas na próxima sessão"""
    try:
        readline.write_history_file(READLINE_HISTORY)
    except Exception as e:
        print(f"⚠️  Erro ao salvar readline history: {e}")


def adicionar_ao_historico(comando):
    """Adiciona um comando ao histórico"""
    global historico_sessao
    
    # Não adiciona comandos vazios ou que são "history"
    if comando.strip() and comando.strip() != "history":
        historico_sessao.append({
            "comando": comando,
            "horario": datetime.now().isoformat(),
            "diretorio": os.getcwd()
        })
        salvar_historico()


def mostrar_historico(filtro=None):
    """Mostra o histórico com opção de filtro"""
    if not historico_sessao:
        print("📭 Histórico vazio")
        return
    
    print("\n" + "═" * 80)
    print(f"{'#':>4} {'HORÁRIO':<20} {'COMANDO':<30} {'DIRETÓRIO':<25}")
    print("═" * 80)
    
    for i, item in enumerate(historico_sessao, 1):
        comando = item.get("comando", "")
        horario = item.get("horario", "")
        diretorio = item.get("diretorio", "")
        
        # Se há filtro, só mostra comandos que contêm o filtro
        if filtro and filtro.lower() not in comando.lower():
            continue
        
        # Formata o horário
        try:
            dt = datetime.fromisoformat(horario)
            horario_formatado = dt.strftime("%H:%M:%S %d/%m/%Y")
        except:
            horario_formatado = horario[:20]
        
        # Trunca comando e diretório se for muito longo
        cmd_truncado = comando[:27] + "..." if len(comando) > 30 else comando
        dir_truncado = diretorio[-22:] if len(diretorio) > 25 else diretorio
        
        print(f"{i:>4} {horario_formatado:<20} {cmd_truncado:<30} {dir_truncado:<25}")
    
    print("═" * 80 + "\n")


def limpar_historico():
    """Limpa todo o histórico"""
    global historico_sessao
    resposta = input("⚠️  Tem certeza que quer limpar TODO o histórico? (s/n): ").lower()
    
    if resposta == 's' or resposta == 'sim':
        historico_sessao = []
        salvar_historico()
        print("✅ Histórico limpo com sucesso!")
    else:
        print("❌ Operação cancelada")


def configurar_readline():
    """Configura o readline para melhor experiência com histórico"""
    # Permite editar linhas com setas
    readline.parse_and_bind('tab: complete')
    
    # Configura o histórico para salvar e carregar
    try:
        readline.read_history_file(READLINE_HISTORY)
    except FileNotFoundError:
        pass



# mostrar o mankfetch

def mankfetch(): 
    info = f"""                                                   
     __  __           _    __     _      _    
    |  \/  |__ _ _ _ | |__/ _|___| |_ __| |_  
    | |\/| / _` | ' \| / /  _/ -_)  _/ _| ' \ 
    |_|  |_\__,_|_||_|_\_\_| \___|\__\__|_||_|
                                           

    Usuário : {getpass.getuser()}
    Sistema : {platform.system()}
    Kernel  : {platform.release()}
    Python  : {sys.version.split()[0]}
    Shell   : MankShell 1.1.0
    Pasta   : {os.getcwd()}
    CPU      : {psutil.cpu_percent(interval=1)}
    RAM      : {round(psutil.virtual_memory().total / (1024**3), 1)}GB
    Arquitetura : {platform.machine()}
"""
    print(info)
                                                                                         



# Carrega o histórico ao iniciar
carregar_historico()
configurar_readline()
 # mostra o cabeçalho toda vez que se entra no terminal

def ajuda():
    print("""
    clear ou cls: limpa o seu terminal mas continua no caminho atual
    sair ou exit: sai do terminal.
    date: mostra a data de hoje. ex:  16:00 12/04/2026
                            _________________________________
    
                        ---- COMANDOS DE CONTROLE DE ARQUIVOS ----
    ls: mostra os arquivos dentro do diretório atual.
    mkdir: cria um novo diretório * mkdir nomedapasta
    cd: Entra em um diretório * cd nomedapasta
    pwd: Mostra o caminho da pasta Atual. exemplo: home/user/documentos
    rm: remove um diretório vazio
    rm -rf: remove um diretório não vazio
    mv: renomeia um diretório
    touch: Cria um arquivo * touch main.jar
    
                        ---- COMANDOS DE HISTÓRICO ----
    history: mostra todo o histórico de comandos
    history <filtro>: mostra histórico filtrando por palavra-chave
    history clear: limpa todo o histórico
    
    ⬆️⬇️ Use as SETAS PARA CIMA e BAIXO para navegar no histórico!
          
    """)

while True:
    try:
        # usuário e pastas
        diretorio = os.getcwd()

        cmd = input(f"@MS{diretorio}~$ ")

        # ===== COMANDOS PRINCIPAIS DO TERMINAL =====
        if cmd == "help" or cmd == "ajuda":
            ajuda()

        elif cmd == "clear" or cmd == "cls" or cmd == "limpar":
            os.system('cls' if os.name == 'nt' else 'clear')
            header() # mostra o cabeçalho com ascii depois de limpar os comandos

        elif cmd == "exit" or cmd == "sair":
            salvar_historico()
            salvar_readline_history()
            print("Tchaaau 👋")
            break

        elif cmd == "date" or cmd == "data":
            data = datetime.now()
            print(data.strftime("%H:%M %d/%m/%Y"))
            adicionar_ao_historico(cmd)

        elif cmd == "mankfetch":
            mankfetch()

        # ===== COMANDOS DE HISTÓRICO =====
        elif cmd == "history":
            mostrar_historico()

        elif cmd.startswith("history "):
            argumento = cmd[8:].strip()
            
            if argumento == "clear":
                limpar_historico()
            else:
                # Mostra histórico filtrado
                mostrar_historico(filtro=argumento)
            
            adicionar_ao_historico(cmd)

        # ===== COMANDOS DE DIRETÓRIO E NAVEGAÇÃO =====
        elif cmd.startswith("cd "):
            pasta = cmd[3:]
            try:
                os.chdir(pasta)
                adicionar_ao_historico(cmd)
            except FileNotFoundError:
                print(f" ❌ Erro: Diretório '{pasta}' não encontrado")
            except PermissionError:
                print(f" ❌ Erro: Sem permissão para acessar '{pasta}'")
            except Exception as e:
                print(f" ❌ Erro inesperado: {e}")

        # ===== COMANDOS DO SISTEMA =====
        else:
            resultado = subprocess.run(cmd, shell=True)
            if resultado.returncode != 0:
                print("Comando não encontrado")
            else:
                adicionar_ao_historico(cmd)

    except KeyboardInterrupt:
        print("\n\n⚠️  Ctrl+C pressionado. Digite 'exit' para sair.")
    except EOFError:
        print("\n\nTchaaau 👋")
        salvar_historico()
        salvar_readline_history()
        break
    except Exception as e:
        print(f"❌ Erro inesperado: {e}")
import subprocess
import threading
from pathlib import Path

# Cores ANSI para output em terminal
COR_BRANCO = "\033[1;37m"
COR_VERDE = "\033[1;32m"
COR_FIM = "\033[0m"

# Diretório para armazenar relatórios
DIRETORIO_RELATORIOS = Path("relatorios_scan")
DIRETORIO_RELATORIOS.mkdir(exist_ok=True)

def executar_nmap(alvo: str) -> None:
    print(f"{COR_BRANCO}[+]{COR_FIM} Iniciando scan: {COR_BRANCO}{alvo}{COR_FIM}")

    comando = ["nmap", "-T4", "-F", "-Pn", "--open", alvo]
    try:
        processo = subprocess.Popen(comando, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    except FileNotFoundError:
        print(f"{COR_BRANCO}[!] Erro: Nmap não está instalado ou não foi encontrado no PATH.{COR_FIM}")
        return

    saida = []
    for linha in processo.stdout:
        print(linha.strip())
        saida.append(linha)

    nome_arquivo = DIRETORIO_RELATORIOS / f"relatorio_{alvo.replace('.', '_').replace('/', '_')}.txt"
    nome_arquivo.write_text(''.join(saida))

    print(f"{COR_VERDE}[✔]{COR_FIM} Scan concluído: {COR_BRANCO}{alvo}{COR_FIM} | Relatório salvo em: {COR_BRANCO}{nome_arquivo}{COR_FIM}")

def main() -> None:
    print(f"{COR_BRANCO}---[ Scanner Nmap Profissional Otimizado ]---{COR_FIM}")
    entrada = input(f"{COR_BRANCO}[?] Introduza os alvos (separados por vírgula): {COR_FIM}")
    alvos = list(set([a.strip() for a in entrada.split(',') if a.strip()]))

    if not alvos:
        print(f"{COR_BRANCO}[!] Nenhum alvo válido introduzido.{COR_FIM}")
        return

    threads = []
    for alvo in alvos:
        t = threading.Thread(target=executar_nmap, args=(alvo,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print(f"{COR_VERDE}[✔]{COR_FIM} Todos os scans foram concluídos.")

if __name__ == "__main__":
    main()

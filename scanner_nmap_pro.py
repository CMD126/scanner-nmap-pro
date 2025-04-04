import subprocess
import threading
import os

# Cores para o terminal (estilo Linux profissional)
branco = "\033[1;37m"
verde = "\033[1;32m"
fim = "\033[0m"

# Função que realiza o scan rapidamente com Nmap
def executar_nmap(alvo):
    print(f"{branco}[+]{fim} Iniciando scan: {branco}{alvo}{fim}")

    comando = ["nmap", "-T4", "-F", "-Pn", "--open", alvo]
    processo = subprocess.Popen(comando, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)

    saida = ""
    while True:
        linha = processo.stdout.readline()
        if not linha:
            break
        print(linha.strip())
        saida += linha

    pasta_relatorios = "relatorios_scan"
    os.makedirs(pasta_relatorios, exist_ok=True)

    nome_seguro = alvo.replace(".", "_").replace("/", "_")
    nome_arquivo = f"{pasta_relatorios}/relatorio_{nome_seguro}.txt"

    with open(nome_arquivo, "w") as arquivo:
        arquivo.write(saida)

    print(f"{verde}[✔]{fim} Scan concluído: {branco}{alvo}{fim} | Salvo em: {branco}{nome_arquivo}{fim}")

# Função principal do script
def main():
    print(f"{branco}---[ Scanner Nmap Profissional Otimizado ]---{fim}")
    alvos = input(f"{branco}[?] Alvos separados por vírgula:{fim} ").split(',')

    threads = []
    for alvo in alvos:
        alvo = alvo.strip()
        thread = threading.Thread(target=executar_nmap, args=(alvo,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print(f"{verde}[✔]{fim} Todos os scans finalizados com sucesso.")

# Inicializa o script
if __name__ == "__main__":
    main()

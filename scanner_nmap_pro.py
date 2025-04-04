import subprocess
import threading
import os


branco = "\033[1;37m"
verde = "\033[1;32m"
vermelho = "\033[1;31m"
fim = "\033[0m"

def executar_nmap(alvo):
    print(f"{branco}[+]{fim} Iniciando scan: {branco}{alvo}{fim}")
    resultado = subprocess.run(["nmap", "-sV", "-sC", "-Pn", "--open", alvo], capture_output=True, text=True)

    pasta_relatorios = "relatorios_scan"
    os.makedirs(pasta_relatorios, exist_ok=True)

    nome_arquivo = f"{pasta_relatorios}/relatorio_{alvo.replace('.', '_')}.txt"
    with open(nome_arquivo, "w") as arquivo:
        arquivo.write(resultado.stdout)

    print(f"{verde}[✔]{fim} Scan concluído: {branco}{alvo}{fim} | Salvo em: {branco}{nome_arquivo}{fim}")

def main():
    print(f"{branco}---[ Scanner Nmap Profissional ]---{fim}")
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

if __name__ == "__main__":
    main()

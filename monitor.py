import platform
import datetime
import os
import psutil 

def gerar_relatorio():
    sistema = platform.system()
    versao = platform.release()
    arquitetura = platform.machine()
    usuario = os.getlogin()
    data_atual = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    
    # Capturando Hardware
    uso_ram = psutil.virtual_memory().percent
    uso_cpu = psutil.cpu_percent(interval=1) # Mede a CPU por 1 segundo

    relatorio = (
        f"--- RELATÓRIO DE SISTEMA ---\n"
        f"Data/Hora: {data_atual}\n"
        f"Usuário: {usuario}\n"
        f"SO: {sistema}\n"
        f"Kernel: {versao}\n"
        f"Arquitetura: {arquitetura}\n"
        f"Uso de RAM: {uso_ram}%\n"
        f"Uso de CPU: {uso_cpu}%\n" # Nova linha!
        f"---------------------------\n"
    )

    with open("log_sistema.txt", "a") as arquivo:
        arquivo.write(relatorio)
    
    print(f"✅ Monitoramento completo! (RAM: {uso_ram}% | CPU: {uso_cpu}%)")

if __name__ == "__main__":
    gerar_relatorio()

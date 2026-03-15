import platform
import datetime
import os
import psutil  # Nossa nova ferramenta

def gerar_relatorio():
    sistema = platform.system()
    versao = platform.release()
    arquitetura = platform.machine()
    usuario = os.getlogin()
    data_atual = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    
    # Capturando uso de memória RAM (Dinâmico)
    memoria = psutil.virtual_memory()
    uso_ram = memoria.percent

    relatorio = (
        f"--- RELATÓRIO DE SISTEMA ---\n"
        f"Data/Hora: {data_atual}\n"
        f"Usuário: {usuario}\n"
        f"SO: {sistema}\n"
        f"Kernel: {versao}\n"
        f"Arquitetura: {arquitetura}\n"
        f"Uso de RAM: {uso_ram}%\n"
        f"---------------------------\n"
    )

    with open("log_sistema.txt", "a") as arquivo:
        arquivo.write(relatorio)
    
    print(f"✅ Relatório atualizado com sucesso! (RAM: {uso_ram}%)")

if __name__ == "__main__":
    gerar_relatorio()

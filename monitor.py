import platform
import datetime
import os

def gerar_relatorio():
    # Coletando os dados do seu Linux
    sistema = platform.system()
    versao = platform.release()
    arquitetura = platform.machine()
    usuario = os.getlogin()
    data_atual = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    # Formatando a mensagem (Template de Log)
    relatorio = (
        f"--- RELATÓRIO DE SISTEMA ---\n"
        f"Data/Hora: {data_atual}\n"
        f"Usuário: {usuario}\n"
        f"SO: {sistema}\n"
        f"Kernel: {versao}\n"
        f"Arquitetura: {arquitetura}\n"
        f"---------------------------\n"
    )

    # Gravando no arquivo (Modo 'a' de append para não apagar o anterior)
    with open("log_sistema.txt", "a") as arquivo:
        arquivo.write(relatorio)

    print(f"✅ Relatório salvo com sucesso para o usuário {usuario}!")

if __name__ == "__main__":
    gerar_relatorio()

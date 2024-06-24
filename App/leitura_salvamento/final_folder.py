import os

def criar_pasta(pasta_consulta, pasta_resultado):
    # Extrair o nome da nova pasta do caminho da pasta de consulta
    nome_nova_pasta = os.path.basename(pasta_consulta)
    
    # Construir o caminho completo para a nova pasta no diretório de resultado
    caminho_nova_pasta = os.path.join(pasta_resultado, nome_nova_pasta)
    
    # Verificar se a pasta já existe
    if not os.path.exists(caminho_nova_pasta):
        # Criar a nova pasta
        os.makedirs(caminho_nova_pasta)
        print(f"Pasta criada: {caminho_nova_pasta}")
    else:
        print(f"A pasta {caminho_nova_pasta} já existe.")


    return caminho_nova_pasta


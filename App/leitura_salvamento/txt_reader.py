import pandas as pd
import os

def convert_to_numeric(series):
    try:
        return pd.to_numeric(series)
    except (ValueError, TypeError):
        # Aqui você pode decidir como lidar com os erros de conversão
        return series  # Por exemplo, retornar a série original ou outro valor padrão


def ler_txt(input_dir, txt_file):
    caminho_arquivo = os.path.join(input_dir, txt_file)
    linhas = []

    with open(caminho_arquivo, 'r', encoding='UTF-8') as arquivo:
        # Ler o arquivo linha a linha
        for idx, linha in enumerate(arquivo):
            if idx >= 7:  # Começa a partir da linha 8 (índice 7)
                linhas.append(linha.strip().split())  # strip() remove espaços em branco e quebras de linha, split() para separar por espaços

    # Criando DataFrame
    df = pd.DataFrame(linhas)

    # Definindo a primeira linha como nomes das colunas
    df.columns = df.iloc[0]

    # Removendo a primeira linha que agora é usada como nomes das colunas
    df = df[1:]

    # Aplica a função convert_to_numeric em cada coluna do DataFrame
    df = df.apply(convert_to_numeric)

    return df


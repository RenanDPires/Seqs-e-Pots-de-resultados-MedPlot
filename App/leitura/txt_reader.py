import pandas as pd

def reader(txt):
    linhas=[]
    with open(txt, 'r') as arquivo:
    # Ler o arquivo linha a linha
        for idx, linha in enumerate(arquivo):
            if idx >= 7:  # Começa a partir da linha 8 (índice 7)
                linhas.append(linha.strip())  # strip() remove espaços em branco e quebras de linha

    # Supondo que os dados são separados por vírgulas, você pode converter diretamente em um DataFrame
    df = pd.DataFrame([linha.split(',') for linha in linhas])

    # Se a primeira linha das informações contém os nomes das colunas, você pode definir isso
    df.columns = df.iloc[0]  # Define a primeira linha como nome das colunas
    df = df[1:]  # Remove a primeira linha que agora é usada como nome das colunas

    return df
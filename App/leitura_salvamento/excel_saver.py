import pandas as pd
import os

def salvar_excel(df, caminho, arquivo):
    caminho_completo = os.path.join(caminho, arquivo)

    # Salvando o DataFrame em um arquivo Excel na pasta especificada
    df.to_excel(caminho_completo, index=False)
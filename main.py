import os
import json
from App.calculos.calculoSeqs import calcular_sequencia_positiva_dataframe
from App.leitura_salvamento.txt_reader import ler_txt
from App.leitura_salvamento.excel_saver import salvar_excel
from App.leitura_salvamento.final_folder import criar_pasta


def main(input, output, config, padrao_nome_arquivo_final):
    pasta_final= criar_pasta(pasta_consulta, pasta_resultado)
    data_handler(input, pasta_final, config, padrao_nome_arquivo_final)
    

def carregar_configuracoes(caminho_arquivo):
    with open(caminho_arquivo, 'r') as arquivo:
        configuracoes = json.load(arquivo)
    print('Configuração carregada')
    return configuracoes

def data_handler(input, output, config, padrao_nome_arquivo_final):
    # Ler arquivos .txt 1 a 1
    arquivos_txt = [f for f in os.listdir(input) if os.path.isfile(os.path.join(input, f)) and f.endswith('.txt')]
    for txt in arquivos_txt:
        print(f'Lendo arquivo: \t {txt}')
        df= ler_txt(input,txt)
        
        resultado= calculos(df, config)
        if not isinstance(resultado, str):
            nome_arquivo= padrao_nome_arquivo_final+'_'+txt.replace('.txt', '.xlsx')
            salvar_excel(resultado, output, nome_arquivo)

def calculos(df, config):
    tipo=''
    resposta= ''
    print('\tValidando se os dados possibilitam os cálculos')
    if 'VA_mod_(V)' in df.columns and 'VB_mod_(V)' in df.columns and 'VC_mod_(V)' in df.columns:
        print('\t\tÉ possível calcular Tensão de Seq+')
        tipo= 'tensao'
        if 'IA_mod_(A)' in df.columns and 'IB_mod_(A)' in df.columns and 'IC_mod_(A)' in df.columns:
            print('\t\tÉ possível calcular Corrente de Seq+')
            print('\t\tÉ possível calcular Potência ativa')
            tipo= tipo+'_corrente'
        print(f'\tCalculando dados')
        resposta = calcular_sequencia_positiva_dataframe(df, config,tipo)  # Caso o tipo tenha tensão e corrente, iremos calcular a pot ativa também
    
    elif 'IA_mod_(A)' in df.columns and 'IB_mod_(A)' in df.columns and 'IC_mod_(A)' in df.columns:
        print('\t\tÉ possível calcular Corrente de Seq+')
        tipo= tipo+'_corrente'
        print(f'\tCalculando dados')
        resposta = calcular_sequencia_positiva_dataframe(df, config,tipo)  # Caso o tipo tenha tensão e corrente, iremos calcular a pot ativa também
        
    else:
        print('Este terminal não permite cálculos')

    return resposta


if __name__ == "__main__":
    # Caminho para o arquivo JSON de configuração (na mesma pasta do script)
    caminho_config_json = os.path.join(os.path.dirname(__file__), 'config.json')

    # Carrega as configurações do arquivo JSON
    configuracoes = carregar_configuracoes(caminho_config_json)

    # Acesso às variáveis de configuração
    pasta_consulta = r'C:\Users\renan\OneDrive\Área de Trabalho\OneDrive-2024-06-24\20221208_142230_142329_60_OpenPDC_ONS_BSB_10_15_22'
    pasta_resultado = r'D:\Projetos\Seq+ e Pots - MedPlot\Seqs-e-Pots-de-resultados-MedPlot\Resultados' # Pasta raiz do resultado final
    padrao_nome_arquivo_final = configuracoes['PADRAO_NOME_ARQUIVO_FINAL'] # prefixo padrão na nomenclatura do arquivo
    config_file = configuracoes

    main(pasta_consulta,pasta_resultado, config_file, padrao_nome_arquivo_final)
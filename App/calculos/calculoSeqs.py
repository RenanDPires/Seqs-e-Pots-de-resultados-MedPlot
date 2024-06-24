import cmath
import math
import pandas as pd
from App.calculos.calculoPots import calcular_pots_seq_1, calcular_pots_3_fases


def calcular_sequencia_positiva_tensoes(V_a_mag, V_a_angle, V_b_mag, V_b_angle, V_c_mag, V_c_angle):
    
    # Converte ângulos de graus para radianos
    theta_a = math.radians(V_a_angle)
    theta_b = math.radians(V_b_angle)
    theta_c = math.radians(V_c_angle)

    # Converte para forma retangular usando a fórmula V_mag * exp(j * theta)
    V_a = cmath.rect(V_a_mag, theta_a)
    V_b = cmath.rect(V_b_mag, theta_b)
    V_c = cmath.rect(V_c_mag, theta_c)

    # Operadores de rotação de fase
    a = cmath.exp(2j * math.pi / 3)
    a2 = cmath.exp(-2j * math.pi / 3)

    # Calcula a sequência positiva
    V_pos = (V_a + a * V_b + a2 * V_c) / 3

    # Calcula o módulo e o ângulo da sequência positiva
    V_pos_mag = abs(V_pos)
    V_pos_angle = cmath.phase(V_pos)  # Retorna o ângulo em radianos

    # Converter ângulo de radianos para graus
    V_pos_angle_deg = math.degrees(V_pos_angle)

    
    return V_pos_mag, V_pos_angle_deg

def calcular_sequencia_positiva_correntes(I_a_mag, I_a_angle, I_b_mag, I_b_angle, I_c_mag, I_c_angle):

    # Converte ângulos de graus para radianos
    theta_a = math.radians(I_a_angle)
    theta_b = math.radians(I_b_angle)
    theta_c = math.radians(I_c_angle)

    # Converte para forma retangular usando a fórmula I_mag * exp(j * theta)
    I_a = cmath.rect(I_a_mag, theta_a)
    I_b = cmath.rect(I_b_mag, theta_b)
    I_c = cmath.rect(I_c_mag, theta_c)

    # Operadores de rotação de fase
    a = cmath.exp(2j * math.pi / 3)
    a2 = cmath.exp(-2j * math.pi / 3)

    # Calcula a sequência positiva das correntes
    I_pos = (I_a + a * I_b + a2 * I_c) / 3

    # Calcula o módulo e o ângulo da sequência positiva das correntes
    I_pos_mag = abs(I_pos)
    I_pos_angle = cmath.phase(I_pos)  # Retorna o ângulo em radianos

    # Converter ângulo de radianos para graus
    I_pos_angle_deg = math.degrees(I_pos_angle)


    return I_pos_mag, I_pos_angle_deg

def calcular_sequencia_positiva_dataframe(df, config, tipo):
    # Criar uma lista para armazenar os resultados

    if 'tensao' in tipo:
        result_tensoes_seq_1 = []
        print('\t\tCalculando Tensão de Seq+')
        # Iterar sobre as linhas do DataFrame
        for index, row in df.iterrows():
            # Extrair os valores das colunas mapeadas para tensões
            V_values = {param_name: row[col_name] for col_name, param_name in config['tensoes']['columns'].items()}
            V_pos_mag, V_pos_angle_deg = calcular_sequencia_positiva_tensoes(**V_values)

            # Construir um dicionário com os resultados
            result_row = {
                'Tempo_(SOC)': row['Tempo_(SOC)'],
                'V_Seq_Pos_(V)': V_pos_mag,
                'V_Seq_Pos_(graus)': V_pos_angle_deg
            }
            # Adicionar o resultado à lista de resultados
            
            result_tensoes_seq_1.append(result_row)
        result_tensoes_seq_1 = pd.DataFrame(result_tensoes_seq_1)
        result_tensoes_seq_1['V_Seq_Pos_(V)'] = result_tensoes_seq_1['V_Seq_Pos_(V)'].astype(float)
        result_tensoes_seq_1['V_Seq_Pos_(graus)'] = result_tensoes_seq_1['V_Seq_Pos_(graus)'].astype(float)

    
    
    
    if 'corrente' in tipo:
        result_correntes_seq_1 = []
        print('\t\tCalculando Corrente de Seq+')
        # Iterar sobre as linhas do DataFrame
        for index, row in df.iterrows():
            # Extrair os valores das colunas mapeadas para correntes
            I_values = {param_name: row[col_name] for col_name, param_name in config['correntes']['columns'].items()}
            I_pos_mag, I_pos_angle_deg = calcular_sequencia_positiva_correntes(**I_values)

            # Construir um dicionário com os resultados
            result_row = {
                'Tempo_(SOC)': row['Tempo_(SOC)'],
                'I_Seq_Pos_(A)': I_pos_mag,
                'I_Seq_Pos_(graus)': I_pos_angle_deg
            }

            # Adicionar o resultado à lista de resultados
            
            result_correntes_seq_1.append(result_row)
        result_correntes_seq_1 = pd.DataFrame(result_correntes_seq_1)
        result_correntes_seq_1['I_Seq_Pos_(A)'] = result_correntes_seq_1['I_Seq_Pos_(A)'].astype(float)
        result_correntes_seq_1['I_Seq_Pos_(graus)'] = result_correntes_seq_1['I_Seq_Pos_(graus)'].astype(float)


    val_tensoes= 'result_tensoes_seq_1' in locals()
    val_correntes= 'result_correntes_seq_1' in locals()

    if val_tensoes and val_correntes:
        df_final = pd.merge(result_tensoes_seq_1, result_correntes_seq_1, on='Tempo_(SOC)', how='inner')
        resultados_df = pd.DataFrame(df_final)
        df_pot_seq_1 = calcular_pots_seq_1(resultados_df)
        df_pot_3_fases = calcular_pots_3_fases(df)

        df_final = pd.merge(df_pot_seq_1, df_pot_3_fases, on='Tempo_(SOC)', how='inner')

        # Obtendo o nome das colunas
        colunas = list(df_final.columns)

        # Mapeando as colunas que serão movidas para as novas posições desejadas
        movimentos = {
            'Pot. Ativa 3 fases (MW)': 7,
            'Pot. Reativa 3 fases (MVAr)': 8
        }

        # Realizando os movimentos das colunas
        for coluna, nova_posicao in movimentos.items():
            indice_atual = colunas.index(coluna)
            colunas.insert(nova_posicao, colunas.pop(indice_atual))

        # Recriando o DataFrame com a nova ordem das colunas
        df_final = df_final[colunas]


    else:
        if 'result_tensoes_seq_1' in locals():
            df_final= pd.merge(result_tensoes_seq_1, df, on='Tempo_(SOC)', how='inner')

        if 'result_correntes_seq_1' in locals():
            df_final= pd.merge(result_correntes_seq_1, df, on='Tempo_(SOC)', how='inner')
            
    # Criar um DataFrame a partir da lista de resultados

    df_final['Tempo_(SOC)'] = df_final['Tempo_(SOC)'].apply(lambda x: '{:.5f}'.format(x))

    print('\tCálculos finalizados\n')

    return df_final
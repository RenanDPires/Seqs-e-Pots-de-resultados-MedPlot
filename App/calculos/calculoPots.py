import pandas as pd
import numpy as np

def calcular_pots_seq_1(df):
    
    V_seq = df['V_Seq_Pos_(V)']
    I_seq = df['I_Seq_Pos_(A)']

    # Calculando a potência ativa (P = V * I * cos(theta))
    cos_theta = np.cos(np.radians(df['V_Seq_Pos_(graus)'] - df['I_Seq_Pos_(graus)']))
    pot_ativa_seq_pos = 3 * V_seq * I_seq * cos_theta / 1000000  # dividido por 1.000.000 para obter em MW
    

    # Calculando a potência reativa (Q = V * I * sin(theta))
    sin_theta = np.sin(np.radians(df['V_Seq_Pos_(graus)'] - df['I_Seq_Pos_(graus)']))
    pot_reativa_seq_pos = 3 * V_seq * I_seq * sin_theta / 1000000  # dividido por 1.000.000 para obter em MVAR

    # Adicionando as colunas de potência ativa e reativa ao DataFrame
    df['Pot. Ativa Seq+ (MW)'] = pot_ativa_seq_pos
    df['Pot. Reativa Seq+ (MVAR)'] = pot_reativa_seq_pos

    return df

def calcular_pots_3_fases(df):
    # Calculando o fator de potência (cos(theta)) para cada fase
    cos_theta_A = np.cos(np.radians(df['VA_ang_(graus)'] - df['IA_ang_(graus)']))
    cos_theta_B = np.cos(np.radians(df['VB_ang_(graus)'] - df['IB_ang_(graus)']))
    cos_theta_C = np.cos(np.radians(df['VC_ang_(graus)'] - df['IC_ang_(graus)']))

    # Calculando a potência ativa por fase
    P_A = df['VA_mod_(V)'] * df['IA_mod_(A)'] * cos_theta_A / 1000000  # em MW
    P_B = df['VB_mod_(V)'] * df['IB_mod_(A)'] * cos_theta_B / 1000000  # em MW
    P_C = df['VC_mod_(V)'] * df['IC_mod_(A)'] * cos_theta_C / 1000000  # em MW

    # Somando a potência ativa trifásica
    P_total = P_A + P_B + P_C

    # Calculando a potência reativa (sin(theta)) para cada fase
    sin_theta_A = np.sin(np.radians(df['VA_ang_(graus)'] - df['IA_ang_(graus)']))
    sin_theta_B = np.sin(np.radians(df['VB_ang_(graus)'] - df['IB_ang_(graus)']))
    sin_theta_C = np.sin(np.radians(df['VC_ang_(graus)'] - df['IC_ang_(graus)']))

    # Calculando a potência reativa por fase
    Q_A = df['VA_mod_(V)'] * df['IA_mod_(A)'] * sin_theta_A / 1000000  # em MVAR
    Q_B = df['VB_mod_(V)'] * df['IB_mod_(A)'] * sin_theta_B / 1000000  # em MVAR
    Q_C = df['VC_mod_(V)'] * df['IC_mod_(A)'] * sin_theta_C / 1000000  # em MVAR

    # Somando a potência reativa trifásica
    Q_total = Q_A + Q_B + Q_C

    # Adicionando as colunas de potência ativa e reativa ao DataFrame
    df['Pot. Ativa 3 fases (MW)'] = P_total
    df['Pot. Reativa 3 fases (MVAR)'] = Q_total

    return df
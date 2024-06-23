from dotenv import load_dotenv
import os
#from App.calculos.calculoSeqs import 
#from App.calculos.calculoSeqs import
from SEQS-E-Pots.App.leitura.txt_reader import reader


def main(input, output):
    # Ler arquivos .txt 1 a 1
    arquivos_txt = [f for f in os.listdir(PASTA_CONSULTA) if os.path.isfile(os.path.join(PASTA_CONSULTA, f)) and f.endswith('.txt')]
    for txt in arquivos_txt:
        df= reader(txt)
        print(df)

        

if __name__ == "__main__":
    load_dotenv()
    # A pasta de consulta deve conter os .txt de interesse, não precisa do XML
    PASTA_CONSULTA= os.getenv('PASTA_CONSULTA') # Todos os arquivos desse diretório terão suas Seqs e Pots calculados / salvos
    
    # Diretório raiz e final desses cálculos
    PASTA_RESULTADO= os.getenv('PASTA_RESULTADO') # Dentro dessa raiz, teremos **1 pasta de input* para **1 pasta de output**
    main(PASTA_CONSULTA,PASTA_RESULTADO)
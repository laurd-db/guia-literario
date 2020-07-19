import pandas as pd
import numpy as np

def load (path):
    """
    Retorna um dataframe a partir do dados_guia_literario.xlsx
    """

    try:
        
        # lê arquivo xlsx
        df = pd.read_excel(path)

        # trocando o tipo das colunas
        df = df.astype({"ano_objeto":object,"pagina":object})
        
        return df

    except Exception as e:

        print(str(e))
import pandas as pd 

def load (path):
    """
    Retorna um dataframe a partir do coordenadas.csv
    """

    try:

        # lê arquivo csv
        df = pd.read_csv(path)

        # troca os nomes das colunas
        df = df.rename(columns={"Name":"id","Latitude":"lat","Longitude":"lng"})

        return df

    except Exception as e:
        print (str(e))
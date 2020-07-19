import pandas as pd 
from tqdm import tqdm
import math

import kmltocsv, location, data_literario #, export

def convert(subset):
    for i in range(len(subset)):
        if math.isfinite(subset[i]):
            subset[i] = int(subset[i])
            #print (subset[i])
        else:
            subset[i] = "Sem informação"
            #print(subset[i])
    return subset


def main ():
    """
    Executa todas as funções
    """

    try:
        paths = open('keys.txt', 'r')
        path_dict = {}
        for line in paths:
            path_key, path_value = line.split('=')
            path_dict[path_key] = path_value.rstrip("\n")

        with tqdm(total=100) as pbar:

            # convertendo KML para CSV
            pbar.set_description("Convertendo dados geográficos...")
            kmltocsv.load(path_dict["KML_PATH"],path_dict["LOC_PATH"])
            
            # cria um geodataframe das localizações
            pbar.set_description("Carregando coordenadas...")
            location_df = location.load(path_dict["LOC_PATH"])
            pbar.update(5)

            # cria um dataframe dos dados literários
            pbar.set_description("Carregando dados literários...")
            datalit_df = data_literario.load(path_dict["LIT_PATH"])
            pbar.update(5)

            # junta todos os dataframes parciais
            pbar.set_description("Atualizando metadados...")
            final_df = pd.merge(datalit_df,location_df, on=["id"], how="left")
            # converte valores float para int
            final_df["ano_objeto"] = convert(final_df["ano_objeto"].copy(deep=True))
            final_df["ano_obra"] = convert(final_df["ano_obra"].copy(deep=True))
            final_df["pagina"] = convert(final_df["pagina"].copy(deep=True))
            final_df["titulo_objeto"] =final_df.loc[final_df['titulo_objeto'].notnull(), 'titulo_objeto'] = "Sem informação"
            final_df["personagens"] =final_df.loc[final_df['personagens'].notnull(), 'personagens'] = "Sem informação"
            pbar.update(10)
            
            # transforma o dataframe em csv
            final_df.to_csv(path_dict["METADATA_PATH"],index=False)

            # exporta o mapa em HTML
            #pbar.set_description("Exportando Mapa...")
            #export.create_html(path_dict["METADATA_PATH"])
            #pbar.update(5)

            print ("Concluído")
    
    except Exception as e:

        print(str(e))


if __name__ == "__main__":
    main()
            
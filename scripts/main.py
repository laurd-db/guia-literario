import os
import geopandas as gpd
import pandas as pd
from tqdm import tqdm

import kmltocsv, maps


def main ():
    """
    Executa todas as funções
    """

    try:

        with tqdm(total=100) as pbar:

            # convertendo KML para CSV
            pbar.set_description("Convertendo dados geográficos...")
            kmltocsv.load_convert(os.environ["KML_PATH"],os.environ["LOC_PATH"])
            pbar.update(20)
            
            # cria um geodataframe das localizações
            pbar.set_description("Carregando coordenadas...")
            location_df = pd.read_csv(os.environ["LOC_PATH"]).rename(
                columns={"Name":"id","Latitude":"lat","Longitude":"lng"}
                )
            pbar.update(20)

            # cria um dataframe dos dados literários
            pbar.set_description("Carregando dados literários...")
            datalit_df = pd.read_excel(os.environ["LIT_PATH"]).astype(
                {"ano_objeto":object,"pagina":object}
                )
            pbar.update(20)

            # junta todos os dataframes parciais
            pbar.set_description("Atualizando metadados...")
            final_df = pd.merge(datalit_df,location_df, on=["id"], how="left")
            # converte valores float para int
            final_df["ano_objeto"] = final_df["ano_objeto"].astype(int)
            final_df["ano_obra"] = final_df["ano_obra"].astype(int)
            final_df["pagina"] = final_df["pagina"].astype(int)
            # preenche células vazias
            final_df["titulo_objeto"] =final_df.loc[final_df['titulo_objeto'].notnull(), 'titulo_objeto'] = "Sem informação"
            final_df["personagens"] =final_df.loc[final_df['personagens'].notnull(), 'personagens'] = "Sem informação"
            # transforma o dataframe em csv
            final_df.to_csv(os.environ["METADATA_PATH"],index=False)
            pbar.update(20)

            # cria index.html
            pbar.set_description("Criando mapa...")
            maps.load_map(os.environ["MAPBOX_KEY"])
            pbar.update(20)


            pbar.set_description("Concluído")
            pbar.close()
    
    except Exception as e:

        print(str(e))


if __name__ == "__main__":
    main()
            
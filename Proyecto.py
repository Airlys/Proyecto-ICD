import pandas as pd
import os
import json

def precios(carpeta):
    i=0
    restaurantes=[]
    for archivo in os.listdir(carpeta):
        if archivo.endswith('.json'):
            ruta_archivo = os.path.join(carpeta, archivo)
            i+=1
            with open(ruta_archivo, 'r') as f:
                data = json.load(f)
                for key, value in data["Restaurants"].items():
                    restaurantes.append(key)
                    df= pd.DataFrame(list(value["menu and prices"].items()))
                if i>1:
                    df_prueba=df.loc[df[0].isin(["Starters","Desserts","Main Dishes","Drinks"])].T
                    df_prueba.columns=df_prueba.iloc[0]
                    df_prueba=df_prueba[1:].reset_index(drop=True)
                    df_completo = pd.concat([df_completo,df_prueba], ignore_index=True)
                else:
                    df_completo =df.loc[df[0].isin(["Starters","Desserts","Main Dishes","Drinks"])].T.copy()
                    df_completo.columns=df_completo.iloc[0]
                    df_completo=df_completo[1:].reset_index(drop=True)
    return df_completo,restaurantes           
            
def minimo(json1):
    x=[]
    k=[]
    if json1==None:
        return None
    if type(json1)==float:
        return None
    for key, value in json1.items():
        try:
            x.append(int(value))
            k.append(key)
        except:
            continue
    if x==[]:
        return None
    minimo=min(x)
    articulo=k[x.index(minimo)]
    return [min(x),articulo]

def pastel(Restaurante_Disponibles,seleccionado):
    if seleccionado:
        df_seleccionado = Restaurante_Disponibles[Restaurante_Disponibles["Restaurants"]==seleccionado]
        if not df_seleccionado.empty:
            df_pastel = df_seleccionado.dropna(subset=["Opciones"])
            valor = df_pastel["Opciones"].explode().value_counts()
            return valor

        else:
             print(f"No se encontro datos de'{seleccionado}'.")
    else:
        print("No se ha introducido ningún restaurante")
        
def total(carpeta):
    i=0
    for archivo in os.listdir(carpeta):
        if archivo.endswith('.json'):
          i+=1 
    return i   

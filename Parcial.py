import pandas as pd
df = pd.read_csv('winequality-red.csv', sep=';')
df.head() 
print (df.head())

mediana_alcohol = df.alcohol.median()  
mediana_ph = df.pH.median()
mediana_sugar = df.residual_sugar.median()
mediana_acido = df.citric_acid.median()

class Calidad_vino:

    def metodo (self, mediana_arreglo, columna_arreglo):
        for i, arreglo in enumerate(columna_arreglo):
            if arreglo >= arreglo:
                df.loc[i, arreglo] = 'alto'
            else:
                df.loc[i, arreglo] = 'bajo'  
        return print (df.groupby(arreglo).quality.mean())
        

Invocar_Clase = Calidad_vino()
Invocar_Clase.metodo(mediana_alcohol, df.alcohol)
Invocar_Clase.metodo(mediana_ph, df.pH)
Invocar_Clase.metodo(mediana_sugar, df.residual_sugar)
Invocar_Clase.metodo(mediana_acido, df.citric_acid)
##############################################
#      Casos de covid cidades com UTFPR      #
#                                            #
# » Casos mensais                            #
# » Casos anuais                             #
# » Casos mensais em relação a população     #
# » Casos anuais em relação a população      #
# » Casos mensais de mortes                  #
# » Casos anuais  de mortes                  #
#                                            #
##############################################

import pandas as pd
import matplotlib.pyplot as plt

# Filtrar e salvar apenas as cidades que possue UTFPR com csv no formato UTF8
archive = pd.read_csv('casos.csv')
archive.query('city == "Apucarana" | city == "Campo Mourão" | city == "Cornélio Procópio" | '
                'city == "Curitiba" | city == "Dois vizinhos" | city == "Fracisco Bentrão" | '
                'city == "Guarapuava" | city == "Londrina" | city == "Medianeira" | '
                'city == "Pato Branco" | city == "Ponta Grossa" | city == "Santa Helena" | '
                'city == "Toledo" ').to_csv('UTFPR.csv', encoding='utf-8', index=False)

# Filtrar por meses por ano
# cidadesUTF = pd.read_csv('UTFPR.csv')
# df = pd.DataFrame(cidadesUTF)
# cidadesUTF=(df['date'] >= '2020-01-01') & (df['date'] <= '2020-01-31').to_csv('mensais.csv', encoding='utf-8', index=False)
# df_filtrado = df[cidadesUTF]


# Gera um plot dos casos mensais de casos de covid
cidadesUTF = pd.read_csv('UTFPR.csv')
df = pd.DataFrame(cidadesUTF)
data = cidadesUTF.iloc[:, 2].values
# data =  
print(data)


# plt.figure(figsize=(8, 6))
# plt.plot(cidadesUTF['last_available_date'], cidadesUTF['GNP'])
# plt.xlabel('Year')
# plt.ylabel('GNP')
# plt.title('Casos de COVID mensais')
# plt.savefig('caso-de-covid-mensais-2020.png')

# plt.close()



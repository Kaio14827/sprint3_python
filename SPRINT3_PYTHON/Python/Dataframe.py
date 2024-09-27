import pandas as pd
import matplotlib.pyplot as plt

# Tuplas com os dados dos pilotos, modelo dos carros e velocidade.
dados = (
    ("Antonio Felix da Costa", "TAG HEUER PORSCHE", 383),
    ("Nick Cassidy", "JAGUAR TCS RACING", 370),
    ("Oliver Rowland", "NISSAN", 320),
    ("Pascal Wehrlein", "TAG HEUER PORSCHE", 375),
    ("Jake Dennis", "ANDRETTI", 365),
    ("Mitch Evans", "JAGUAR TCS RACING", 368),
    ("Jehan Daruvala", "MASERATI MSG RACING", 300),
    ("Taylor Barnard", "NEOM MCLAREN", 360),
    ("Joel Eriksson", "ENVISION RACING", 355),
    ("Jean-Éric Vergne", "DS Techeetah", 362),
    ("Lucas Di Grassi", "ABT CUPRA", 340),
    ("Jake Hughes", "NEOM MCLAREN", 350),
    ("Sérgio Sette Câmara", "ERT", 330),
    ("Paul Aron", "ENVISION RACING", 325),
    ("Kevin Van Der Linde", "ABT CUPRA", 335),
    ("Edoardo Mortara", "MAHINDRA RACING", 345),
    ("Dan Ticktum", "ERT FORMULA", 328),
    ("Jordan King", "MAHINDRA RACING", 342),
    ("Norman Nato", "ANDRETTI", 348),
    ("Stoffel Vandoorne", "DS PENSKE", 380)
)

# Criando um DataFrame a partir das tuplas
df = pd.DataFrame(dados, columns=["Piloto", "Modelo", "Velocidade"])

# Definindo as condições para a pontuação
bins = [0, 320, 350, 370, 400]
labels = [0, 1, 2, 3]
df['Pontuação'] = pd.cut(df['Velocidade'], bins=bins, labels=labels, right=False)

print(df)

# Função para calcular a média das velocidades
def calcular_media_velocidade(dataframe):
    media_velocidade = dataframe["Velocidade"].mean()
    return media_velocidade

# Usando a função
media = calcular_media_velocidade(df)
print(f"A média das velocidades dos pilotos é: {media:.2f} km/h")



#Função para filtrar Pilotos por Pontuação
def filtrar_pilotos_por_pontuacao(dataframe, pontuacao):
    return dataframe[dataframe['Pontuação'] == pontuacao]

# Exemplo de uso:
pilotos_pontuacao_3 = filtrar_pilotos_por_pontuacao(df, 3)
print(pilotos_pontuacao_3)


df_sorted = df.sort_values(by="Velocidade", ascending=False)
print(df_sorted)

df['Classificação'] = df['Velocidade'].rank(ascending=False)
print(df)

#Gerar estatísticas (Máxima, Mínima, Mediana e Desvio Padrão)
velocidade_max = df['Velocidade'].max()
velocidade_min = df['Velocidade'].min()
velocidade_mediana = df['Velocidade'].median()
velocidade_std = df['Velocidade'].std()

print(f"Velocidade Máxima: {velocidade_max} km/h")
print(f"Velocidade Mínima: {velocidade_min} km/h")
print(f"Velocidade Mediana: {velocidade_mediana} km/h")
print(f"Desvio Padrão das Velocidades: {velocidade_std:.2f} km/h")

#Visualizar dados com gráficos
plt.figure(figsize=(10, 6))
plt.bar(df['Piloto'], df['Velocidade'], color='blue')
plt.xlabel('Piloto')
plt.ylabel('Velocidade (km/h)')
plt.title('Velocidade dos Pilotos')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

#Faixa de cores para velocidade
df.style.background_gradient(subset=['Velocidade'], cmap='Blues')

#Ranking de pilotos por pontuação
df['Ranking'] = df['Pontuação'].astype(int) * df['Velocidade']
df = df.sort_values(by='Ranking', ascending=False)
print(df)

#Função para Verificar a performance dos Pilotos
def verificar_performance(piloto, velocidade):
    if velocidade > 370:
        print(f"{piloto} está entre os mais rápidos, com {velocidade} km/h!")
    elif velocidade < 330:
        print(f"{piloto} pode melhorar a performance, com apenas {velocidade} km/h.")
    else:
        print(f"{piloto} está com uma boa velocidade de {velocidade} km/h.")

# Aplicar a função a cada piloto
for index, row in df.iterrows():
    verificar_performance(row['Piloto'], row['Velocidade'])

#Função para classificar pilotos em grupos de performance
def classificar_piloto(velocidade):
    if velocidade > 370:
        return "Excelente"
    elif 350 <= velocidade <= 370:
        return "Bom"
    elif 330 <= velocidade < 350:
        return "Regular"
    else:
        return "Baixo desempenho"

df['Categoria'] = df['Velocidade'].apply(classificar_piloto)
print(df)

#Função para destacar o melhores e piores pilotos
def destacar_pilotos(dataframe):
    velocidade_max = dataframe['Velocidade'].max()
    velocidade_min = dataframe['Velocidade'].min()
    
    for index, row in dataframe.iterrows():
        if row['Velocidade'] == velocidade_max:
            print(f"{row['Piloto']} é o mais rápido com {velocidade_max} km/h.")
        elif row['Velocidade'] == velocidade_min:
            print(f"{row['Piloto']} é o mais lento com {velocidade_min} km/h.")

destacar_pilotos(df)

#Função para recomendar piloto de acordo com a pontuação
def recomendacao_piloto(dataframe):
    for index, row in dataframe.iterrows():
        if row['Velocidade'] > 370:
            print(f"Parabéns, {row['Piloto']}! Continue assim!")
        elif row['Velocidade'] < 330:
            print(f"{row['Piloto']}, recomendamos revisar o setup do carro.")
        else:
            print(f"{row['Piloto']} está indo bem, mas pode melhorar.")

recomendacao_piloto(df)

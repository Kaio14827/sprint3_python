import pandas as pd
import matplotlib.pyplot as plt
import random

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

#Função para verificar a performance dos Pilotos
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



class Driver:
    def __init__(self, name, team):
        self.name = name
        self.team = team
        self.points = 0

    def add_points(self, points):
        self.points += points

# Criando os pilotos
driver1 = Driver("Antonio Felix da Costa", "TAG HEUER PORSCHE")
driver2 = Driver("Nick Cassidy", "JAGUAR TCS RACING")
driver3 = Driver("Oliver Rowland", "NISSAN")
driver4 = Driver("Pascal Werhlein", "TAG HEUER PORSCHE")
driver5 = Driver("Jake Dennis", "ANDRETTI")
driver6 = Driver("Mitch Evans", "JAGUAR TCS RACING")
driver7 = Driver("Jehan Daruvala", "MASERATI MSG RACING")
driver8 = Driver("Taylor Barnard", "NEOM MCLAREN")
driver9 = Driver("Joel Eriksson", "ENVISION RACING")
driver10 = Driver("Jean-Éric Vergne", "DS Techeetah")
driver11 = Driver("Lucas Di-Grassi", "ABT CUPRA")
driver12 = Driver("Jake Hughes", "NEOM MCLAREN")
driver13 = Driver("Sérgio Sette Câmara", "ERT")
driver14 = Driver("Paul Aron", "ENVISION RACING")
driver15 = Driver("Kevin Van Der Linde", "ABT CUPRA")
driver16 = Driver("Edoardo Mortara", "MAHINDRA RACING")
driver17 = Driver("Dan Ticktum", "ERT FORMULA")
driver18 = Driver("Jordan King", "MAHINDRA RACING")
driver19 = Driver("Norman Nato", "ANDRETTI")
driver20 = Driver("Stoffel Vandoorne", "DS PENSKE")

# Lista dos pilotos
drivers = [driver1, driver2, driver3, driver4, driver5, driver6, driver7, driver8, driver9, driver10
           , driver11, driver12, driver13, driver14, driver15, driver16, driver17, driver18, driver19,
           driver20]

# Simulando a corrida
def simulate_race():
    results = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
               11, 12, 13, 14, 15, 16, 17, 18,
               19, 20]  # resultado da corrida e como eles foram
    random.shuffle(results)  # deixando os resultados aleatórios
    return results

# Pontuação dos corredores em base nos seus numeros
def assign_points(results):
    for position, index in enumerate(results):
        if position == 0:
            drivers[index - 1].add_points(25)  # Primeiro
        elif position == 1:
            drivers[index - 1].add_points(18)  # Segundo
        elif position == 2:
            drivers[index - 1].add_points(15)  # Terceiro
        elif position == 3:
            drivers[index - 1].add_points(12) # Quarto
        elif position == 4:
            drivers[index - 1].add_points(10) # Quinto
        elif position == 5:
            drivers[index - 1].add_points(8) # Sexto
        elif position == 6:
            drivers[index - 1].add_points(6) # Setimo
        elif position == 7:
            drivers[index - 1].add_points(4) # Oitavo
        elif position == 8:
            drivers[index - 1].add_points(2) # Nono
        elif position == 9:
            drivers[index - 1].add_points(1) # Decimo
        elif position == 10:
            drivers[index - 1].add_points(0) # Decimo Primeiro
        elif position == 11:
            drivers[index - 1].add_points(0) # Decimo Segundo
        elif position == 12:
            drivers[index - 1].add_points(0) # Decimo terceiro
        elif position == 13:
            drivers[index - 1].add_points(0) # Decimo Quarto
        elif position == 14:
            drivers[index - 1].add_points(0) # Decimo Quinto
        elif position == 15:
            drivers[index - 1].add_points(0) # Decimo Sexto
        elif position == 16:
            drivers[index - 1].add_points(0) # Decimo setimo
        elif position == 17:
            drivers[index - 1].add_points(0) # Decimo oitavo
        elif position == 18:
            drivers[index - 1].add_points(0) # Decimo Nono
        elif position == 19:
            drivers[index - 1].add_points(0) # Vigesimo

# Simulação da corrida
race_results = simulate_race()

# Pontuação dos pilotos
assign_points(race_results)

# Organizando com a pontuação
drivers.sort(key=lambda x: x.points, reverse=True)

# Tabela no fim da corrida
print("Formula E Championship Standings after the race:")
print("{:<20} {:<20} {:<10}".format("Driver", "Team", "Points"))
for driver in drivers:
    print("{:<20} {:<20} {:<10}".format(driver.name, driver.team, driver.points))
import random

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
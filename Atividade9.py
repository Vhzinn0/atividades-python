def ler_tempo():
    tempo = float(input("Informe o tempo gasto na viagem (em horas): "))
    return tempo

def ler_velocidade_media():
    velocidade_media = float(input("Informe a velocidade média durante a viagem (em Km/h): "))
    return velocidade_media

def calcular_distancia(tempo, velocidade_media):
    distancia = tempo * velocidade_media
    return distancia

def calcular_litros_gastos(distancia):
    litros_gastos = distancia / 12
    return litros_gastos

def exibir_resultado(litros_gastos):
    print("A quantidade de litros de combustível gastos foi de: ", round(litros_gastos, 2), "litros")

tempo = ler_tempo()
velocidade_media = ler_velocidade_media()
distancia = calcular_distancia(tempo, velocidade_media)
litros_gastos = calcular_litros_gastos(distancia)
exibir_resultado(litros_gastos)

def apresentar_resultado(tempo, velocidade_media, distancia, litros_gastos):
    print("Tempo gasto na viagem:", tempo, "horas")
    print("Velocidade média durante a viagem:", velocidade_media, "Km/h")
    print("Distância percorrida:", distancia, "Km")
    print("Quantidade de litros de combustível gastos:", round(litros_gastos, 2), "litros")

def main():
    tempo = ler_tempo()
    velocidade_media = ler_velocidade_media()
    distancia = calcular_distancia(tempo, velocidade_media)
    litros_gastos = calcular_litros_gastos(distancia)
    apresentar_resultado(tempo, velocidade_media, distancia, litros_gastos)

if __name__ == "__main__":
    main()

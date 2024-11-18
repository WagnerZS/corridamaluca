def geraDicionarioCarros(xVermelho, xAmarelo, xAzul):
    dicCarros = {"Vermelho": xVermelho, "Amarelo": xAmarelo, "Azul": xAzul}
    dicCarros = dict(sorted(dicCarros.items(), key=lambda item: item[1], reverse=True))
    return dicCarros

def getPrimeiroCarro(dicCarros):
    return list(dicCarros.items())[0]

def getSegundoCarro(dicCarros):
    return list(dicCarros.items())[1]

def getTerceiroCarro(dicCarros):
    return list(dicCarros.items())[2]


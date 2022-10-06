def Polegadas():
  cm = float(input("Digite o valor em centímetros: "))
  pole = cm * 0.39370
  file = open('Valores.txt','w+')
  file.write(f'O valor {cm} em centímetros corresponde a {pole} valor em polegadas.')
  
pontuacao = 0

print('Bem-Vindo ao Jogo das Perguntas')

#Primeira pergunta
resposta = input('Qual a capital da França? ')
if resposta.lower() == 'paris':
    print("Correto!")
    pontuacao += 1
else:
    print("Errado!")

#Segunda pergunta

resposta = input('Qual o maior planeta do sistema solar? ')
if resposta.lower() == 'jupiter' or resposta.lower() == 'júpiter':
    print("Correto!")
    pontuacao += 1
else:
    print("Errado!")

#Terceira pergunta
resposta = input('Quanto é 5 + 5? ')
if resposta.lower() == '10':
    print("Correto!")
    pontuacao += 1
else:
    print("Errado!")

print(f"Sua pontuacao final é: {pontuacao} de 3 perguntas")
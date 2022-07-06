import random # Importando o comando RANDOM para gerar um número aleatório
from datetime import date # Importando o DATETIME para saber a data de hoje

# O menu principal, é definido (def) primeiro para poder chamar as outras funções do programa
def main():
    apresenta()

# Esse vai ser a função para reconhecer recolher os dados do usuário
def apresenta():
    print("Olá, vamos nos conhecer?") #Apresentação do programa

    nome = input("Qual o seu nome? ") #Recolhe o nome do usuário

    print ("\nOi {}, prazer em te conhecer!".format(nome)) #Frase com o nome do usuário

    #Campo para descobrir se o aniversariante é maior ou menor de 18 anos
    ano_nascimento = int(input("Que ano você nasceu? "))
    ano_atual = date.today().year # Datetime para saber o ano atual
    idade = ano_atual - ano_nascimento
	
    print(f'Que legal {nome}, você tem {idade} anos!')
    
    # Chama a função para conferir idade, que precisa dos parâmetros nome e idade
    checar_idade(nome,idade)

    # Envia para outras funções os parâmetros de nome e idade
    return nome,idade
    
# Função para checar idade, se for mais de 18 anos continua no jogo, se não encerra
def checar_idade(nome,idade):
    
    if idade >= 18:
        chamada_jogo(nome)
    else:
        despedida(nome)

# Função que pergunta se o usuário quer continuar o jogo
def chamada_jogo(nome):
    
    # Resposta com SIM ou NÃO
    # .lower() vai transformar a resposta em letra minuscula
    resposta = input(f'\n{nome}. Você me ajuda a testar um jogo? Responda Sim ou Não: ').lower()

    if resposta == 'não' or  resposta == 'nao':
        despedida(nome)
    
    elif resposta == 'sim':
        jogo(nome)

    else:
        print('Por favor, digite SIM ou NÃO')
        chamada_jogo(nome)

# Função que joga
def jogo(nome):
    
        # Gera um número aleatório entre 1 e 9
        numero = random.randint(1,9)

        print('\nVou escolher um número, tente acertar qual é!')
        chute = int(input(f'\n{nome}, escolha um número entre 1 e 9: '))
        
        if chute <=0 or chute >9:
            print(f'{nome}, escolhe um número entre \033[1m1 e 9 apenas\033[m')
            jogo(nome)

        elif chute == numero:
            print(f'Parabéns {nome}! Você acertou de primeira.')
            despedida(nome)

        else:
            print('Não foi esse número que eu escolhi. Vou te dar mais 3 tentativas')            
            tentativa = 1
            
            while tentativa <= 3:
                chute=int(input('\nTente um outro número: '))
                
                if chute < numero:
                    print(f'O número {chute} é mais baixo do que o que eu escolhi')
                    
                
                if chute > numero:
                    print(f'O número {chute} é mais alto do que o que eu escolhi')

                if chute == numero:
                    print ('\033[1mParabéns! Você acertou :D\033[m')
                    despedida(nome)
                    tentativa += 3
                        	
                tentativa += 1

            if tentativa > 4 and chute != numero:
                print(f'Acabaram as tentativas. O número era {numero}')
                print('\nQuem sabe na proxima vez, não é?')
                despedida(nome)
                	
def despedida(nome):
    print(f'\nFoi um prazer te conhecer {nome}. Nos vemos na próxima!')

main()

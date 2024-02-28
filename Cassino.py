import random
import emoji
# Define variaveis.
inicial = 0
vermelho = []
preto = []
normal = '\033[m'
saldo = 0
cont = 0
# Inicio de jogo
print(emoji.emojize('''
BEM VINDO AO CASSINO JOKER :joker:
AQUI TEMOS VARIAS OPÇÕES DE JOGOS!
[1] ROLETA
[2] ROLETA SOVIETICA (o nome roleta russa foi proibido por lei :crying_face:)
[3] TIGRINHO DO J** V****
'''))
jogo = int(input('- E ai meu vencedor, qual o jogo de hoje? [Digite apenas o número]: '))
if jogo == 1:
    print('{:-^20}'.format('ROLETA'))
    print(f'''
O JOGO FUNCIONA DE FORMA SIMPLES
- VOCÊ ESCOLHE QUAL O SEU VALOR INICIAL ENTRE 100 E 1000 REAIS!
- O JOGO INICIA E VOCÊ ESCOLHE A MODALIDADE QUE VAI APOSTAR
- VOCÊ GANHA SE O VALOR SORTEADO FOR O SEU ESCOLHIDO VOCÊ GANHA!

AQUI ESTÃO OS NUMEROS:''')
    # printa os numeros na cor certa
    for c in range(0, 37):
        if c == 0:
            print(c, end='')
        elif c in [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]:
            vermelho.append(c)
            print('\033[31m', c, end='')
        else:
            print('\033[30m', c, end='')
            preto.append(c)
    print('\033[m')
    print('''
    POR FIM É SÓ APOSTAR E LUCRAR PORQUE TÁ PAGANDO MUITO!
[1] IMPAR OU PAR
[2] VERMELHO OU PRETO
[3] NUMERO ESPECIFICO''')
    # Codigo da roleta
    while True:
        cont += 1
        print('-=' * 20)
        modalidade = input('Em qual modalidade você quer jogar?[1/2/3]').strip()
        if cont == 1:
            inicial = int(input('Qual o valor inicial: '))
            if inicial > 1000:
                print('Valor maior que o limite, arredondado para 1000!')
                inicial = saldo = 1000
            elif inicial < 100:
                print('Valor menos que o minimo, arredondado para 100!')
                inicial = saldo = 100
            else:
                saldo = inicial
                print(f'Valor aceito! {saldo} adicionado a sua carteira!')
        match modalidade:
            case '1':
                numpc = random.randint(0, 36)
                print('-=' * 20)
                print('INICIANDO IMPAR OU PAR')
                escjog = input('PAR OU IMPAR? [P/I]').strip()
                aposta = int(input('Quanto você quer apostar?'))
                if aposta > saldo:
                    print(f'você não possui tanto dinheiro all in automatico de: {saldo}.')
                    aposta = saldo
                else:
                    print(f'apostando {aposta}')
                saldo -= aposta
                print(f'A ROLETA CAIU NO {numpc}')
                if numpc % 2 == 0 and escjog[0] in 'Pp' or numpc % 2 == 1 and escjog[0] in 'Ii':
                    saldo += aposta * 2
                    print(f'VOCÊ GANHOU {aposta * 2} E AGORA SEU SALDO É: {saldo}')
                else:
                    print(f'você perdeu {aposta} e seu saldo agora é de {saldo}')
                if saldo == 0:
                    print('')
                    break
            case '2':
                numpc = random.randint(0, 36)
                print('-=' * 20)
                print('INICIANDO VERMELHO OU PRETO')
                escjog = input('VERMELHO OU PRETO? [V/P]: ').strip()
                aposta = int(input('Quanto você quer apostar?'))
                if aposta > saldo:
                    print(f'você não possui tanto dinheiro all in automatico de: {saldo}.')
                    aposta = saldo
                else:
                    print(f'apostando {aposta}')
                saldo -= aposta
                print(f'A ROLETA CAIU NO {numpc}')
                if escjog[0] in 'Vv' and numpc in vermelho \
                        or escjog[0] in 'Pp' and numpc in preto:
                    saldo += aposta * 2
                    print(f'VOCÊ GANHOU {aposta * 2} E AGORA SEU SALDO É: {saldo}')
                else:
                    print(f'você perdeu {aposta} e seu saldo agora é de {saldo}')
                if saldo == 0:
                    print('')
                    break
            case '3':
                numpc = random.randint(0, 36)
                print('-=' * 20)
                print('INICIANDO ESCOLHA POR NUMERO!')
                escjog = int(input('QUAL O NUMERO? [1-36] '))
                if escjog > 36:
                    print('Numero fora do alcance, arredondado para 36!')
                    escjog = 36
                elif escjog < 1:
                    print('Numero fora do alcance, arredondado para 1')
                    escjog = 1
                aposta = int(input('Quanto você quer apostar?'))
                if aposta > saldo:
                    print(f'você não possui tanto dinheiro all in automatico de: {saldo}.')
                    aposta = saldo
                else:
                    print(f'apostando {aposta}')
                saldo -= aposta
                print(f'A ROLETA CAIU NO {numpc}')
                if escjog == numpc:
                    saldo += aposta * 36
                    print(f'VOCÊ GANHOU {aposta * 36} E AGORA SEU SALDO É: {saldo}')
                else:
                    print(f'você perdeu {aposta} e seu saldo agora é de {saldo}')
                if saldo == 0:
                    print('')
                    break

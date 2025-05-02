import numpy as np #pip3 install numpy
import random
import time
import matplotlib.pyplot as plt #pip3 install matplotlib
import matplotlib.backends.backend_tkagg as tkagg

Nomes = [
    "Dr. Eggman",
    "Sam, O Gato",
    "Irvine, O Rato",
    "Fortune, Grande Mestre Do Horizonte",
    "Marisa",
    "Reimu",
    "Morgana",
    "Red",
    "Pink",
    "Blue",
    "Bong-Bong",
    "Yesod, Sephiroth",
    "Netzach, Sephiroth",
    "Malkuth, Sephiroth",
    "Binah, Sephiroth",
    "Chesed, Sephiroth",
    "Angela, Bibliotecária Patrono",
    "Roland",
    "Kingaleppu",
    "Lucy, A Slime",
    "Artoria Pendagron",
    "Luana",
    "João P.",
    "João G.",
    "Tomé",
    "Renan",
    "Amanda",
    "Cecilia",
    "Gleristone",
    "Marcelino",
    "Feliciano",
    "Luciano",
    "Romulo",
    "Félix",
    "Pedro",
    "Paulistaaaaaaaaaaaaaaaa",
    "Jack Black",
    "Pablo",
    "Marciano",
    "Omni-Man"
]

itens = [
    "Metal Sonic",
    "Kit de Abrir Fechaduras",
    "Óculos Irado",
    "Pelúcia de Raposa Kitsune",
    "Mini Hakkero",
    "Gohei de 3 Metros",
    "Pente para Gatos",
    "Braço de um Boneco de Madeira",
    "Bandana Vermelha",
    "Braço de um Boneco de Madeira (Roubado)",
    "Mini Metralhadora",
    "Livro “Python para Iniciantes”",
    "Livro “Como Usar Ataques de Penetração 101”",
    "Livro “Botei Fogo no Meu Colega, e Agora?”",
    "Livro “História da Floresta Escura e os 3 Pássaros”",
    "Livro “Para os Viciados em Café”",
    "Miniatura de Biblioteca",
    "Livro “Como Lidar com a Morte da Minha Esposa”",
    "Mimicry",
    "Talismã com um Rosto Familiar",
    "Saber",
    "Enxada (Deluxe, Usada pelo Deus do Capino dos Lotes)",
    "Cópia Física de “Everhood 2”",
    "Manga “Call of the Night”",
    "Mangá “Jujutsu Kaizen 0”",
    "Partes de Carro",
    "Dicionário da Língua Espanhola",
    "Cópia Física de “A Night in the Woods”",
    "Coleção de Mangá da Série Jojo",
    "Cópia Física de “Anno Mutationem”",
    "10000 Jades Estelares",
    "Cópia Digital de “Terraria” (2000 Horas)",
    "Kit de Poker",
    "Bola de Futebol Assinada",
    "Kit de Chapéus",
    "Livro “Como Fazer Agachamento”",
    "Jockey de Galinha",
    "Doutorado",
    "Máquina de Contato Extraterrestre",
    "“Are You Sure?”"
]

precos = [
    15000,
    120,
    250,
    340,
    800,
    2000,
    90,
    130,
    100,
    300,
    1800,
    60,
    120,
    75,
    110,
    50,
    400,
    95,
    2000,
    600,
    1000,
    3500,
    300,
    45,
    60,
    800,
    70,
    250,
    900,
    220,
    10000,
    80,
    150,
    500,
    220,
    65,
    700,
    5000,
    15000,
    1
]

#array para decidir a venda das pessoas
produtosavenda = []
# variavel que calcula vendas diarias
valordiario = 0
#array que calcula o total de vendas de cada dia vendas 
vendadias = []
# dias rodados
dias = 1
# array de dias (Gráfico)
diaspassados = []

#Função que usa random para atribuir valores aléatorios na loja, podendo se repetir até 3 vezes
def adicionarprodutosnaloja():
    repet = random.randint(1,3)
    while repet > 0:
        nomesnaloja = random.randint(0,60)
        if nomesnaloja < len(Nomes):
            produtosnaloja = random.randint(0,len(itens) - 1)
            produtosavenda.append([Nomes[nomesnaloja], itens[produtosnaloja], precos[produtosnaloja]])
        repet -= 1

#menu
def WelcomeFolks():
    print('''

    Escolha uma opção:

    1. Vender Produto
    2. Comprar produto
    3. Interagir com {}
    4. Passar dia
    0. sair da loja por tempo indefinido

    '''.format(Vendedor))


#1. vender produto
def venderprodutos():
    continuarvendas = "0"
    while continuarvendas == "0":
        meuprodutoavender = input("Digite o nome do produto que você irá vender : ")
        meuprodutoavenderpreco = input("Digite o preço apropiado do produto que você vai vender : ")
        meuprodutoavenderpreco = int(meuprodutoavenderpreco)
        produtosavenda.append([ProtagonistaDaJornadaDeRevendas, meuprodutoavender, meuprodutoavenderpreco])

        continuarvendas = input("Deseja continuar vendendo outros produtos? 0 - Sim / 1 - Não : ")
        if continuarvendas == "0":
            pass
        else:
            break

# primeira linha de dialógo
trabalhoseu = ["Como anda o trabalho?","Por qual razão você veio trabalhar aqui?"]
trabalhodele = ["Está indo bem. Sou apenas uma alma desesperada trabalhando nesse fim de mundo.", "O fim está proximo."]

# segunda linha de dialógo
agradecerseu = ["Muito obrigado por estar ao meu lado.","Irei sentir sua falta.","Colega, obrigado pela ajuda", "O fim está próximo, se sofrimento irá acabar."]
agradecerdele = ["Só estou fazendo meu trabalho.", "...", "Você me traz esperanças fátuas", "..."]

# terceira linha de dialógo
complimentoseu = ["apenas não.", "..."]
complimentodele = ["Obrigado.", "... :3"]

# Quarta linha de dialógo
geralseu = ["Sua Opinião na morte?", "qual sua opinião no jogo de ontem?", "Cuzcuz paulista é bom?"]
geraldele = ["Todos morremos, é apenas questão de tempo.", "Eu não saio dessa maldita loja, eu não tenho tempo para jogos imbecis.", "Fale isso denovo e eu deleto o system32."]

# Quinta linha de dialógo
lebronseu = "LEBRON O GOAT!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
lebrondele = "LEBRON O GOAT!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"

#3. Interação
def interação():
    print('''Selecione uma linha de dialogo :
1. Perguntar sobre o Trabalho
2. agradecer pelo acompanhamento
3. complimentar aparencia
4. Falar sobre tópicos gerais
5. Falar sobre como o lebron james é o GOAT!!!!!!!!!!!!!!!!!!!!
''')
    dialogo = input("Digite uma linha de dialogo : ")
    dialogo = int(dialogo)
    if dialogo == 1:
        selecionardialogo = random.randint(0, len(trabalhoseu) - 1)
        print("{} : ".format(ProtagonistaDaJornadaDeRevendas), trabalhoseu[selecionardialogo])
        time.sleep(2)
        print("{} : ".format(Vendedor), trabalhodele[selecionardialogo])
        time.sleep(2)
    elif dialogo == 2:
        selecionardialogo = random.randint(0, len(agradecerseu) - 1)
        print("{} : ".format(ProtagonistaDaJornadaDeRevendas), agradecerseu[selecionardialogo])
        time.sleep(2)
        print("{} : ".format(Vendedor), agradecerdele[selecionardialogo])
        time.sleep(2)
    if dialogo == 3:
        selecionardialogo = random.randint(0, len(complimentoseu) - 1)
        print("{} : ".format(ProtagonistaDaJornadaDeRevendas), complimentoseu[selecionardialogo])
        time.sleep(2)
        print("{} : ".format(Vendedor), complimentodele[selecionardialogo])
        time.sleep(2)
    if dialogo == 4:
        selecionardialogo = random.randint(0, len(geralseu) - 1)
        print("{} : ".format(ProtagonistaDaJornadaDeRevendas), geralseu[selecionardialogo])
        time.sleep(2)
        print("{} : ".format(Vendedor), geraldele[selecionardialogo])
        time.sleep(2)
    if dialogo == 5:
        print("{} : ".format(ProtagonistaDaJornadaDeRevendas), lebronseu)
        time.sleep(2)
        print("{} : ".format(Vendedor), lebrondele)
        time.sleep(2)
    else:
        pass


#4. Função que calcula o fim do dia
def Fimdedia():
    global valordiario, dias
# calcula a renda diaria
    for k in produtosavenda:
        valordiario += k[2]
#
    resumo = np.array(produtosavenda)
    print('''#
#''')
    print('Relátorio do que foi vendido hoje (dia {}) : \n {}'.format(dias, resumo))

#envia o valor das vendas diarias 
    vendadias.append(valordiario)
# zera o valor diario
    valordiario = 0
# array de dias
    diaspassados.append(dias)


    if dias == 1:
        print("Gráfico não dísponivel")
    else:
        # Criação do gráfico
        # primeiro array = Y no gráfico, segundo array = X no gráfico
        # obs, o primeiro e segundo array devem ter o a mesma quantidade de valores
        plt.plot(diaspassados ,  vendadias)

        #Acessando a janela Tkinter
        # pega a atual figura
        fig = plt.gcf()
        # chama o canvas
        canvas = fig.canvas

        # Alterando o título da janela usando o canvas
        canvas.manager.window.title("resumo diário")
        # Mostra o gráfico
        plt.show()

    del produtosavenda[:]

        # para rodar o código dennovo feche a janela do gráfico atual.
    # dias passados
    dias += 1

 

#Função que pergunta se o nome está certo
def nome_certo(nomecorreto):
    nomecerto = "0"
    while nomecerto == "0":
        print("{} : Seu nome é {} , está correto?".format(Vendedor, nomecorreto))
        time.sleep(2)
        nomecerto = input("(Sim - 1 / Não - 0) : ")
        if nomecerto == "0":
            time.sleep(2)
            nomecorreto = input("Digite o seu nome : ")
            time.sleep(2)
        else:
            break








Vendedor = "David, Filho de Edwin"
print("??? : Seja bem vido a loja de revenda 'LCB Workshop' Sou o trabalhador que irá lhe acompanhar meu nome é {} , será um prazer lhe ajudar.".format(Vendedor))
time.sleep(2)
print("{} : Para começar a vender, ou comprar, porfavor insira seu nome.".format(Vendedor))
time.sleep(2)
ProtagonistaDaJornadaDeRevendas = input("Digite seu nome : ")
time.sleep(2)
nome_certo(ProtagonistaDaJornadaDeRevendas)
time.sleep(2)
print("{} : O menu da loja irá abrir, vendemos várias coisas, exceto coisas orgânicas. Boa sorte.".format(Vendedor))
 

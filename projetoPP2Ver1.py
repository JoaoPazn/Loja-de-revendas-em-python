import numpy as np #pip3 install numpy
import random
import time
import matplotlib.pyplot as plt #pip3 install matplotlib
import matplotlib.backends.backend_tkagg as tkagg



# # Criação do gráfico
# plt.plot([1, 2, 10], [1, 4, 3,])

# # Acessando a janela Tkinter
# fig = plt.gcf()
# canvas = fig.canvas

# # Alterando o título da janela
# canvas.manager.window.title("Minha Janela de Gráfico")

# # Mostrar o gráfico
# plt.show()


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

#Função que usa random para atribuir valores aléatorios na loja, podendo se repetir até 3 vezes
def adicionarprodutosnaloja():
    repet = random.randint(1,4)
    while repet > 0:
        nomesnaloja = random.randint(0,80)
        if nomesnaloja < len(Nomes):
            produtosnaloja = random.randint(0,len(itens) - 1)
            produtosavenda.append([Nomes[nomesnaloja], itens[produtosnaloja], precos[produtosnaloja]])
        repet -= 1

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

#menu
def WelcomeFolks():
    print('''

    Escolha uma opção:

    1. Vender Produto
    2. Comprar prroduto
    3. Interagir com {}
    4. Perguntar Sobre Meta diária da loja
    5. Passar dia
    0. sair da loja por tempo indefinido

    '''.format(Vendedor))


# #1. vender produto
# def venderprodutos():
#    meuprodutoavender 







Vendedor = "David, Filho de Edwin"
print("??? : Seja bem vido a loja de revenda 'Lobotomy Workshop' Sou o trabalhador que irá lhe acompanhar meu nome é {} , será um prazer lhe ajudar.".format(Vendedor))
time.sleep(2)
print("{} : Para começar a vender, ou comprar, porfavor insira seu nome.".format(Vendedor))
time.sleep(2)
ProtagonistaDaJornadaDeRevendas = input("Digite seu nome : ")
nome_certo(ProtagonistaDaJornadaDeRevendas)
time.sleep(2)
print("{} : O menu da loja irá abrir, vendemos várias coisas, exceto coisas orgânicas".format(Vendedor))
 

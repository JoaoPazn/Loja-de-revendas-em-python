import numpy as np #pip3 install numpy
import random
import time
import matplotlib.pyplot as plt #pip3 install matplotlib
import matplotlib.backends.backend_tkagg as tkagg
import json
from PIL import Image
from PIL import features
from tkinter import Tk, Label
from PIL import Image, ImageTk

# Carregar o arquivo JSON
with open('Nomes.json', 'r', encoding='utf-8') as N:
    data = json.load(N)

# Acessar a lista de nomes
Nomes = data["Nomes"]

# Carregar o arquivo JSON
with open('itens.json', 'r', encoding='utf-8') as I:
    data = json.load(I)

# Acessar a lista de nomes
itens = data["itens"]

# Carregar o arquivo JSON
with open('preco.json', 'r', encoding='utf-8') as P:
    data = json.load(P)

# Acessar a lista de nomes
precos = data["precos"]



#array para armazenar a venda das pessoas
produtosavenda = []
# Armazenamento de itens que o ProtagonistaDaJornadaDeRevendas irá comprar
inventario = []
# inventario vendas (usado junto de produtos vendas)
iventariopravendasapenas = []
# variavel que calcula vendas diarias
valordiario = 0
#array que calcula o total de vendas de cada dia vendas 
vendadias = []
# dias rodados
dias = 1
# array de dias (Gráfico)
diaspassados = []

#Função que usa random para atribuir valores aléatorios na loja, podendo se repetir até 3 vezes
# .5 Passar tempo
def adicionarprodutosnaloja():
    repet = random.randint(1,3)
    while repet > 0:
        nomesnaloja = random.randint(0,60)
        if nomesnaloja < len(Nomes):
            produtosnaloja = random.randint(0,len(itens) - 1)
            produtosavenda.append([Nomes[nomesnaloja], itens[produtosnaloja], precos[produtosnaloja]])
            print("Novo item na loja! \n")
        repet -= 1
    
    
#menu
def WelcomeFolks():
    print('''Escolha uma opção:

    1. Comprar Produto
    2. Vender produto
    3. Interagir com {}
    4. Passar dia
    5. Esperar Novos itens serem estockados
    6. Observar inventario
    7. Atualizar nome
    0. sair da loja por tempo indefinido

    '''.format(Vendedor))


#1. vender produto
def venderprodutos():
    continuarvendas = "1"
    while continuarvendas == "1":
        meuprodutoavender = input("Digite o nome do produto que você irá vender : ")
        
        while True:
            meuprodutoavenderpreco = input("Digite o preço apropriado do produto que você vai vender: ")
            try:
                meuprodutoavenderpreco = int(meuprodutoavenderpreco)
                iventariopravendasapenas.append([ProtagonistaDaJornadaDeRevendas, meuprodutoavender, meuprodutoavenderpreco])
                break  
            except ValueError:
                print("Por favor, digite um valor numérico válido para o preço.")
        

        continuarvendas = input("Deseja continuar vendendo outros produtos? 1 - Sim / 0 - Não : ")
        if continuarvendas == "1":
            pass
        else:
            break

#2. comprar Produto
def comprarprodutos():
    global iventariopravendasapenas, produtosavenda, iventario
    comprarmais = "1"
    if produtosavenda == []:
        print("Nada a vender por enquanto")
        comprarmais = "0" 
    while comprarmais == "1":
        estoque = np.array(produtosavenda)
        
        comprarmais = input("Você REALMENTE deseja comprar Algo? 1 - Sim / 0 - Não : ")
        if comprarmais == "1":  
            print('''#
#''')
            print('Produtos em estoque atualmente :')
            for idx, item in enumerate(estoque, 1):
                print(f"{idx}. {item}")
            print('''#''') 
            selec = input("selecione o item que você irá comprar : ")
            selec = int(selec)
            selec -= 1
            if selec < len(produtosavenda):
                iventariopravendasapenas.append(produtosavenda[selec])
                inventario.append(produtosavenda[selec][1])
                del produtosavenda[selec]
                print("Produto comprado!")
            else:
                print("Produto Inexistente")
        else:
            pass




# primeira linha de dialógo
trabalhoseu = ["Como anda o trabalho?","Por qual razão você veio trabalhar aqui?","Qual sua relação com o chefe?"]
trabalhodele = ["Está indo bem. Sou apenas uma alma desesperada trabalhando nesse fim de mundo.", "O fim está proximo.","Lulu Suricato? Ele foi um colega de turma."]

# segunda linha de dialógo
agradecerseu = ["Muito obrigado por estar ao meu lado.","Irei sentir sua falta.","Colega, obrigado pela ajuda", "O fim está próximo, se sofrimento irá acabar."]
agradecerdele = ["Só estou fazendo meu trabalho.", "...", "Você me traz esperanças fátuas", "..."]

# terceira linha de dialógo
complimentoseu = ["apenas não.", "..."]
complimentodele = ["Obrigado.", "..."]

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
    global valordiario, dias, produtosavenda, iventariopravendasapenas
# calcula a renda diaria
    produtosavenda = iventariopravendasapenas + produtosavenda
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
    del iventariopravendasapenas[:]
        # para rodar o código dennovo feche a janela do gráfico atual.
    # dias passados
    dias += 1

# .6 Observar itens 
def observearitens():
    contobserve = "1"
    while contobserve == "1":
        iventario1 = np.array(inventario)
        print("Itens disponíveis para observar:")
        for idx, item in enumerate(iventario1, 1):
            print(f"{idx}. {item}")
        
        while True:
            try:
                abririmg = input("Selecione a imagem que você gostaria de observar: ")
                abririmg = int(abririmg)
                abririmg -= 1
                if abririmg < 0 or abririmg >= len(inventario):
                    raise IndexError
                break
            except ValueError:
                print("Entrada inválida.1 Por favor, digite um número.")
            except IndexError:
                print("Índice fora do intervalo. Tente novamente.")

        if inventario[abririmg] == "Metal Sonic":
            imagem = Image.open("img\Metal_Sonic.png")
            janela = Tk()
            janela.title("Metal Sonic")
            janela.geometry(f"{imagem.width}x{imagem.height}")
            imagem_tk = ImageTk.PhotoImage(imagem)
            label = Label(janela, image=imagem_tk)
            label.pack()
            janela.mainloop()

        elif inventario[abririmg] == "Kit de Abrir Fechaduras":
            imagem = Image.open("img\Kit_Abrir_fechaduras.jpg")
            janela = Tk()
            janela.title("Kit de Abrir Fechaduras")
            janela.geometry(f"{imagem.width}x{imagem.height}")
            imagem_tk = ImageTk.PhotoImage(imagem)
            label = Label(janela, image=imagem_tk)
            label.pack()
            janela.mainloop()

        elif inventario[abririmg] == "Óculos Irado":
            imagem = Image.open("img\óculos_irado.png")
            janela = Tk()
            janela.title("Óculos Irado")
            janela.geometry(f"{imagem.width}x{imagem.height}")
            imagem_tk = ImageTk.PhotoImage(imagem)
            label = Label(janela, image=imagem_tk)
            label.pack()
            janela.mainloop()

        elif inventario[abririmg] == "Pelúcia de Raposa Kitsune":
            imagem = Image.open("img\pelucia_kitsune.png")
            janela = Tk()
            janela.title("Pelúcia de Raposa Kitsune")
            janela.geometry(f"{imagem.width}x{imagem.height}")
            imagem_tk = ImageTk.PhotoImage(imagem)
            label = Label(janela, image=imagem_tk)
            label.pack()
            janela.mainloop()

        elif inventario[abririmg] == "Mini Hakkero":
            imagem = Image.open("img\Mini_Hakkero.png")
            janela = Tk()
            janela.title("Mini Hakkero")
            janela.geometry(f"{imagem.width}x{imagem.height}")
            imagem_tk = ImageTk.PhotoImage(imagem)
            label = Label(janela, image=imagem_tk)
            label.pack()
            janela.mainloop()

        elif inventario[abririmg] == "Gohei de 3 Metros":
            imagem = Image.open("img\Gohei_3_metros.png")
            janela = Tk()
            janela.title("Gohei de 3 Metros")
            janela.geometry(f"{imagem.width}x{imagem.height}")
            imagem_tk = ImageTk.PhotoImage(imagem)
            label = Label(janela, image=imagem_tk)
            label.pack()
            janela.mainloop()

        elif inventario[abririmg] == "Pente para Gatos":
            imagem = Image.open("img\Pente_Gatos.webp")
            janela = Tk()
            janela.title("Pente para Gatos")
            janela.geometry(f"{imagem.width}x{imagem.height}")
            imagem_tk = ImageTk.PhotoImage(imagem)
            label = Label(janela, image=imagem_tk)
            label.pack()
            janela.mainloop()

        elif inventario[abririmg] == "Braço de um Boneco de Madeira":
            imagem = Image.open("img\Braco_Madeira.webp")
            janela = Tk()
            janela.title("Braço de um Boneco de Madeira")
            janela.geometry(f"{imagem.width}x{imagem.height}")
            imagem_tk = ImageTk.PhotoImage(imagem)
            label = Label(janela, image=imagem_tk)
            label.pack()
            janela.mainloop()

        elif inventario[abririmg] == "Bandana Vermelha":
            imagem = Image.open("img\Bandana_vermelha.png")
            janela = Tk()
            janela.title("Bandana Vermelha")
            janela.geometry(f"{imagem.width}x{imagem.height}")
            imagem_tk = ImageTk.PhotoImage(imagem)
            label = Label(janela, image=imagem_tk)
            label.pack()
            janela.mainloop()

        elif inventario[abririmg] == "Braço de um Boneco de Madeira (Roubado)":
            imagem = Image.open("img\Braco_Madeira.webp")
            janela = Tk()
            janela.title("Braço de um Boneco de Madeira (Roubado)")
            janela.geometry(f"{imagem.width}x{imagem.height}")
            imagem_tk = ImageTk.PhotoImage(imagem)
            label = Label(janela, image=imagem_tk)
            label.pack()
            janela.mainloop()

        elif inventario[abririmg] == "Mini Metralhadora":
            imagem = Image.open("img\Mini_Metralhadora.png")
            janela = Tk()
            janela.title("Mini Metralhadora")
            janela.geometry(f"{imagem.width}x{imagem.height}")
            imagem_tk = ImageTk.PhotoImage(imagem)
            label = Label(janela, image=imagem_tk)
            label.pack()
            janela.mainloop()

        elif inventario[abririmg] == "Livro “Python para Iniciantes”":
            imagem = Image.open("img\Python_Iniciantes.png")
            janela = Tk()
            janela.title("Livro “Python para Iniciantes”")
            janela.geometry(f"{imagem.width}x{imagem.height}")
            imagem_tk = ImageTk.PhotoImage(imagem)
            label = Label(janela, image=imagem_tk)
            label.pack()
            janela.mainloop()

        elif inventario[abririmg] == "Livro “Como Usar Ataques de Penetração 101”":
            imagem = Image.open("img\Ataques_Penetracao.png")
            janela = Tk()
            janela.title("Livro “Como Usar Ataques de Penetração 101”")
            janela.geometry(f"{imagem.width}x{imagem.height}")
            imagem_tk = ImageTk.PhotoImage(imagem)
            label = Label(janela, image=imagem_tk)
            label.pack()
            janela.mainloop()

        elif inventario[abririmg] == "Livro “Botei Fogo no Meu Colega, e Agora?”":
            imagem = Image.open("img\Botei_Fogo_no_meu_amigo.png")
            janela = Tk()
            janela.title("Livro “Botei Fogo no Meu Colega, e Agora?”")
            janela.geometry(f"{imagem.width}x{imagem.height}")
            imagem_tk = ImageTk.PhotoImage(imagem)
            label = Label(janela, image=imagem_tk)
            label.pack()
            janela.mainloop()

        elif inventario[abririmg] == "Livro “História da Floresta Escura e os 3 Pássaros”":
            imagem = Image.open("img\PASSAROS.png")
            janela = Tk()
            janela.title("Livro “História da Floresta Escura e os 3 Pássaros”")
            janela.geometry(f"{imagem.width}x{imagem.height}")
            imagem_tk = ImageTk.PhotoImage(imagem)
            label = Label(janela, image=imagem_tk)
            label.pack()
            janela.mainloop()

        elif inventario[abririmg] == "Livro “Para os Viciados em Café”":
            imagem = Image.open("img\Café_livro.png")
            janela = Tk()
            janela.title("Livro “Para os Viciados em Café”")
            janela.geometry(f"{imagem.width}x{imagem.height}")
            imagem_tk = ImageTk.PhotoImage(imagem)
            label = Label(janela, image=imagem_tk)
            label.pack()
            janela.mainloop()

        elif inventario[abririmg] == "Miniatura de Biblioteca":
            imagem = Image.open("img\Miniatura_biblioteca.png")
            janela = Tk()
            janela.title("Miniatura de Biblioteca")
            janela.geometry(f"{imagem.width}x{imagem.height}")
            imagem_tk = ImageTk.PhotoImage(imagem)
            label = Label(janela, image=imagem_tk)
            label.pack()
            janela.mainloop()

        elif inventario[abririmg] == "Livro “Como Lidar com a Morte da Minha Esposa”":
            imagem = Image.open("img\Como_Lidar_com_a_morte_da_esposa.png")
            janela = Tk()
            janela.title("Livro “Como Lidar com a Morte da Minha Esposa”")
            janela.geometry(f"{imagem.width}x{imagem.height}")
            imagem_tk = ImageTk.PhotoImage(imagem)
            label = Label(janela, image=imagem_tk)
            label.pack()
            janela.mainloop()

        elif inventario[abririmg] == "Mimicry":
            imagem = Image.open("img\mimicry.png")
            janela = Tk()
            janela.title("Mimicry")
            janela.geometry(f"{imagem.width}x{imagem.height}")
            imagem_tk = ImageTk.PhotoImage(imagem)
            label = Label(janela, image=imagem_tk)
            label.pack()
            janela.mainloop()

        elif inventario[abririmg] == "Talisma":
            imagem = Image.open("img\Talismã.png")
            janela = Tk()
            janela.title("Talismã com um Rosto Familiar")
            janela.geometry(f"{imagem.width}x{imagem.height}")
            imagem_tk = ImageTk.PhotoImage(imagem)
            label = Label(janela, image=imagem_tk)
            label.pack()
            janela.mainloop()

        elif inventario[abririmg] == "Saber":
            imagem = Image.open("img\saber.png")
            janela = Tk()
            janela.title("Saber")
            janela.geometry(f"{imagem.width}x{imagem.height}")
            imagem_tk = ImageTk.PhotoImage(imagem)
            label = Label(janela, image=imagem_tk)
            label.pack()
            janela.mainloop()

        elif inventario[abririmg] == "Enxada (Deluxe, Usada pelo Deus do Capino dos Lotes)":
            imagem = Image.open("img\enxada_deuses.png")
            janela = Tk()
            janela.title("Enxada (Deluxe, Usada pelo Deus do Capino dos Lotes)")
            janela.geometry(f"{imagem.width}x{imagem.height}")
            imagem_tk = ImageTk.PhotoImage(imagem)
            label = Label(janela, image=imagem_tk)
            label.pack()
            janela.mainloop()

        elif inventario[abririmg] == "Cópia Física de “Everhood 2”":
            imagem = Image.open("img\everhood2_copia_fisica.png")
            janela = Tk()
            janela.title("Cópia Física de “Everhood 2”")
            janela.geometry(f"{imagem.width}x{imagem.height}")
            imagem_tk = ImageTk.PhotoImage(imagem)
            label = Label(janela, image=imagem_tk)
            label.pack()
            janela.mainloop()

        elif inventario[abririmg] == "Manga “Call of the Night”":
            imagem = Image.open("img\Call_of_the_night.png")
            janela = Tk()
            janela.title("Manga “Call of the Night”")
            janela.geometry(f"{imagem.width}x{imagem.height}")
            imagem_tk = ImageTk.PhotoImage(imagem)
            label = Label(janela, image=imagem_tk)
            label.pack()
            janela.mainloop()

        elif inventario[abririmg] == "Mangá “Jujutsu Kaizen 0”":
            imagem = Image.open("img\jjk0.png")
            janela = Tk()
            janela.title("Mangá “Jujutsu Kaizen 0”")
            janela.geometry(f"{imagem.width}x{imagem.height}")
            imagem_tk = ImageTk.PhotoImage(imagem)
            label = Label(janela, image=imagem_tk)
            label.pack()
            janela.mainloop()

        elif inventario[abririmg] == "Partes de Carro":
            imagem = Image.open("img\Partes de carro.png")
            janela = Tk()
            janela.title("Partes de Carro")
            janela.geometry(f"{imagem.width}x{imagem.height}")
            imagem_tk = ImageTk.PhotoImage(imagem)
            label = Label(janela, image=imagem_tk)
            label.pack()
            janela.mainloop()

        elif inventario[abririmg] == "Dicionário da Língua Espanhola":
            imagem = Image.open("img\dicionarioespanhol.png")
            janela = Tk()
            janela.title("Dicionário da Língua Espanhola")
            janela.geometry(f"{imagem.width}x{imagem.height}")
            imagem_tk = ImageTk.PhotoImage(imagem)
            label = Label(janela, image=imagem_tk)
            label.pack()
            janela.mainloop()

        elif inventario[abririmg] == "Cópia Física de “A Night in the Woods”":
            imagem = Image.open("img\A night in the woods physical.png")
            janela = Tk()
            janela.title("Cópia Física de “A Night in the Woods”")
            janela.geometry(f"{imagem.width}x{imagem.height}")
            imagem_tk = ImageTk.PhotoImage(imagem)
            label = Label(janela, image=imagem_tk)
            label.pack()
            janela.mainloop()

        elif inventario[abririmg] == "Coleção de Mangá da Série Jojo":
            imagem = Image.open("img\jojo.png")
            janela = Tk()
            janela.title("Coleção de Mangá da Série Jojo")
            janela.geometry(f"{imagem.width}x{imagem.height}")
            imagem_tk = ImageTk.PhotoImage(imagem)
            label = Label(janela, image=imagem_tk)
            label.pack()
            janela.mainloop()

        elif inventario[abririmg] == "Cópia Física de “Anno Mutationem”":
            imagem = Image.open("img\mutationem.png")
            janela = Tk()
            janela.title("Cópia Física de “Anno Mutationem”")
            janela.geometry(f"{imagem.width}x{imagem.height}")
            imagem_tk = ImageTk.PhotoImage(imagem)
            label = Label(janela, image=imagem_tk)
            label.pack()
            janela.mainloop()

        elif inventario[abririmg] == "Coleção Persona 3":
            imagem = Image.open("img\persona3.png")
            janela = Tk()
            janela.title("Coleção Persona 3")
            janela.geometry(f"{imagem.width}x{imagem.height}")
            imagem_tk = ImageTk.PhotoImage(imagem)
            label = Label(janela, image=imagem_tk)
            label.pack()
            janela.mainloop()

        elif inventario[abririmg] == "Cópia Digital de “Terraria” (2000 Horas)":
            imagem = Image.open("img\Terraria.jpg")
            janela = Tk()
            janela.title("Cópia Digital de “Terraria” (2000 Horas)")
            janela.geometry(f"{imagem.width}x{imagem.height}")
            imagem_tk = ImageTk.PhotoImage(imagem)
            label = Label(janela, image=imagem_tk)
            label.pack()
            janela.mainloop()

        elif inventario[abririmg] == "Kit de Poker":
            imagem = Image.open("img\omulo.png")
            janela = Tk()
            janela.title("Kit de Poker")
            janela.geometry(f"{imagem.width}x{imagem.height}")
            imagem_tk = ImageTk.PhotoImage(imagem)
            label = Label(janela, image=imagem_tk)
            label.pack()
            janela.mainloop()

        elif inventario[abririmg] == "Bola de Futebol Assinada":
            imagem = Image.open("img\Bola_assinada.png")
            janela = Tk()
            janela.title("Bola de Futebol Assinada")
            janela.geometry(f"{imagem.width}x{imagem.height}")
            imagem_tk = ImageTk.PhotoImage(imagem)
            label = Label(janela, image=imagem_tk)
            label.pack()
            janela.mainloop()

        elif inventario[abririmg] == "Kit de Chapéus":
            imagem = Image.open("img\kitchapeus.png")
            janela = Tk()
            janela.title("Kit de Chapéus")
            janela.geometry(f"{imagem.width}x{imagem.height}")
            imagem_tk = ImageTk.PhotoImage(imagem)
            label = Label(janela, image=imagem_tk)
            label.pack()
            janela.mainloop()

        elif inventario[abririmg] == "Livro “Como Fazer Agachamento”":
            imagem = Image.open("img\gachamento.png")
            janela = Tk()
            janela.title("Livro “Como Fazer Agachamento”")
            janela.geometry(f"{imagem.width}x{imagem.height}")
            imagem_tk = ImageTk.PhotoImage(imagem)
            label = Label(janela, image=imagem_tk)
            label.pack()
            janela.mainloop()

        elif inventario[abririmg] == "Jockey de Galinha":
            imagem = Image.open("img\jockey de galinha.png")
            janela = Tk()
            janela.title("Jockey de Galinha")
            janela.geometry(f"{imagem.width}x{imagem.height}")
            imagem_tk = ImageTk.PhotoImage(imagem)
            label = Label(janela, image=imagem_tk)
            label.pack()
            janela.mainloop()

        elif inventario[abririmg] == "Doutorado":
            imagem = Image.open("img\doutorado.png")
            janela = Tk()
            janela.title("Doutorado")
            janela.geometry(f"{imagem.width}x{imagem.height}")
            imagem_tk = ImageTk.PhotoImage(imagem)
            label = Label(janela, image=imagem_tk)
            label.pack()
            janela.mainloop()

        elif inventario[abririmg] == "Máquina de Contato Extraterrestre":
            imagem = Image.open("img\maquina_extra_terrestre.png")
            janela = Tk()
            janela.title("Máquina de Contato Extraterrestre")
            janela.geometry(f"{imagem.width}x{imagem.height}")
            imagem_tk = ImageTk.PhotoImage(imagem)
            label = Label(janela, image=imagem_tk)
            label.pack()
            janela.mainloop()

        elif inventario[abririmg] == "“Are You Sure?”":
            imagem = Image.open("img\eyousure.png")
            janela = Tk()
            janela.title("“Are You Sure?”")
            janela.geometry(f"{imagem.width}x{imagem.height}")
            imagem_tk = ImageTk.PhotoImage(imagem)
            label = Label(janela, image=imagem_tk)
            label.pack()
            janela.mainloop()

        elif inventario[abririmg] == "Carmed":
            imagem = Image.open("img\carmed.png")
            janela = Tk()
            janela.title("Carmed")
            janela.geometry(f"{imagem.width}x{imagem.height}")
            imagem_tk = ImageTk.PhotoImage(imagem)
            label = Label(janela, image=imagem_tk)
            label.pack()
            janela.mainloop()

        else:
            print("erro!")
        
        contobserve = input("Gostaria de observar um outro item? 1 - Sim / 0 - Não : ")
        
def atualizar_nome():
    global ProtagonistaDaJornadaDeRevendas
    novo_nome = input("{} : Digite o novo nome do protagonista: ".format(Vendedor))
    ProtagonistaDaJornadaDeRevendas = novo_nome
    print("Nome atualizado com sucesso!")

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

print("??? : Seja bem vido a loja de revenda 'L. S. Lixão' Sou o trabalhador que irá lhe acompanhar meu nome é {} , será um prazer lhe ajudar.".format(Vendedor))
time.sleep(2)
print("{} : Para começar a vender, ou comprar, porfavor insira seu nome.".format(Vendedor))
time.sleep(2)
ProtagonistaDaJornadaDeRevendas = input("Digite seu nome : ")
time.sleep(2)
nome_certo(ProtagonistaDaJornadaDeRevendas)
time.sleep(2)
print("{} : O menu da loja irá abrir, vendemos várias coisas, exceto coisas orgânicas. Boa sorte.".format(Vendedor))
time.sleep(5)

def main():
    opcao = 1
    while opcao != 0:
        adicionarprodutosnaloja()
        WelcomeFolks()
        
       
        opcao = int(input('Opção? '))
        if opcao == 1:
            comprarprodutos()
        elif opcao == 2:
            venderprodutos()
        elif opcao == 3:
            interação()
        elif opcao == 4:
            Fimdedia()
        elif opcao == 5:
            adicionarprodutosnaloja()
        elif opcao == 6:
            observearitens()
        elif opcao == 7:
            atualizar_nome()
        elif opcao == 0:
            break
        else:
            print('Opção inválida')
        
if __name__ == "__main__":
    main()

    
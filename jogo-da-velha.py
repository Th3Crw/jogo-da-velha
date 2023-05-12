from tkinter import *


def proximo_turno(linha, coluna): 
     global jogador_atual
     
     if espacos[linha][coluna]['text'] == "" and verificar_vencedor() is False: #Botão Vazio Sem Vencedor
         if jogador_atual == jogadores[0]:
             espacos[linha][coluna]['text'] = jogador_atual

             if verificar_vencedor() is False:
                 jogador_atual = jogadores[1]
                 turno.config(text= (f"Turno do {jogador_atual}"))

             elif verificar_vencedor() is True:
                 
                 turno.config(text= (f"{jogadores[0]} Vence!"))

             elif verificar_vencedor() == "Empate":
                 turno.config(text=("Empate!"))
         else:
             espacos[linha][coluna]['text'] = jogador_atual

             if verificar_vencedor() is False:
                 jogador_atual = jogadores[0]
                 turno.config(text=(f"Turno do {jogador_atual}"))

             elif verificar_vencedor() is True:
                 turno.config(text=(f"{jogadores[1]} Vence!"))

             elif verificar_vencedor() == "Empate":
                 turno.config(text=("Empate!"))
                      

def espaco_vazio():
    espaco_livre = 9
    for linha in range(3):
        for coluna in range(3):
            if espacos[linha][coluna]['text'] != "":
                espaco_livre -= 1
    if espaco_livre == 0:
        return False
    else:
        return True

def verificar_vencedor():
    for linha in range(3): #Checar condições de vitória horizontais
        if espacos[linha][0]['text'] == espacos[linha][1]['text'] == espacos[linha][2]['text'] != "":
            return True
    for coluna in range(3): #Checar condições de vitória verticais
        if espacos[0][coluna]['text'] == espacos[1][coluna]['text'] == espacos[2][coluna]['text'] != "":
            return True
    
    #Checar condições de vitória diagonais
    if espacos[0][0]['text'] == espacos[1][1]['text'] == espacos[2][2]['text'] != "":
        return True
    elif espacos[0][2]['text'] == espacos[1][1]['text'] == espacos[2][0]['text'] != "":
        return True
    
    elif espaco_vazio() is False:
        return 'Empate'
    
    else:
        return False
        

def novo_jogo():
    global jogador_atual

    jogador_atual = jogadores[0]
    turno.config(text= f"Turno do {jogador_atual}")

    for linha in range(3):
        for coluna in range(3):
            espacos[linha][coluna].config(text="")


janela = Tk()
janela.title("Jogo da Velha")

jogadores = ["X", "O"]
jogador_atual = jogadores[0]

espacos = [[0,0,0], 
           [0,0,0], 
           [0,0,0]]

turno = Label(text= f"Turno do {jogador_atual}", font=("Times New Roman", 40))
turno.pack(side="top")

botao_resetar = Button(text="Resetar", font=("Times New Roman", 20), command=novo_jogo)
botao_resetar.pack(side="bottom")

tabuleiro = Frame(janela)
tabuleiro.pack()

for linha in range(3):
    for coluna in range(3):
        espacos[linha][coluna] = Button(tabuleiro, text="", font=("Times New Roman", 40), width=5, height= 2, command= lambda linha=linha, coluna = coluna: proximo_turno(linha,coluna))
        espacos[linha][coluna].grid(row=linha, column=coluna)

janela.mainloop()
# Importar módulos necessários
import random
import tkinter as tk
from tkinter import messagebox

# Criar uma lista de perguntas e respostas sobre canais iônicos
perguntas = [
    ("Qual canal iônico é responsável pela despolarização da membrana celular durante um potencial de ação?", "A) Canal de sódio\nB) Canal de potássio\nC) Canal de cálcio\nD) Canal de cloro", "A"),
    ("Qual canal iônico é bloqueado pelo tetrodotoxina, uma toxina encontrada no peixe baiacu?", "A) Canal de sódio\nB) Canal de potássio\nC) Canal de cálcio\nD) Canal de cloro", "A"),
    ("Qual canal iônico é ativado pelo neurotransmissor GABA, causando uma hiperpolarização da membrana pós-sináptica?", "A) Canal de sódio\nB) Canal de potássio\nC) Canal de cálcio\nD) Canal de cloro", "D"),
    ("Qual canal iônico é afetado pelos anestésicos locais, como a lidocaína, que impedem a transmissão do impulso nervoso?", "A) Canal de sódio\nB) Canal de potássio\nC) Canal de cálcio\nD) Canal de cloro", "A"),
    ("Qual canal iônico é regulado pelo hormônio insulina, que facilita a entrada de glicose nas células?", "A) Canal de sódio\nB) Canal de potássio\nC) Canal de cálcio\nD) Canal de cloro", "B")
]

# Criar uma janela gráfica para o jogo
janela = tk.Tk()
janela.title("Jogo de Farmacologia sobre Canais Iônicos")
janela.geometry("600x400")

# Criar uma variável para armazenar a pontuação do jogador
pontuacao = tk.IntVar()
pontuacao.set(0)

# Criar uma função para mostrar uma pergunta aleatória na janela
def mostrar_pergunta():
    # Escolher uma pergunta e uma resposta aleatórias da lista
    pergunta, alternativas, resposta = random.choice(perguntas)
    
    # Limpar a janela de qualquer widget anterior
    for widget in janela.winfo_children():
        widget.destroy()
    
    # Criar um rótulo para mostrar a pergunta na janela
    rotulo_pergunta = tk.Label(janela, text=pergunta, font=("Arial", 16), wraplength=500)
    rotulo_pergunta.pack(pady=20)
    
    # Criar um rótulo para mostrar as alternativas na janela
    rotulo_alternativas = tk.Label(janela, text=alternativas, font=("Arial", 14), justify="left")
    rotulo_alternativas.pack(pady=10)
    
    # Criar um campo de entrada para o jogador digitar a sua resposta na janela
    entrada_resposta = tk.Entry(janela, font=("Arial", 14), width=5)
    entrada_resposta.pack(pady=10)
    
    # Criar um botão para enviar a resposta e verificar se está correta na janela
    botao_enviar = tk.Button(janela, text="Enviar", font=("Arial", 14), command=lambda: verificar_resposta(entrada_resposta.get(), resposta))
    botao_enviar.pack(pady=10)

# Criar uma função para verificar se a resposta do jogador está correta e atualizar a pontuação
def verificar_resposta(resposta_jogador, resposta_correta):
    # Comparar a resposta do jogador com a resposta correta
    if resposta_jogador.upper() == resposta_correta.upper():
        # Se a resposta estiver correta, aumentar a pontuação em um ponto
        pontuacao.set(pontuacao.get() + 1)
        # Mostrar uma mensagem de parabéns na janela
        tk.messagebox.showinfo("Parabéns!", "Você acertou!")
    else:
        # Se a resposta estiver errada, mostrar uma mensagem de erro na janela
        tk.messagebox.showerror("Erro!", f"Você errou! A resposta correta era {resposta_correta}.")
    
    # Mostrar outra pergunta na janela
    mostrar_pergunta()

# Mostrar a primeira pergunta na janela
mostrar_pergunta()

# Criar um rótulo para mostrar a pontuação do jogador na janela
rotulo_pontuacao = tk.Label(janela, textvariable=pontuacao, font=("Arial", 14))
rotulo_pontuacao.place(x=550, y=10)

# Iniciar o loop principal da janela
janela.mainloop()

import tkinter as tk
import random

class AdivinhaNumero:
    def __init__(self, root):
        self.root = root
        self.root.title("Adivinhe o Número")
        self.root.configure(bg="#E3F2FD")

        self.numero_secreto = random.randint(1, 100)
        self.tentativas = 0

        self.label_instrucoes = tk.Label(root, text="Adivinhe um número entre 1 e 100:", bg="#E3F2FD", font=("Helvetica", 16, "bold"), fg="#4A148C")
        self.label_instrucoes.pack(pady=15)

        self.entrada = tk.Entry(root, font=("Helvetica", 14), bd=2, relief="solid")
        self.entrada.pack(pady=10)
        self.entrada.bind("<Return>", self.adivinhar)

        self.botao_adivinhar = tk.Button(root, text="Adivinhar", command=self.adivinhar, bg="#6A1B9A", fg="white", font=("Helvetica", 14, "bold"), bd=2, relief="raised")

        self.label_resultado = tk.Label(root, text="", bg="#E3F2FD", font=("Helvetica", 14, "italic"), fg="#1E88E5")
        self.label_resultado.pack(pady=10)

        self.label_novo_num = tk.Label(root, text="", bg="#E3F2FD", font=("Helvetica", 12), fg="#1E88E5")
        self.label_novo_num.pack(pady=10)

        self.label_novo_num.config(text="Um número foi sortado entre 1 e 100!")

    def adivinhar(self, event=None):
        palpite = self.entrada.get()

        if palpite.isdigit():
            palpite = int(palpite)
            self.tentativas += 1

            if palpite < self.numero_secreto:
                self.label_resultado.config(text="Muito baixo! Tente novamente.", fg="#D32F2F")
                self.label_novo_num.config(text=" ")
            elif palpite > self.numero_secreto:
                self.label_resultado.config(text="Muito alto! Tente novamente.", fg="#D32F2F")
                self.label_novo_num.config(text=" ")
            else:
                self.label_resultado.config(text=f"Parabéns! Você acertou em {self.tentativas} tentativas!", fg="#4CAF50")
                self.tentativas = 0
                self.label_novo_num.config(text="Um novo número foi sortado entre 1 e 100!")
                self.numero_secreto = random.randint(1, 100)
        else:
            self.label_resultado.config(text="Por favor, insira apenas números.", fg="#F44336")

root = tk.Tk()
app = AdivinhaNumero(root)
root.mainloop()

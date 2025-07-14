import random
from os import system, name

def limpa_tela():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def display_hangman(chances):
    stages = [
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |      
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|
           |      |
           |     
           -
        """,
        """
           --------
           |      |
           |      O
           |      |
           |      |
           |     
           -
        """,
        """
           --------
           |      |
           |      O
           |    
           |      
           |     
           -
        """,
        """
           --------
           |      |
           |      
           |    
           |      
           |     
           -
        """
    ]
    return stages[chances]

def game():
    limpa_tela()
    print("\n🎉 Bem-vindo(a) ao jogo da forca!")
    print("🔤 Tente adivinhar a palavra abaixo:\n")

    palavras = ['banana', 'sao paulo', 'guarda-chuva', 'livro', 'meu amigo', 'cachorro']
    palavra = random.choice(palavras)
    lista_letras_palavras = [letra for letra in palavra]
    tabuleiro = ['-' if letra == '-' else ' ' if letra == ' ' else '_' for letra in palavra]
    chances = 6
    letras_tentativas = []
    letras_erradas = []

    while chances > 0:
        print(display_hangman(chances))
        print("📌 Palavra:", " ".join(tabuleiro))
        print("📝 Letras tentadas:", ", ".join(letras_tentativas))
        print("❌ Letras erradas: ", ", ".join(letras_erradas))
        print("\n")

        tentativa = input("Digite uma letra: ").lower()

        if tentativa.isdigit():
            print("⚠️ Por favor, digite **uma letra**, não um número.")
        
        elif len(tentativa) != 1:
            print("⚠️ Digite **somente uma letra** por vez.")
        
        else:
            if tentativa in letras_tentativas:
                print("🔁 Você já tentou essa letra. Tente outra!")
                continue

            letras_tentativas.append(tentativa)

            if tentativa in lista_letras_palavras:
                print("✅ Boa! Você acertou a letra!")

                for indice in range(len(lista_letras_palavras)):
                    if lista_letras_palavras[indice] == tentativa:
                        tabuleiro[indice] = tentativa

                if "_" not in tabuleiro:
                    print(f"\n🏆 Parabéns! Você venceu! A palavra era: **{palavra}**")
                    break
            else:
                print("❌ Ops! Essa letra não está na palavra.")
                chances -= 1
                letras_erradas.append(tentativa)

    if "_" in tabuleiro:
        print(f"\n💀 Você perdeu! A palavra correta era: **{palavra}**.")

if __name__ == "__main__":
    game()

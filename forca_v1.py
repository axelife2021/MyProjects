# Hangman Game (Jogo da Forca) 
# Programação Orientada a Objetos

# Import
import random

# Board (tabuleiro)
board = ['''

+---+
|   |
	|
	|
	|
	|
=========''', '''

+---+
|   |
O   |
	|
	|
	|
=========''', '''

+---+
|   |
O   |
|   |
	|
	|
=========''', '''

 +---+
 |   |
 O   |
/|   |
	 |
	 |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
	 |
	 |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
	 |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
	 |
=========''']

# Classe
class Hangman:

    # Método Construtor
    def __init__(self, word):
        self.word = word
        self.wrong_letters = []
        self.right_letters = []
        self.index_board = 0
        self.hidden_word = '_' * len(word)

    # Método para adivinhar a letra
    def guess(self, letter):
        if letter in self.word:
            self.add_letter_in_rights(letter)
        else:
            self.add_letter_in_wrongs(letter)

    # Método para verificar se o jogo terminou
    def hangman_over(self):
        return (self.index_board == (len(board) - 1)) or (self.hidden_word == self.word)

    # Método para verificar se o jogador venceu
    def hangman_won(self):
        return self.word == self.hidden_word

    # Método para não mostrar a letra no board
    def hide_word(self):
        for (i, l_word) in enumerate(self.word):
            self.hidden_word = self.hidden_word[:i] + self.right_letters[-1] + self.hidden_word[i + 1:] if (
                    l_word == self.right_letters[-1]) else self.hidden_word

    # Método para imprimir o board na tela
    def print_game_status(self):
        print(board[self.index_board])

    #Método para adicionar letra na lista de letras corretas
    def add_letter_in_rights(self, letter):
        if letter not in self.right_letters:
            self.right_letters.append(letter)
            self.hide_word()
        else:
            print(f'\nA letra {letter} já foi utilizada.')
            letter = input('\nDigite uma letra: ')
            self.guess(letter)

    #Método para adicionar letra na lista de letras erradas
    def add_letter_in_wrongs(self, letter):
        if letter not in self.wrong_letters:
            self.wrong_letters.append(letter)
            self.index_board += 1
        else:
            print(f'\nA letra {letter} já foi utilizada.')
            letter = input('\nDigite uma letra: ')
            self.guess(letter)

# Função para ler uma palavra de forma aleatória do banco de palavras
def rand_word():
    with open("palavras.txt", "rt") as f:
        bank = f.readlines()
    return bank[random.randint(0, len(bank))].strip()

# Função Main - Execução do Programa
def main():
    # Objeto
    game = Hangman(rand_word())

    #Imprimindo o título do jogo
    print('\n>>>>>>>>>>Hangman<<<<<<<<<<')

    # Enquanto o jogo não tiver terminado, print do status, solicita uma letra e faz a leitura do caracter
    while not game.hangman_over():
        # Verifica o status do jogo
        game.print_game_status()
        print('\nPalavra: ' + game.hidden_word)
        print('\nLetras erradas: \n' + '\n'.join(game.wrong_letters))
        print('Letras corretas: \n' + '\n'.join(game.right_letters) + '\n')
        letter = input('Digite uma letra: ')
        game.guess(letter)

    # De acordo com o status, imprime mensagem na tela para o usuário
    if game.hangman_won():
        print(board[game.index_board])
        print('\nPalavra: ' + game.hidden_word)
        print('\nLetras erradas: \n' + '\n'.join(game.wrong_letters))
        print('Letras corretas: \n' + '\n'.join(game.right_letters) + '\n')
        print('\nParabéns! Você venceu!!')
    else:
        print(board[game.index_board])
        print('\nPalavra: ' + game.hidden_word)
        print('\nLetras erradas: \n' + '\n'.join(game.wrong_letters))
        print('Letras corretas: \n' + '\n'.join(game.right_letters) + '\n')
        print('\nGame over! Você perdeu.')
        print('A palavra era ' + game.word)

    print('\nFoi bom jogar com você! Agora vá estudar!\n')

# Executa o programa
if __name__ == "__main__":
    main()
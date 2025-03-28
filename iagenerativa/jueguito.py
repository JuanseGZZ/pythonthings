import random

def play_game():
    game_words = ["python", "programacion", "inteligencia", "artificial", "juego"]
    palabra = random.choice(game_words)
    vidas = 6
    letras_adivinadas = ["_"] * len(palabra)
    letras_usadas = set()

    print("¡Bienvenido al juego de adivinar palabras!")
    print(" ".join(letras_adivinadas))

    while vidas > 0:
        letra = input("Adivina una letra: ").lower()

        if len(letra) != 1 or not letra.isalpha():
            print("Por favor, introduce una sola letra válida.")
            continue

        if letra in letras_usadas:
            print("Ya has usado esa letra. Intenta con otra.")
            continue

        letras_usadas.add(letra)

        if letra in palabra:
            print(f"¡Bien hecho! La letra '{letra}' está en la palabra.")
            for i, l in enumerate(palabra):
                if l == letra:
                    letras_adivinadas[i] = letra
        else:
            vidas -= 1
            print(f"La letra '{letra}' no está en la palabra. Te quedan {vidas} vidas.")

        print(" ".join(letras_adivinadas))

        if "_" not in letras_adivinadas:
            print("¡Felicidades! Has adivinado la palabra.")
            break
    else:
        print(f"Te has quedado sin vidas. La palabra era '{palabra}'.")

if __name__ == "__main__":
    play_game()

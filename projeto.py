# JOGO DE ADIVINHAÇÃO + IMPRESSÃO DE MATRIZ E CÉDULAS

from random import randint

# --- JOGO DE ADIVINHAÇÃO ---
print("🔢 A MÁQUINA ESCOLHEU UM NÚMERO ENTRE 1 E 20. TENTE ADIVINHAR!")

escolha_maquina = randint(1, 20)
tentativas = 0
limite_tentativas = 5

while tentativas < limite_tentativas:
    try:
        palpite = int(input(f"Tentativa {tentativas + 1}/{limite_tentativas}: "))
        tentativas += 1

        if palpite == escolha_maquina:
            print("🎉 Parabéns, você acertou!")
            break
        elif palpite < escolha_maquina:
            print("⬆️ Muito baixo.")
        else:
            print("⬇️ Muito alto.")
    except ValueError:
        print("❗ Por favor, digite um número válido.")

else:
    print(f"❌ Suas tentativas acabaram. O número era {escolha_maquina}.")

print("\n---\n")

# --- IMPRESSÃO DE MATRIZ E CÉDULAS ---
matrix_numeros = [
    [1, 4, 5, 6],
    [7, 8, 9],
    [0]
]

print("📊 Matriz de números:")
for linha in matrix_numeros:
    print(linha)

cedulas = [100, 50, 20, 10, 5, 2]
print("\n💵 Cédulas disponíveis:")
print(cedulas)

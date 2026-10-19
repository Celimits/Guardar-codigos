import random
import time
import sys

EMOJIS = ["🍒", "🍉", "🍋", "⭐", "💎"]
SALDO_INICIAL = 100

def girar_roleta():
    return [random.choice(EMOJIS) for _ in range(3)]

def efeito_roleta():
    """Cria uma animação de rotação no terminal."""
    for i in range(15):
        roleta_visual = [random.choice(EMOJIS) for _ in range(3)]
        sys.stdout.write(f"\r🎰  [ {roleta_visual[0]} | {roleta_visual[1]} | {roleta_visual[2]} ]  🎰")
        sys.stdout.flush()
        time.sleep(0.05 + (i * 0.02))
    print()

def calcular_premio(resultado, aposta):
    """Calcula o ganho com base nos emojis sorteados."""
    if resultado[0] == resultado[1] == resultado[2]:
        if resultado[0] == "💎":
            return aposta * 10, "JACKPOT DE DIAMANTE! 💎💎💎"
        elif resultado[0] == "⭐":
            return aposta * 5, "Grande Vitória! ⭐⭐⭐"
        else:
            return aposta * 3, f"Três iguais! {resultado[0] * 3}"
    elif resultado[0] == resultado[1] or resultado[1] == resultado[2] or resultado[0] == resultado[2]:
        return int(aposta * 1.5), "Par combinado! Retorno parcial."
    
    return 0, "Não foi dessa vez. Tente novamente!"

def jogar():
    saldo = SALDO_INICIAL
    print("=" * 45)
    print("🎰 BEM-VINDO AO PY-CASSINO STANDARD EDITION 🎰")
    print(f"Você começa com um saldo inicial de: ${saldo}")
    print("=" * 45)
    print(f"Símbolos válidos: {' '.join(EMOJIS)}")
    print("Regras: 3 Iguais = até 10x | 2 Iguais = 1.5x")
    print("=" * 45)

    while saldo > 0:
        print(f"\nSeu saldo atual: ${saldo}")
        entrada = input("Digite o valor da sua aposta (ou 'sair' para encerrar): ").strip().lower()

        if entrada == 'sair':
            break

        if not entrada.isdigit():
            print("❌ Por favor, insira um número válido.")
            continue

        aposta = int(entrada)

        if aposta <= 0:
            print("❌ A aposta deve ser maior que zero.")
            continue

        if aposta > saldo:
            print("❌ Saldo insuficiente para essa aposta!")
            continue

        saldo -= aposta
        print("\nPuxando a alavanca...")
        
        efeito_roleta()
        resultado = girar_roleta()
        
        print(f"🎯  [ {resultado[0]} | {resultado[1]} | {resultado[2]} ]  🎯")

        ganho, mensagem = calcular_premio(resultado, aposta)
        saldo += ganho

        print(f"-> {mensagem}")
        if ganho > 0:
            print(f"💰 Você ganhou: ${ganho}!")

    print("\n" + "=" * 45)
    if saldo <= 0:
        print("💥 Você faliu! O cassino sempre ganha. 😉")
    else:
        print(f"👋 Você saiu do jogo com ${saldo}. Até a próxima!")
    print("=" * 45)

if __name__ == "__main__":
    jogar()

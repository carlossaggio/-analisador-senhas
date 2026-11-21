import getpass
import re


SENHAS_COMUNS = {
    "123456", "12345678", "123456789", "1234567890", "000000",
    "password", "password123", "senha", "senha123", "admin", "admin123",
    "qwerty", "qwerty123", "abc123", "letmein", "iloveyou",
}

TERMOS_PREVISIVEIS = ("password", "senha", "qwerty", "admin", "123456")
SEQUENCIAS_TECLADO = ("qwerty", "asdfgh", "zxcvbn", "1qaz", "2wsx")


def contem_sequencia(senha):
    texto = senha.lower()

    if any(sequencia in texto for sequencia in SEQUENCIAS_TECLADO):
        return True

    for indice in range(len(texto) - 3):
        trecho = texto[indice:indice + 4]

        if not (trecho.isascii() and (trecho.isalpha() or trecho.isdigit())):
            continue

        codigos = [ord(caractere) for caractere in trecho]
        crescente = all(codigos[i + 1] - codigos[i] == 1 for i in range(3))
        decrescente = all(codigos[i + 1] - codigos[i] == -1 for i in range(3))

        if crescente or decrescente:
            return True

    return False


def contem_repeticao(senha):
    if re.search(r"(.)\1{2,}", senha):
        return True

    for tamanho in range(1, min(5, len(senha) // 3 + 1)):
        for inicio in range(len(senha) - tamanho * 3 + 1):
            trecho = senha[inicio:inicio + tamanho]
            if senha[inicio:inicio + tamanho * 3] == trecho * 3:
                return True

    return False


def analisar_senha(senha):
    tamanho = len(senha)
    tipos = sum((
        any(caractere.islower() for caractere in senha),
        any(caractere.isupper() for caractere in senha),
        any(caractere.isdigit() for caractere in senha),
        any(not caractere.isalnum() for caractere in senha),
    ))
    texto = senha.casefold()
    comum = texto in SENHAS_COMUNS
    termo_previsivel = any(termo in texto for termo in TERMOS_PREVISIVEIS)
    sequencia = contem_sequencia(senha)
    repeticao = contem_repeticao(senha)

    if tamanho < 8:
        pontuacao = 5
    elif tamanho < 12:
        pontuacao = 25
    elif tamanho < 16:
        pontuacao = 45
    elif tamanho < 20:
        pontuacao = 65
    else:
        pontuacao = 78

    if tipos >= 3:
        pontuacao += 12
    elif tipos == 2:
        pontuacao += 6

    if len(set(senha)) >= 8:
        pontuacao += 5

    recomendacoes = []

    if tamanho < 12:
        recomendacoes.append("Prefira senhas longas, com pelo menos 12 caracteres.")
    elif tamanho < 16:
        recomendacoes.append("Uma senha mais longa ou uma frase-senha pode ser ainda melhor.")

    if comum:
        recomendacoes.append("Esta senha aparece na pequena lista local de exemplos comuns.")
        pontuacao = min(pontuacao, 10)
    elif termo_previsivel:
        recomendacoes.append("Evite palavras e combinações muito previsíveis.")
        pontuacao = min(pontuacao - 20, 35)

    if sequencia:
        recomendacoes.append("Evite sequências de teclado, letras ou números em ordem.")
        pontuacao -= 15

    if repeticao:
        recomendacoes.append("Evite caracteres ou blocos repetidos várias vezes.")
        pontuacao -= 15

    if tipos == 1 and tamanho < 16:
        recomendacoes.append("Considere uma frase-senha longa ou uma combinação menos previsível.")

    if tamanho < 8:
        pontuacao = min(pontuacao, 20)
    elif tamanho < 12:
        pontuacao = min(pontuacao, 55)

    pontuacao = max(0, min(100, pontuacao))

    if pontuacao < 20:
        nivel = "Muito fraca"
    elif pontuacao < 40:
        nivel = "Fraca"
    elif pontuacao < 60:
        nivel = "Moderada"
    elif pontuacao < 80:
        nivel = "Boa"
    else:
        nivel = "Forte"

    if not recomendacoes:
        recomendacoes.append("Continue usando uma senha exclusiva para cada conta.")

    return {"pontuacao": pontuacao, "nivel": nivel, "recomendacoes": recomendacoes}


def main():
    print("\nANALISADOR DE SENHAS | PROJETO EDUCACIONAL")
    print("A análise acontece localmente, sem salvar ou transmitir a senha.")
    print("A pontuação é apenas uma estimativa didática de características observáveis.")
    print("Use exemplos fictícios, não senhas de contas reais.\n")

    while True:
        try:
            senha = getpass.getpass("Digite uma senha de teste: ")
        except (EOFError, KeyboardInterrupt):
            print("\nPrograma encerrado.")
            break

        resultado = analisar_senha(senha)
        print(f"\nNível: {resultado['nivel']}")
        print(f"Indicador didático: {resultado['pontuacao']}/100")
        print("Recomendações:")

        for recomendacao in resultado["recomendacoes"]:
            print(f"- {recomendacao}")

        try:
            repetir = input("\nAnalisar outra senha fictícia? (s/n): ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            print("\nPrograma encerrado.")
            break

        if repetir != "s":
            print("Até a próxima!")
            break


if __name__ == "__main__":
    main()

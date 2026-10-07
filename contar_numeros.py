import re
import sys
from pathlib import Path

def contar_numeros(arquivo):
    # errors="replace" evita que o programa pare caso o XML tenha algum
    # caractere com codificação diferente de UTF-8.
    conteudo = Path(arquivo).read_text(encoding="utf-8", errors="replace")

    numeros = re.findall(
        r"<numeroTerminal>\s*(.*?)\s*</numeroTerminal>",
        conteudo,
        re.DOTALL | re.IGNORECASE
    )

    encontrados = set()

    for numero in numeros:
        # Remove { }, espaços, hífens, parênteses etc.,
        # deixando somente os dígitos.
        numero = re.sub(r"\D", "", numero.strip())
        if numero:
            encontrados.add(numero)

    return encontrados


if len(sys.argv) < 2:
    print("Arraste um arquivo XML para cima deste .BAT.")
    input("\nPressione ENTER para sair...")
    sys.exit(1)

arquivo = sys.argv[1]

try:
    numeros = contar_numeros(arquivo)

    print("=" * 60)
    print("CONTAGEM DE NUMEROS TELEFONICOS")
    print("=" * 60)
    print(f"Arquivo: {arquivo}")
    print(f"\nQuantidade de numeros diferentes: {len(numeros)}")
    print("\nNumeros encontrados:")

    for numero in sorted(numeros):
        print(numero)

    print("\n" + "=" * 60)

except FileNotFoundError:
    print(f"ERRO: arquivo nao encontrado:\n{arquivo}")
except Exception as e:
    print(f"ERRO: {e}")

input("\nPressione ENTER para fechar...")

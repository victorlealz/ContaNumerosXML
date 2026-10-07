# CONTADOR DE NÚMEROS TELEFÔNICOS

Ferramenta simples em Python para extrair e contabilizar **números telefônicos distintos** presentes em arquivos XML.

O programa procura pelas informações contidas nas tags:

```xml
<numeroTerminal>...</numeroTerminal>
```

Os números são normalizados, removendo espaços, parênteses, hífens e outros caracteres, mantendo somente os dígitos. Números repetidos são contabilizados apenas uma vez.

---

## 1. Arquivos do programa

O software é composto por dois arquivos:

```text
Contador de Numeros Telefonicos/
│
├── contar_numeros.bat
├── contar_numeros.py
└── README.md
```

### `contar_numeros.bat`

Arquivo responsável por iniciar o programa no Windows.

Ele verifica automaticamente se o Python está disponível através dos comandos:

```text
py
```

ou

```text
python
```

### `contar_numeros.py`

Arquivo principal responsável pela leitura do XML, extração, normalização e contagem dos números telefônicos.

---

## 2. Requisitos

- Windows 10 ou Windows 11;
- Python 3 instalado;
- Arquivo XML contendo informações na tag `<numeroTerminal>`.

Não são necessárias bibliotecas externas. O programa utiliza apenas módulos que já fazem parte da instalação padrão do Python.

---

## 3. Instalação do Python

Caso o computador não possua Python instalado, instale uma versão recente do Python 3.

Durante a instalação, recomenda-se habilitar a opção:

```text
Add Python to PATH
```

Após a instalação, o programa poderá ser executado normalmente.

---

## 4. Como utilizar

### Método recomendado — arrastar o XML

1. Localize o arquivo XML que deseja analisar.
2. Localize o arquivo:

```text
contar_numeros.bat
```

3. **Arraste o arquivo XML para cima do `contar_numeros.bat`.**
4. Uma janela será aberta automaticamente.
5. O programa realizará a leitura e exibirá os números encontrados.

### Exemplo

```text
arquivo.xml
     │
     │ arrastar
     ▼
contar_numeros.bat
```

---

## 5. Resultado

O programa exibirá:

- o arquivo analisado;
- a quantidade de números telefônicos diferentes;
- a lista dos números encontrados.

Exemplo:

```text
============================================================
CONTAGEM DE NUMEROS TELEFONICOS
============================================================
Arquivo: C:\Investigacao\dados.xml

Quantidade de numeros diferentes: 5

Numeros encontrados:
5511987654321
5583987654321
5583998765432
5583987654322
5583991234567

============================================================
```

---

## 6. Tratamento de números

O programa mantém somente os caracteres numéricos.

Por exemplo, os seguintes valores:

```text
(83) 99999-9999
83 99999-9999
83-99999-9999
{83} 99999-9999
```

serão convertidos para:

```text
83999999999
```

Dessa forma, diferentes formas de representação do mesmo número são consideradas como um único número.

---

## 7. Números duplicados

O programa elimina números repetidos.

Por exemplo, se o XML possuir:

```xml
<numeroTerminal>(83) 99999-9999</numeroTerminal>
<numeroTerminal>83 99999-9999</numeroTerminal>
<numeroTerminal>83999999999</numeroTerminal>
```

o resultado será:

```text
Quantidade de numeros diferentes: 1
```

---

## 8. Codificação do XML

O programa tenta ler os arquivos utilizando **UTF-8**.

Caso existam caracteres incompatíveis com essa codificação, o programa utiliza tratamento de erro para evitar que a execução seja interrompida.

Isso permite trabalhar com determinados XMLs que apresentem problemas de codificação de caracteres.

---

## 9. Estrutura esperada do XML

O programa procura especificamente por elementos semelhantes a:

```xml
<numeroTerminal>83999999999</numeroTerminal>
```

Também são aceitas quebras de linha e espaços dentro da tag, por exemplo:

```xml
<numeroTerminal>
    83999999999
</numeroTerminal>
```

A busca não diferencia letras maiúsculas e minúsculas.

---

## 10. Erros comuns

### Python não encontrado

Caso apareça:

```text
ERRO: Python nao foi encontrado neste computador.
```

significa que o Python não foi localizado pelo Windows.

Instale o Python 3 e tente novamente.

### Arquivo XML não encontrado

Caso o arquivo tenha sido movido, renomeado ou excluído durante a execução, poderá aparecer:

```text
ERRO: arquivo nao encontrado
```

Verifique se o XML ainda existe no local indicado.

### Nenhum número encontrado

Se o programa apresentar:

```text
Quantidade de numeros diferentes: 0
```

verifique se o XML realmente contém elementos:

```xml
<numeroTerminal>...</numeroTerminal>
```

---

## 11. Observações

- O arquivo XML original **não é alterado**.
- O programa apenas realiza a leitura dos dados.
- Números repetidos são contabilizados uma única vez.
- Caracteres não numéricos são removidos dos números.
- Os números são apresentados em ordem crescente.
- O processamento é realizado localmente no computador.
- Não é necessária conexão com a Internet.

---

## 12. Uso em investigação

A ferramenta pode ser utilizada como recurso auxiliar para análise de arquivos XML que contenham registros de números telefônicos.

O resultado deve ser considerado uma **extração automatizada dos dados presentes no arquivo analisado**, devendo eventual utilização em relatório, informação ou procedimento investigativo ser conferida conforme a origem e a integridade do arquivo.

---

## 13. Licença / distribuição

Este software é destinado a uso interno e operacional.

A distribuição, modificação ou incorporação em outros sistemas deve observar as regras e autorizações aplicáveis à instituição responsável pelo seu uso.

By Victor Leal Antunes.

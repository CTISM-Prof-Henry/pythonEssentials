# Instalando pacotes

## Sumário

* [Introdução](#introdução)
* [Instalando bibliotecas](#instalando-bibliotecas)
* [Como saber se as bibliotecas foram instaladas?](#como-saber-se-as-bibliotecas-foram-instaladas)
* [Como desinstalar uma biblioteca?](#como-desinstalar-uma-biblioteca)

## Introdução

Quando estamos programando em Python, às vezes queremos realizar algum processamento que muito 
provavelmente já foi feito por outra pessoa.
Considere o caso de querermos calcular o 
[determinante](https://brasilescola.uol.com.br/matematica/determinantes-1.htm) da seguinte matriz:

```
1 2 3
4 5 6
7 8 9
```

1 2 3 1 2 
4 5 6 4 5
7 8 9 7 8

Seguindo as regras da matemática, o determinante seria 
((1*5*9)+(2*6*7)+(3*4*8)) - ((7*5*3)+(8*6*1)+(9*4*2))= 0.

Se fôssemos implementar um algoritmo para calcular o determinante de matrizes 3x3, ele seria o seguinte:

```python
def det(matrix: list) -> int:
	diag_principal = (
		(matrix[0][0] * matrix[1][1] * matrix[2][2]) + 
		(matrix[0][1] * matrix[1][2] * matrix[2][0]) + 
		(matrix[0][2] * matrix[1][0] * matrix[2][1])
	)
	diag_secundaria = (
		(matrix[2][0] * matrix[1][1] * matrix[0][2]) + 
		(matrix[2][1] * matrix[1][2] * matrix[0][0]) + 
		(matrix[2][2] * matrix[1][0] * matrix[0][1])
	)
	return diag_principal - diag_secundaria
```

Porém, para que se dar ao trabalho? Este código já foi implementado pela biblioteca 
[NumPy](https://numpy.org/doc/stable/reference/generated/numpy.linalg.det.html):

```python
import numpy as np
print(round(np.linalg.det([[1, 2, 3],[4, 5, 6],[7, 8, 9]])))
```

É para isto que bibliotecas existem: para evitar que reinventemos a roda toda vez que formos 
programar uma aplicação!

## Instalando bibliotecas

Existem duas maneiras de instalar bibliotecas: usando o comando `conda`, ou então o comando 
`pip`.

É sempre preferível instalar as bibliotecas com o comando `conda`, pois ele efetivamente 
"instala" a biblioteca na sua máquina. Por exemplo, se você fosse instalar a biblioteca 
Tensorflow, utilizada para processamento de imagens, e não posuísse os drivers mais atualizados 
da sua placa de vídeo, o `conda` os instalaria automaticamente para você. Com o comando `pip`, 
você precisaria instalar esses drivers por conta própria.

Além disso, `pip` não resolve conflitos entre bibliotecas. Se uma biblioteca precisa por 
exemplo do NumPy versão 1.09, e outra biblioteca precisa do NumPy versão 1.01, pode ser que a 
versão 1.05 do NumPy atenda aos requisitos de ambas as bibliotecas. O comando `conda` tentará 
verificar se este é o caso, e instalar as versões das bibliotecas que atendem todos os requisitos.

Já o comando `pip` copia-e-cola os pacotes numa pasta do ambiente virtual. Se houver algum 
conflito, você saberá porque a sua aplicação parou de funcionar...

Dito tudo isso, ainda haverão vezes que não será possível instalar uma biblioteca com o comando `conda`.
Nesse caso, não haverá jeito, e você precisará usar o comando `pip` mesmo.

### Passo-a-passo

1. Crie um novo ambiente virtual:

```bash
conda create --name test --yes
```

2. Ative-o:

```bash
conda activate test
```

3. Instale a biblioteca `pip` usando o comando `conda`:

```bash
conda install pip
```

**Por que estamos fazendo isso?** 

Toda vez que você criar um novo ambiente virtual, instale o `pip` nesse novo ambiente virtual. Senão
o Python usará o `pip` padrão, e as bibliotecas serão instaladas para o Python padrão (e não para
o Python do ambiente virtual).

4. Se você já souber quais pacotes quer instalar, você pode instalá-los listando-os nome por nome, pela
	linha de comando:

```bash
conda install numpy scipy matplotlib
```

```bash
pip install numpy scipy matplotlib
```


5. Ou, se você tiver clonado um repositório e houver um arquivo requirements.txt, você pode instalar todas
as bibliotecas deste arquivo com os seguintes comandos:

```bash
conda install --file requirements.txt
```

```bash
pip install --requirement requirements.txt
```

**Aviso:** note que às vezes não será possível instalar todos os pacotes de um arquivo requirements.txt com o 
`conda`. Nesse caso, você terá que abrir este arquivo com um editor de textos (como o bloco de notas), e instalar
pacote por pacote como no passo 4, até descobrir quais pacotes/bibliotecas só podem ser instalados com o pip.

## Como saber se as bibliotecas foram instaladas?

Você pode descobrir se os pacotes foram instalados corretamente digitando o comando

```bash
conda list
```

ou então o comando

```bash
pip list
```

Eles lhe mostrarão não apenas todas as bibliotecas/pacotes instalados no ambiente virtual atual, como também suas versões.

## Como desinstalar uma biblioteca?

Use o comando

```bash
conda uninstall <nome do pacote>
```

ou então 

```bash
pip uninstall <nome do pacote>
```

Para desinstalar as bibliotecas.
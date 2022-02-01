# Rodando testes

## Introdução

No decorrer deste curso, muitas atividades serão 
disponibilizadas com um arquivo `test.py` junto. Este
arquivo é um testador programado com a biblioteca 
[unittest](https://docs.python.org/3/library/unittest.html).

O objetivo do testador é validar se a atividade que você 
realizou foi feita corretamente ou não. Você **não deve** mexer
neste arquivo (a menos que seja para achar bugs no código!),
mas você **deve** executar este script.

As instruções a seguir servirão para qualquer arquivo `test.py`
disponibilizado durante este curso. Para facilitar as coisas,

## Passo-a-passo

Abra o arquivo [src/assignment/main.py](../src/assignment/main.py). 
O código-fonte dentro deste arquivo é o seguinte:

```python
def main():
    # apague o caractere # da linha abaixo
    # return 1 + 1
    pass  # apague esta linha

if __name__ == '__main__':
    main()
```

Simples, não? Você só precisa modificar o código-fonte de forma 
que ele fique da seguinte forma:

```python
def main():
    # apague o caractere # da linha abaixo
    return 1 + 1

if __name__ == '__main__':
    main()
```

Se você rodar esse script pela linha de comando 
(`python main.py`), verá que nada acontece. Isso porque este 
script não imprime nada na tela (comando `print`). Ele apenas 
retorna o valor 2.

O que você deve fazer a seguir é rodar o script `test.py`, para
verificar se o exercício foi feito corretamente. Abra o prompt
de comando, navegue até a pasta assignment com o comando `cd`,
e dê o comando `python test.py`. Se tudo estiver certo, você
deverá ver a seguinte tela:




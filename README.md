# Testes Automatizados com Pytest

Este repositório contém um exemplo prático do uso da ferramenta de teste automatizado **Pytest** com o plugin **pytest-cov** para geração de relatórios de cobertura de código.

## Conteúdo

- [Instalação](#instalação)
- [Como Executar os Testes](#como-executar-os-testes)
- [Relatório de Cobertura de Código](#relatório-de-cobertura-de-código)
- [Recursos](#recursos)
- [Prós e Contras do Pytest](#prós-e-contras-do-pytest)

---

## Instalação

Para começar, instale as dependências do projeto executando o seguinte comando:

```bash
pip install pytest pytest-cov
```

## Como Executar os Testes

Para executar os testes com o **Pytest**, utilize o comando abaixo:

```bash
pytest
```

Esse comando irá procurar automaticamente os arquivos de teste no diretório atual, executar os testes e exibir os resultados na linha de comando.

### Exemplo de Função Testada

O arquivo `math_functions.py` contém funções simples para operações matemáticas. Um exemplo:

```python
# math_functions.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
```

Os testes para essas funções estão definidos no arquivo `test_math_functions.py`:

```python
# test_math_functions.py
import math_functions

def test_add():
    assert math_functions.add(2, 3) == 5
```

### Executando os Testes com Cobertura de Código

Para gerar um relatório de cobertura de código, utilize o seguinte comando:

```bash
pytest --cov=math_functions
```

Esse comando executa os testes e calcula a porcentagem de linhas de código cobertas pelos testes.

## Relatório de Cobertura de Código

Para gerar um relatório de cobertura mais detalhado, como em formato **HTML**, execute:

```bash
pytest --cov=math_functions --cov-report=html
```

Após a execução, um relatório será gerado no diretório `htmlcov/`. Abra o arquivo `index.html` no seu navegador para visualizar o relatório completo.

## Recursos

- **Fixtures e Parametrização**: Pytest facilita a reutilização de código de teste através de **fixtures**, que configuram e limpam o ambiente de teste.
- **Integração Simples**: Pode ser integrado facilmente em pipelines de CI/CD, como Jenkins e GitLab CI.
- **Plugins**: Pytest suporta uma grande variedade de plugins, incluindo o **pytest-cov** para cobertura de código e **pytest-xdist** para execução em paralelo.

## Prós e Contras do Pytest

### Prós:
- **Simples de Usar**: Criação e execução de testes de forma intuitiva.
- **Altamente Extensível**: Suporte a plugins para aumentar a funcionalidade.
- **Cobertura de Código**: Relatórios detalhados sobre o que foi testado e o que não foi.
- **Suporte a Testes Parametrizados**: Reutilização de testes com diferentes conjuntos de dados.

### Contras:
- **Falta de GUI**: Para quem prefere uma interface gráfica, o Pytest pode parecer limitado.
- **Curva de Aprendizado para Funcionalidades Avançadas**: Algumas funcionalidades, como o uso de fixtures, podem ter uma curva de aprendizado mais íngreme.
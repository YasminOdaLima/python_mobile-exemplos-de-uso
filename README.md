# Aprenda a Criar Apps com Python e Flet 📱🐍

Bem-vindo ao repositório **Python Mobile com Flet**\!

Este espaço foi criado para ser um guia completo e prático, ensinando você a desenvolver aplicativos multiplataforma (com foco em mobile) utilizando apenas a linguagem de programação Python e o incrível framework Flet.

## ✨ Sobre o Flet

[Flet](https://flet.dev/) é um framework que permite criar aplicações interativas em tempo real com uma sintaxe simples e intuitiva, diretamente em Python. Ele renderiza a interface usando Flutter, garantindo um visual moderno e performático em todas as plataformas.

## 📂 Estrutura do Repositório

Este curso é dividido em módulos progressivos. Cada pasta representa um projeto ou um conjunto de conceitos, começando do básico e avançando para aplicativos mais complexos.

| Módulo | Pasta | Descrição |
| :--- | :--- | :--- |
| **01** | `1_basico` | Introdução aos conceitos e widgets fundamentais do Flet. É o ponto de partida ideal\! |
| **02** | `2_imc` | **Projeto Prático:** Uma calculadora de Índice de Massa Corporal (IMC). |
| **03** | `3_gerador_senhas`| **Projeto Prático:** Um aplicativo para gerar senhas seguras e personalizadas. |
| **04** | `4_noobank` | **Desafio:** Reconstrução da interface de um famoso banco digital para praticar layouts complexos. |
| **05** | `5_todo` | **Projeto Prático:** O clássico aplicativo de lista de tarefas (To-Do List). |
| **06**| `6_weather_app`| **Projeto Prático:** Um aplicativo que consome uma API para mostrar a previsão do tempo. |

-----

## 🚀 Como Começar

Para executar os projetos deste repositório em sua máquina, siga os passos abaixo.

### Pré-requisitos

  - **Python 3.7** ou superior instalado em seu sistema. Você pode baixá-lo em [python.org](https://www.python.org/downloads/).

### 1\. Clone o Repositório

```bash
git clone https://github.com/SEU-USUARIO/SEU-REPOSITORIO.git
cd SEU-REPOSITORIO
```

### 2\. Instale o Flet

Com o Python instalado, abra seu terminal e instale a biblioteca do Flet usando o `pip`:

```bash
pip install flet
```

### 3\. Execute um Aplicativo

Navegue até a pasta de um dos projetos e execute o arquivo Python principal com o comando `flet run`.

**Exemplo (executando a calculadora):**

```bash
# Navegue até a pasta do projeto
cd 7_calculadora

# Execute o app
flet run 7_calculadora.py
```

O Flet abrirá uma janela nativa em seu sistema operacional exibindo o aplicativo.

-----

## 📚 Detalhes do Módulo 1: Fundamentos do Flet

A pasta `1_basico` contém exemplos pequenos e focados, perfeitos para aprender um conceito de cada vez.

| Arquivo | Conceito Principal |
| :--- | :--- |
| `1_primeiro_app.py` | Configuração da janela e exibição do primeiro texto (`ft.Text`). |
| `2_botao_simples.py` | Criação de botões (`ft.ElevatedButton`) e resposta a eventos de clique (`on_click`). |
| `3_campo_texto.py`| Coleta de dados do usuário com o campo de entrada (`ft.TextField`). |
| `4_lista_cores.py` | Uso de listas suspensas (`ft.Dropdown`) para dar opções ao usuário. |
| `5_layout_basico.py`| Organização de elementos na tela com Linhas (`ft.Row`) e Colunas (`ft.Column`). |
| `5a_desafio1.py` | **Desafio:** Um aplicativo "Criador de Perfil" que valida dados e mostra o resultado. |
| `6_contador.py` | Manipulação de estado com um contador interativo que muda de cor. |
| `7_calculadora.py` | **Mini-Projeto:** Uma calculadora funcional com as 4 operações básicas. |

## 🤝 Contribuições

Contribuições são sempre bem-vindas\! Se você encontrar um bug, tiver uma sugestão de melhoria ou quiser adicionar um novo projeto-exemplo, sinta-se à vontade para abrir uma **Issue** ou um **Pull Request**.

-----

Feito com ❤️ e Python\!
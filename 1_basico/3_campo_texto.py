import flet as ft

def main(page: ft.Page):
    page.title = "Campo de texto"
    page.title = ft.padding.only(top=40, left=20, right=20, bottom= 20) # Padding superior para área segura

    # Criando um campo onde o usuário pode digitar
    campo_nome = ft.TextField(
        label="Digite seu nome aqui", # Texto de orientação 
        width=300, # Largura do campo
        border_color=ft.Colors.BLUE # Cor da borda
    )

    # Texto que mostrará a resposta
    resposta = ft.Text(
        value="", # Inicialmente vazio
        size=18,
        text_align=ft.TextAlign.CENTER
    )

    def processar_nome(evento):
        """
        Função que paga o texto digitado pelo usuário e faz algo com ele.
        """
        # Pegando o valor digitado no campo 
        nome_digitado = campo_nome.value

        # Verificando se o usuário realmente digitou algo
        if nome_digitado == "" or nome_digitado is None:
            resposta.value = "⚠️ Por Favor, digite seu nome!"
            resposta.color = ft.Colors.RED 
        elif len(nome_digitado) < 2:
            resposta.value = "⚠️ Nome muito curto!"
            resposta.color= ft.Colors.ORANGE
        else:
            resposta.value = f"✅ Olá, {nome_digitado}! Prazer em conhcêlo(a)!"
            resposta.color = ft.Colors.GREEN

        # Atualizando a interface
        page.update()

    # Botao para processar o nome
    botao_ok = ft.ElevatedButton(
        text="Confirmar",
        on_click=processar_nome,
        width=150
    )

    # Adicionar elementos à página
    page.add(
        ft.Text("Vamos nos conhecer! 😊", size=22, weight=ft.FontWeight.BOLD),
        campo_nome,
        botao_ok,
        resposta
    )

ft.app(target=main)
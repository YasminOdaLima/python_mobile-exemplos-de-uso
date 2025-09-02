import flet as ft

def main(page: ft.Page):
    page.title = "Gerenciador de Tarefas"
    page.padding = ft.padding.only(top=40, left=20, right=20, bottom=20)
    page.scroll = ft.ScrollMode.AUTO

    # Lista para armazenar tarefas
    tarefas = []

    # Campos de entrada
    campo_tarefa = ft.TextField(label="Digite uma tarefa", width=400)
    campo_categoria = ft.Dropdown(
        label="Categoria",
        width=200,
        options=[
            ft.dropdown.Option("Trabalho"),
            ft.dropdown.Option("Estudo"),
            ft.dropdown.Option("Pessoal"),
            ft.dropdown.Option("Outros")
        ]
    )
    campo_prioridade = ft.Dropdown(
        label="Prioridade",
        width=200,
        options=[
            ft.dropdown.Option("Baixa"),
            ft.dropdown.Option("Média"),
            ft.dropdown.Option("Alta")
        ]
    )

    # Lista visual de tarefas
    lista_tarefas = ft.Column(spacing=10)

    # Área de status
    status_info = ft.Text("Nenhuma tarefa adicionada ainda.", size=14, color=ft.Colors.GREY_600)

    def atualizar_status():
        """Atualiza a área de status com o total de tarefas"""
        total = len(tarefas)
        if total == 0:
            status_info.value = "Nenhuma tarefa cadastrada."
        else:
            status_info.value = f"Total de tarefas: {total}"
        page.update()

    def adicionar_tarefa(e):
        """Adiciona uma nova tarefa"""
        nome = campo_tarefa.value
        categoria = campo_categoria.value
        prioridade = campo_prioridade.value

        if not nome or not categoria or not prioridade:
            status_info.value = "⚠️ Preencha todos os campos!"
            status_info.color = ft.Colors.RED
            page.update()
            return

        # Estrutura da tarefa
        tarefa = {
            "nome": nome,
            "categoria": categoria,
            "prioridade": prioridade,
            "concluida": False
        }
        tarefas.append(tarefa)

        # Criando item visual
        item_tarefa = criar_item_tarefa(tarefa)
        lista_tarefas.controls.append(item_tarefa)

        # Resetando os campos
        campo_tarefa.value = ""
        campo_categoria.value = None
        campo_prioridade.value = None

        status_info.value = "✅ Tarefa adicionada com sucesso!"
        status_info.color = ft.Colors.GREEN
        atualizar_status()
        page.update()

    def criar_item_tarefa(tarefa):
        """Cria o cartão visual de uma tarefa"""
        nome = ft.Text(tarefa["nome"], size=16, weight=ft.FontWeight.BOLD)
        categoria = ft.Text(f"Categoria: {tarefa['categoria']}", size=14)
        prioridade = ft.Text(f"Prioridade: {tarefa['prioridade']}", size=14)

        checkbox = ft.Checkbox(
            label="Concluída",
            value=tarefa["concluida"],
            on_change=lambda e: marcar_concluida(tarefa, nome, checkbox)
        )

        botao_remover = ft.ElevatedButton(
            "Remover",
            bgcolor=ft.Colors.RED,
            color=ft.Colors.WHITE,
            on_click=lambda e: remover_tarefa(tarefa, item_container)
        )

        item_container = ft.Container(
            content=ft.Column([
                nome, categoria, prioridade, checkbox, botao_remover
            ]),
            bgcolor=ft.Colors.GREY_200,
            padding=10,
            border_radius=10
        )

        return item_container

    def marcar_concluida(tarefa, texto_nome, checkbox):
        """Marca uma tarefa como concluída"""
        tarefa["concluida"] = checkbox.value
        if tarefa["concluida"]:
            texto_nome.color = ft.Colors.GREEN
        else:
            texto_nome.color = ft.Colors.BLACK
        page.update()

    def remover_tarefa(tarefa, item_container):
        """Remove uma tarefa da lista"""
        if tarefa in tarefas:
            tarefas.remove(tarefa)
            lista_tarefas.controls.remove(item_container)
            status_info.value = "🗑️ Tarefa removida!"
            status_info.color = ft.Colors.ORANGE
            atualizar_status()
            page.update()

    # Botão principal
    botao_adicionar = ft.ElevatedButton(
        "Adicionar Tarefa",
        on_click=adicionar_tarefa,
        bgcolor=ft.Colors.BLUE,
        color=ft.Colors.WHITE
    )

    # Layout principal
    layout_principal = ft.Column(
        [
            ft.Text("📝 Gerenciador de Tarefas", size=26, weight=ft.FontWeight.BOLD),
            campo_tarefa,
            ft.Row([campo_categoria, campo_prioridade], spacing=10),
            botao_adicionar,
            ft.Divider(),
            status_info,
            lista_tarefas
        ],
        spacing=15,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )

    page.add(layout_principal)

ft.app(target=main)



    

import flet as ft

def main(page: ft.Page):
    page.title = 'meu app de previsao do tempo'
    page.window.height = 720
    page.window.width = 400
    
   
    cntPrincipal = ft.Container(
    bgcolor="#3f6cb4",
    padding=10,
    height=page.window.height * 0.90,
    width=page.window.width * 0.90,
    content=ft.Column(
        alignment=ft.MainAxisAlignment.START,  # Alinha os filhos no topo (vertical)
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,  # Centraliza filhos (horizontal)
        spacing=10,
    )
)
    
    ### Container Superior ######################
    cntSuperior = ft.Container(
        height=100,
        content=ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=10,
        )
    )
    
    pesqLocal = ft.TextField(
        bgcolor='white',
        border_color='white',
        border_radius=10,
        width=290,
        hint_text='digite sua cidade',
        hint_style=ft.TextStyle(size=14, color='#778899'),
        text_align=ft.TextAlign.CENTER,
        text_style=ft.TextStyle(color='#000000', size=16),
        value='Sao Paulo,BR',
    )
    
    btnPesquisar = ft.IconButton(icon=ft.icons.SEARCH)
    
    ############################ CONTAINER CENTRAL #############################
    cntCentral = ft.Container(
    height=200,
    width=220,  # Largura fixa (opcional)
    alignment=ft.alignment.center,  # Centraliza o conteúdo interno
    content=ft.Column(
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=10,
    )
)
    
    cntCentralLinha1 = ft.Row(
        alignment=ft.MainAxisAlignment.CENTER,
        controls=[
            ft.Text(
                "São Caetano Do Sul",
                font_family='Roboto Medium',
                color='white',
                size=28,
                weight=ft.FontWeight.BOLD,
            )
        ]
    )
    
    cntCentralLinha2 = ft.Row(
        alignment=ft.MainAxisAlignment.CENTER,
        controls=[
            ft.Image(
                src="sol.png",
                width=50,
                height=50,
                
            )
        ]
    )
    
    cntCentralLinha3 = ft.Row(
        alignment=ft.MainAxisAlignment.CENTER,
        controls=[
            ft.Text(
                "24°C",
                font_family='Roboto Medium',
                color='white',
                size=18,
            )
        ]
    )
    
    cntCentralLinha4 = ft.Row(
        alignment=ft.MainAxisAlignment.CENTER,
        controls=[
            ft.Text(
                "75%",
                font_family='Roboto Medium',
                color='white',
                #size=18,
            )
        ]
    )
    
    # Adiciona as linhas ao cntCentral
    cntCentral.content.controls.extend([cntCentralLinha1, cntCentralLinha2, cntCentralLinha3,cntCentralLinha4])
    
    # Adiciona os controles ao cntSuperior
    cntSuperior.content.controls.extend([pesqLocal, btnPesquisar])
    
    # Adiciona cntSuperior e cntCentral ao cntPrincipal
    cntPrincipal.content.controls.extend([cntSuperior, cntCentral])
    
    # Adiciona cntPrincipal à página
    page.add(cntPrincipal)

ft.app(target=main)
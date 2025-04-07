import flet as ft


def main(page:ft.Page):
    #page.bgcolor=ft.colors.BLACK
    page.title='meu app de previsao do tempo'
    page.window.height=720
    page.window.width=400
    
    
    ######--------------------------------------------##########
    #page.add(ft.Text(value='testando aplicação web',color='white'))
    
    cntPrincipal=ft.Container(
        bgcolor="#3f6cb4",
        padding=10,
        height=page.window.height *0.90 ,
        width=page.window.width * 0.90 ,
        content=ft.Column(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            height=page.window.height *0.90,
            width=page.window.width *0.90
            
        )
        
        
    )
    ###Container superipor######################
    cntSuperior = ft.Container(
         #bgcolor="white",
         height=100,
         content=ft.Row(
             
         )
        
    )
    
     ####containerSuperior texto
    
    pesqLocal=ft.TextField(
        bgcolor='white',
        border_color='white',
        border_radius=10,
        width=290,
        hint_text='digite sua cidade',
        hint_style=ft.TextStyle(
            size=14,
            color='#778899'
            
        ),
        text_align=ft.TextAlign.CENTER,
        text_style=ft.TextStyle(
            color='#000000',
            size=16
        ),
        value='Sao Paulo,BR',
    )
    ####containerSuperior botao para executar a pesquisa
    
    btnPesquisar=ft.IconButton(
        icon=ft.icons.SEARCH,
    )
    
    controls = [cntPrincipal]
    cntPrincipal.content.controls.append(cntSuperior)
    cntSuperior.content.controls.append(pesqLocal)
    cntSuperior.content.controls.append(btnPesquisar)
    page.add(*controls)
    
    
   
    


    



ft.app(target=main)
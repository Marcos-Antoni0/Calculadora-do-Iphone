import flet as ft
from decimal import Decimal

botoes = [
    {'operador': 'AC', 'fonte': ft.colors.WHITE, 'fundo': ft.colors.BLUE_GREY_100},
    {'operador': '≤', 'fonte': ft.colors.WHITE, 'fundo': ft.colors.BLUE_GREY_100},
    {'operador': '%', 'fonte': ft.colors.WHITE, 'fundo': ft.colors.BLUE_GREY_100},
    {'operador': '/', 'fonte': ft.colors.WHITE, 'fundo': ft.colors.ORANGE},
    {'operador': '7', 'fonte': ft.colors.WHITE, 'fundo': ft.colors.WHITE24},
    {'operador': '8', 'fonte': ft.colors.WHITE, 'fundo': ft.colors.WHITE24},
    {'operador': '9', 'fonte': ft.colors.WHITE, 'fundo': ft.colors.WHITE24},
    {'operador': '*', 'fonte': ft.colors.WHITE, 'fundo': ft.colors.ORANGE},
    {'operador': '4', 'fonte': ft.colors.WHITE, 'fundo': ft.colors.WHITE24},
    {'operador': '5', 'fonte': ft.colors.WHITE, 'fundo': ft.colors.WHITE24},
    {'operador': '6', 'fonte': ft.colors.WHITE, 'fundo': ft.colors.WHITE24},
    {'operador': '-', 'fonte': ft.colors.WHITE, 'fundo': ft.colors.ORANGE},
    {'operador': '1', 'fonte': ft.colors.WHITE, 'fundo': ft.colors.WHITE24},
    {'operador': '2', 'fonte': ft.colors.WHITE, 'fundo': ft.colors.WHITE24},
    {'operador': '3', 'fonte': ft.colors.WHITE, 'fundo': ft.colors.WHITE24},
    {'operador': '+', 'fonte': ft.colors.WHITE, 'fundo': ft.colors.ORANGE},
    {'operador': '0', 'fonte': ft.colors.WHITE, 'fundo': ft.colors.WHITE24},
    {'operador': '.', 'fonte': ft.colors.WHITE, 'fundo': ft.colors.WHITE24},
    {'operador': '=', 'fonte': ft.colors.WHITE, 'fundo': ft.colors.ORANGE},
]

def main(page: ft.Page):
    page.bgcolor = '#000'
    page.window_resizable = False
    page.window_width = 300
    page.window_height = 390
    page.title = 'Calculadora'
    page.window_always_on_top = True

    result = ft.Text(value="0", color= ft.colors.WHITE, size=20)

    def calculate(operador, value_at):
        try:
            value = eval(value_at) # Função capaz de decodificar string em números e operadores aritméticos

            if operador == '%':
                value /= 100


            elif operador == '≤':
                value = -value

        except:
            return 'Error'
        
        digists = min(abs(Decimal(value).as_tuple().exponent), 5)
        return format(value, f'.{digists}f')


    def select(e):
        value_at = result.value if result.value not in ('0', 'Error') else '' # verificando se o resultado é diferente de zero
        value = e.control.content.value # Pegando botão que o usuário clicou

        if value.isdigit(): # Verificando se o valor é um digito
            value = value_at + value # Concatenando todos valores digitados
        elif value == 'AC': # Caso clique em AC o valor será zerado
            value = '0'
        else: # Nesse o resultado só pode ser os operadores matematicos
            if value_at and value_at[-1] in ('/', '*', '-', '+', '.'): # Verificando se o valor atual existe e se o ultimo elemento digitado está entre ('/', '*', '-', '+', '.')
                value_at = value_at[:-1] # Se for o caso, o valor menos o ultimo elemento digitado (operador)

            value = value_at + value # Então quero que meu value seja igual ao valor atual mais o valor

            if value[-1] in ('=', '%', '≤'):
                value = calculate(operador=value[-1], value_at=value_at)

        result.value = value
        result.update()

    display = ft.Row(
        width=250,
        controls=[result],
        alignment= 'end',
    )

    btn = [ft.Container(
        content=ft.Text(value=btn['operador'], color=btn['fonte']),
        width=50,
        height=50,
        bgcolor=btn['fundo'],
        border_radius=100,
        alignment=ft.alignment.center,
        on_click=select
    ) for btn in botoes]

    keyboard = ft.Row(
        width=250,
        wrap=True,
        controls=btn,
        alignment='end'
    )

    page.add(display, keyboard)

ft.app(target=main)
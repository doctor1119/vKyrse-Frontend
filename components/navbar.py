from dash import html

def create_navbar():
    navbar = html.Div([
        html.Ul([
            html.Li(html.A('О проекте', href='/')),
            html.Li(html.A('Аналитика', href='/currency-analysis')),
            html.Li(html.A('Контакты', href='/contact')),
        ], style={
            'list-style-type': 'none',
            'padding': 0,
            'height': '100vh',  # Высота на всю высоту окна просмотра
            'width': '200px',  # Ширина блока навигации
            'background-color': '#f0f0f0',  # Цвет фона
            'position': 'fixed',  # Фиксированное положение
        })
    ], style={'flex': '0 0 200px'})  # Задаем фиксированную ширину для блока навигации
    return navbar


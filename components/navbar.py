from dash import html


def create_navbar():
    navbar_style = {
        'list-style-type': 'none',
        'margin': 0,
        'padding': '40px 16px 0 16px',
        'height': '100vh',
        'width': '270px',
        'background-color': '#252B33E8',
        'position': 'fixed',
    }

    logo_style = {
        'height': '50px',
        'margin-bottom': '16px',
    }

    title_style = {
        'color': '#000',  # Цвет текста названия приложения
        'margin-bottom': '16px',  # Отступ снизу названия приложения
        'font-size': '20px',  # Размер шрифта названия приложения
    }

    # link_style = {
    #     'display': 'block',
    #     'color': '#000',
    #     'padding': '16px',
    #     'text-decoration': 'none',
    #     'font-family': 'Inter',
    #     'font-size': '26px',
    #     # 'font-weight': '500',
    #     # 'line-height': '31.47px',
    #     'text-align': 'center',
    # }

    # hover_style = {
    #     'background-color': '#F9F9FC',
    #     'border-radius': '20px',
    #     'margin': '16px 0',
    #     'display': 'flex',
    #     'align-items': 'center',
    #     'justify-content': 'center',
    #     'height': '40px',
    #     'width': '100%',
    #     'padding': '0 16px',
    # }

    navbar = html.Div([
        html.Ul([
            # html.Img(src='/assets/logo_svg.svg', className='logo'),
            html.Li(html.A('О проекте', href='/', className='nav-link nav-item')),
            html.Li(html.A('Аналитика', href='/currency-analysis', className='nav-link nav-item')),
            html.Li(html.A('Контакты', href='/contact', className='nav-link nav-item')),
        ], style=navbar_style)
    ], style={'flex': '0 0 200px'})

    return navbar

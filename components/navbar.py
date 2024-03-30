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

    navbar = html.Div([
        html.Ul([
            # html.Img(src='/assets/logo_svg.svg', className='logo'),
            html.Li(html.A('О проекте', href='/', className='nav-link nav-item')),
            html.Li(html.A('Аналитика', href='/currency-analysis', className='nav-link nav-item')),
            html.Li(html.A('Контакты', href='/contact', className='nav-link nav-item')),
        ], style=navbar_style)
    ], style={'flex': '0 0 200px'})

    return navbar

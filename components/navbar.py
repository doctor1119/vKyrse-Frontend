from dash import html


def create_navbar():
    navbar_style = {
        'list-style-type': 'none',
        'margin': 0,
        'padding': '40px 16px 0 16px',
        'height': '120px',
        'width': '100%',
        'background-color': '#1E1E1E',
        'position': 'fixed',
        'top': 0,  # Указываем, чтобы навбар был прижат к верху страницы
        'display': 'flex',  # Используем flexbox для центрирования элементов
        'z-index': '10',
    }

    navbar = html.Div([
        html.H1("вКурсе", className="header-text", style={'color': 'white', 'margin-left': '20px'}),
        #почему эта надпись уехала вниз, я не знаю
        html.Img(src='/assets/ris1.png', height='40px', style={'margin-left': '10px'}),
        html.Ul([
            html.Li(html.A('О проекте', href='/', className="nav-link", style={'margin-left': '300px'})),
            html.Li(
                html.A('Аналитика', href='/currency-analysis', className="nav-link", style={'margin-left': '65px'})),
            html.Li(html.A('Контакты', href='/contact', className="nav-link", style={'margin-left': '65px'})),
        ], style={'margin': 0, 'padding': 0, 'display': 'flex', 'list-style-type': 'none',
                  }),
        html.A(html.Button(id='email-button', children="@", className="email-link", style={'margin-left': '430px'}),
               href='CIFRA@gmail.com')
    ], style=navbar_style)

    return navbar

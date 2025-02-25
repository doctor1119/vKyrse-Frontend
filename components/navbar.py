from dash import html
import dash_bootstrap_components as dbc

def create_navbar():
    navbar_style = {
        'list-style-type': 'none',
        'margin': 0,
        #'padding': '40px 16px 0 16px',
        'height': '120px',
        'width': '100%',
        'background-color': '#1E1E1E',
        'position': 'fixed',  # Зафиксировать навбар
        'top': 0,
        'z-index': 1000, # Устанавливаем z-index для того, чтобы навбар был поверх других элементов страницы
    }

    navbar = html.Div([
        html.H1("вКурсе", className="header-text", style={
            'position': 'absolute',
            'top': '45%',
            'left': '7%',
            'transform': 'translate(-50%, -50%)',
            'text-align': 'center',
            'color': 'white',
        }),
        html.Img(src='/assets/ris1.png', style={
            'position': 'relative',
            'width': '7vw',
            'height': '4vw',
            'top': '45%',
            'left': '15%',
            'transform': 'translate(-50%, -50%)',
            'text-align': 'center',
        }),
        html.Ul([
            html.Li(html.A('О проекте', href='/',
                           className="nav-link", style={
            'position': 'absolute',
            'height': '50px',
            'top': '55%',
            'left': '38%',
            'transform': 'translate(-50%, -50%)',
            'text-align': 'center',
                })),
            html.Li(
                html.A('Аналитика', href='/currency-analysis', className="nav-link", style={
                    'position': 'absolute',
                    'height': '50px',
                    'top': '55%',
                    'left': '50%',
                    'transform': 'translate(-50%, -50%)',
                    'text-align': 'center',
                })),
            html.Li(html.A('Контакты', href='/contact', className="nav-link", style={
                'position': 'absolute',
                'height': '50px',
                'top': '55%',
                'left': '62%',
                'transform': 'translate(-50%, -50%)',
                'text-align': 'center',
            })),
        ], style={'margin': 0, 'padding': 0, 'display': 'flex', 'list-style-type': 'none',
                  }),
        html.A(html.Button(id='email-button', children="@", className="email-link", style={
            'position': 'absolute',
            'top': '40%',
            'right': '7%',
            'transform': 'translate(-50 %, -50 %)',
        }),
               href='mailto:ivan@sample.com'),
        html.A(
            html.Img(src='/assets/link-tg.png', className="tg-link"),
            href='https://t.me/parfenowakate',
            style={
                'position': 'absolute',
                'top': '52%',
                'right': '5%',
                'left': '95%',
                'transform': 'translate(-50%, -50%)',
            }
        )
    ], style=navbar_style)

    return navbar

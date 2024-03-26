from dash import html


def create_navbar():
    navbar_style = {
        'list-style-type': 'none',
        'margin': 0,
        'padding': 0,
        'height': '100vh',
        'width': '200px',
        'background-color': '#f0f0f0',
        'position': 'fixed',
    }

    link_style = {
        'display': 'block',
        'color': '#000',
        'padding': '8px',
        'text-decoration': 'none',
    }

    hover_style = {
        'background-color': '#ddd',
    }

    navbar = html.Div([
        html.Ul([
            html.Li(html.A('О проекте', href='/', style=link_style), style=hover_style),
            html.Li(html.A('Аналитика', href='/currency-analysis', style=link_style), style=hover_style),
            html.Li(html.A('Контакты', href='/contact', style=link_style), style=hover_style),
        ], style=navbar_style)
    ], style={'flex': '0 0 200px'})

    return navbar

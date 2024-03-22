from dash import html


def create_main_layout():
    layout = html.Div([
        html.Div(id='page-content', children=[
            html.H1("О нашем проекте", className="text-center mt-5"),
            html.P("Этот проект создан для демонстрации того, как легко можно добавить текст на страницу с помощью "
                   "Dash.", style={'fontSize': '18px', 'color': 'green'})
        ]),
    ])
    return layout

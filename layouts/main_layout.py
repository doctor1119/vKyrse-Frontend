from dash import html


def create_main_layout():
    layout = html.Div([
        html.Div(children=[
            html.H1("Кто мы?", className="header-text"),
            html.P("Мы команда инициативных студентов, создавших для вас продукт, который позволит делать прогнозы  и "
                   "анализировать курса рубля", className="text")
        ], className="block-text"),
        html.Div(children=[
            html.H1("О чем?", className="header-text"),
            html.P("Мы тщательно подобрали для вас самые разнообразные и последние новости, которые больше всего "
                   "могут влиять на курс рубля.", className="text")
        ], className="block-text"),
        html.Div(
            children=[
                html.Div("НА НАШЕЙ ПЛАТФОРМЕ ВЫ СМОЖЕТЕ", className='gradient-bar')
            ]
        )

    ])
    return layout

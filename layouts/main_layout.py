from dash import html
import dash_bootstrap_components as dbc


def create_main_layout():
    layout = html.Div([
        html.Div(children=[
            #html.H1("Кто мы?", className="header-text"),
            html.P("Мы команда инициативных студентов, создавших для вас продукт, который позволит делать прогнозы  и "
                   "анализировать курса рубля", className="text")
        ], className="block-html", style={'marginTop': '60px'}),  #, style={'marginTop': '60px'} добавляет отступ от навбара
        html.Div(children=[
            html.H1("О чем?", className="header-text"),
            html.P("Мы тщательно подобрали для вас самые разнообразные и последние новости, которые больше всего "
                   "могут влиять на курс рубля.", className="text")
        ], className="block-html"),
        html.Div(
            children=[
                html.Div("НА НАШЕЙ ПЛАТФОРМЕ ВЫ СМОЖЕТЕ", className='gradient-bar')
            ], className="block-html"
        ),
        dbc.Row([
            dbc.Col(dbc.Card([
                dbc.CardBody([
                    html.P("Быть в курсе всех актуальных событий и новостей", className="block-text"),
                ])
            ]),
            ),
            dbc.Col(dbc.Card([
                dbc.CardBody([
                    html.P("Прогнозировать изменения курса рубля", className="block-text"),
                ])
            ])),
        ], className='mb-4'),
        dbc.Row([
            dbc.Col(dbc.Card([
                dbc.CardBody([
                    html.P("Анализировать текущую обстановку на рынке", className="block-text"),
                ])
            ]),
            ),
            dbc.Col(dbc.Card([
                dbc.CardBody([
                    html.P("Создавать свою стратегию инвестирования", className="block-text"),
                ])
            ])),
        ], className='mb-4'),
    ])
    return layout

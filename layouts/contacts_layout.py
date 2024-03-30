from dash import html, dcc

def create_contacts_layout():
    layout = html.Div([
        html.H1(html.Strong("Контакты"), className="text-center mt-5"),
        html.Br(),
        html.P(html.Strong('Мы всегда открыты к новым предложениям и сотрудничеству.  Наша команда стремится сделать для вас лучший сервис по анализу новостей и событий. Поэтому будем рады услышать ваши честные отзывы!')),
        #html.Br(),
        html.P(html.Strong('Вы можете связаться с нами:'), className="text-center mt-5"),
        html.P(html.Strong('Email:'), style={'margin-left': '200px','display': 'inline-block', 'width': '60px'}),
        html.P('teamCIFRA@gmail.com', style={'display': 'inline-block', 'margin-right': '350px'}),
        html.P(html.Strong('Tg:'), style={'display': 'inline-block', 'width': '50px'}),
        html.P('@teamCIFRA', style={'display': 'inline-block'}),
        html.Br(),
        html.Br(),
        html.Br(),
        html.P(html.Strong('Наша команда')),
        html.Br(),
        html.Div([
            # Первый столбец
            html.Div([
                html.Img(src='/assets/avatar.png', style={'width': '10%', 'height': '10%'}),
                html.Br(),
                html.Br(),
                html.Img(src='/assets/avatar.png', style={'width': '10%', 'height': '10%'}),
                html.Br(),
                html.Br(),
                html.Img(src='/assets/avatar.png', style={'width': '10%', 'height': '10%'}),
                html.Br(),
                html.Br(),
                html.Img(src='/assets/avatar.png', style={'width': '10%', 'height': '10%'}),
            ], style={'width': '25%', 'height': '100%','float': 'left'}),

            html.Div([
            html.P('Имя 1', className="text"),
            html.P('Имя 2',className="text"),
            html.P('Имя 3', className="text"),
            html.P('Имя 4', className="text"),
                ], className="block-html"),


        ])
    ])

    return layout
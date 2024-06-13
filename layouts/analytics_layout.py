from dash import html, dcc
import dash_bootstrap_components as dbc
import plotly.graph_objs as go

def create_analytics_layout():
    layout = html.Div([
        # 1 слайд
        html.Div([
            # Фоновый слой
            html.Div(style={
                'background-image': 'url(/assets/digital-increasing-bar-graph-with-businessman-hand-overlay.png)',
                'height': '90vh',
                'background-size': 'cover',
                'background-position': 'top center',
                'position': 'absolute',
                'width': '100%',
                'z-index': '-1',
                'margin': '0',  # Убираем отступы слева и справа
            }),
            # Контентный слой
            html.Div([
                html.A('Текст', className='text-bubble-2', style={
                    'height': '30vw',
                    'width': '30vw',
                    'display': 'flex',
                    'align-items': 'center',
                    'justify-content': 'center',
                    'text-decoration': 'none',
                    'position': 'absolute',
                    'top': '15%',
                    'left': '5%',
                }),
            ], style={
                'display': 'flex',
                'flex-direction': 'column',
                'align-items': 'center',
                'justify-content': 'center',
                'height': '100%',
                'text-align': 'center',
                'position': 'relative',
            }),
        ], style={
            'height': '90vh',
            'position': 'relative',
            'z-index': '-1',
        }),

        # Отдельный маленький слайд для выбора даты
        html.Div([
            html.Div([
                html.Img(src='/assets/calendar_month.png', style={'height': '2vw', 'margin-right': '1vw'}),
                dcc.DatePickerRange(
                    id='date-picker-range',
                    start_date_placeholder_text="Начало",
                    end_date_placeholder_text="Конец",
                    calendar_orientation='horizontal',
                ),
                html.Button('Загрузить данные', id='load-data-button', n_clicks=0, className='btn btn-primary ml-3', style={
                    'background-color': '#30D9CA',
                    'border-color': '#30D9CA',
                    'margin-left': '1vw',
                }),
            ], style={
                'display': 'flex',
                'align-items': 'center',
                'margin-left': '10%',
                'margin-top': '5vh',
            }),
        ], style={'height': 'auto', 'z-index': '-1'}),

        # 2 и 3 слайд (объединены)
        html.Div([
            dbc.Row([
                dbc.Col(dbc.Card([
                    dbc.CardBody([
                        html.H4("График 1", className="card-title"),
                        dcc.Graph(id='graph-1', figure=go.Figure()),
                    ])
                ]), width=6, style={'margin-left': '5%'}),
                dbc.Col(
                    html.Div([
                        html.A(
                            'На этом графике можно посмотреть, как меняется курс рубля по отношению к доллару за конкретный промежуток времени',
                            className='text-bubble-2', style={
                                'height': 'auto',
                                'width': 'auto',
                                'padding': '2vw',
                                'display': 'flex',
                                'align-items': 'center',
                                'justify-content': 'center',
                                'z-index': '-1',
                                'text-decoration': 'none',
                                'margin-left': '2vw',
                                'margin-top': '2vw',
                            }),
                    ]),
                    width=4,
                    style={'z-index': '-1', 'margin-left': '2vw', 'margin-top': '2vw'}
                    # Добавляем отступы для выравнивания текста
                ),  # Текст справа от графика 1
            ], className='mb-4', style={'z-index': '-1', 'margin-top': '5vh'}),  # Перемещаем ниже

            dbc.Row([
                dbc.Col(dbc.Card([
                    dbc.CardBody([
                        html.H4("График 2", className="card-title"),
                        dcc.Graph(id='graph-2', figure=go.Figure()),
                    ])
                ]), width=6, style={'margin-left': '5%'}),
            ], className='mb-4', style={'margin-top': '5vh'}),
        ], style={'height': '180vh', 'position': 'relative', 'z-index': '-1',}),

        # Подвал
        html.Div([
            html.H1("вКурсе", className="header-text", style={
                'position': 'absolute',
                'top': '45%',
                'left': '47%',
                'transform': 'translate(-50%, -50%)',
                'text-align': 'center',
                'color': 'white',
            }),
            html.Img(src='/assets/ris1.png', style={
                'position': 'absolute',
                'width': '7vw',
                'height': '4vw',
                'top': '45%',
                'left': '55%',
                'transform': 'translate(-50%, -50%)',
                'text-align': 'center',
            }),
        ], style={
            'background-color': 'rgba(30, 30, 30, 1)',
            'height': '15vh',
            'background-size': 'cover',
            'background-position': 'center center',
            'position': 'relative',
            'z-index': '-1',
        }),
    ])

    return layout

from dash import html, dcc
import dash_bootstrap_components as dbc
import plotly.graph_objs as go

def create_analytics_layout():
    layout = html.Div([
        # 1 слайд
        html.Div([
            html.Div([
                html.H1("ТЕКУЩИЙ КУРС ВАЛЮТЫ", className='main-layout-header-text-2', style={'text-align': 'left', 'margin-top': '3%'}),
                html.Div([
                    html.Img(src='/assets/bookmarks.png', style={'height': '3vw', 'margin-right': '0.5vw'}),
                    html.H2("На этом графике можно посмотреть, как меняется курс рубля по отношению к доллару за конкретный промежуток времени.",
                            className='text', style={'display': 'inline', 'vertical-align': 'middle', 'text-align': 'left'}),
                ], style={'display': 'flex', 'justify-content': 'flex-start', 'align-items': 'center', 'margin-top': '1%'}),
            ], style={'margin-left': '3%', 'width': '50%'}),
            html.Div([
                html.Img(src='/assets/currency_ruble.png', style={'height': '35vw', 'position': 'relative', 'margin-left': '60%', 'margin-top': '-5%'}),
                html.Img(src='/assets/attach_money.png',
                         style={'height': '26vw', 'position': 'relative', 'margin-left': '70%', 'margin-top': '-28%'}),
            ], style={'position': 'relative', 'width': '100%', 'height': '0'}),
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
                    'z-index': '10'
                }),
            ], style={
                'display': 'flex',
                'align-items': 'center',
                'margin-left': '3%',
                'margin-top': '1%',
                'position': 'relative',
            }),
            dbc.Row([
                dbc.Col(dbc.Card([
                    dbc.CardBody([
                        html.H4("График 1", className="card-title"),
                        dcc.Graph(id='graph-1', figure=go.Figure(), style={'height': '50vh'}),
                    ])
                ]), width=6, style={'margin-left': '3%'}),
            ], className='mb-4', style={'z-index': '-1', 'margin-top': '1%'}),
        ], style={'height': '90vh', 'position': 'relative', 'z-index': '-1'}),

        # 2 слайд
        html.Div([
            html.Div([
                html.H1("КУРС ВАЛЮТЫ ПО СОБЫТИЯМ", className='main-layout-header-text-2', style={'text-align': 'left', 'margin-top': '3%'}),
                html.Div([
                    html.Img(src='/assets/bookmarks.png', style={'height': '3vw', 'margin-right': '0.5vw'}),
                    html.H2("Вы можете настроить графики по событиям и увидеть, какое из них оказало наибольшее влияние курс рубля за месяц.", className='text', style={'display': 'inline', 'vertical-align': 'middle', 'text-align': 'left'}),
                ], style={'display': 'flex', 'justify-content': 'flex-start', 'align-items': 'center', 'margin-top': '1%'}),
            ], style={'margin-left': '3%', 'width': '50%'}),
            html.Div([
                html.Img(src='/assets/currency_ruble.png', style={'height': '35vw', 'position': 'relative', 'margin-left': '60%', 'margin-top': '-5%'}),
                html.Img(src='/assets/attach_money.png',
                         style={'height': '26vw', 'position': 'relative', 'margin-left': '70%', 'margin-top': '-28%'}),
            ], style={'position': 'relative', 'width': '100%', 'height': '0'}),
            html.Div([
                html.Img(src='/assets/calendar_month.png', style={'height': '2vw', 'margin-right': '1vw'}),
                dcc.DatePickerRange(
                    id='date-picker-range-2',
                    start_date_placeholder_text="Начало",
                    end_date_placeholder_text="Конец",
                    calendar_orientation='horizontal',
                ),
                html.Button('Загрузить данные', id='load-data-button-2', n_clicks=0, className='btn btn-primary ml-3', style={
                    'background-color': '#30D9CA',
                    'border-color': '#30D9CA',
                    'margin-left': '1vw',
                    'position': 'relative',
                    'z-index': '10',
                }),
            ], style={
                'display': 'flex',
                'align-items': 'center',
                'margin-left': '3%',
                'margin-top': '1%',
                'position': 'relative',
            }),
            dbc.Row([
                dbc.Col(dbc.Card([
                    dbc.CardBody([
                        html.H4("График 1", className="card-title"),
                        dcc.Graph(id='graph-1', figure=go.Figure(), style={'height': '50vh'}),
                    ])
                ]), width=6, style={'margin-left': '3%'}),
            ], className='mb-4', style={'z-index': '-1', 'margin-top': '1%', 'position': 'relative'}),
        ], style={'height': '90vh', 'position': 'relative'}),

        # 3 слайд
        html.Div([
            html.Div([
                html.H1("КОЭФФИЦИЕНТ ВЛИЯНИЯ НОВОСТЕЙ", className='main-layout-header-text-2', style={'text-align': 'left', 'margin-top': '3%'}),
                html.Div([
                    html.Img(src='/assets/bookmarks.png', style={'height': '3vw', 'margin-right': '0.5vw'}),
                    html.H2("На графике показано, какой вес вносит каждое событие на общий курс изменения валюты в течение месяца. Чем выше коэффициент, тем больше влияние.", className='text', style={'display': 'inline', 'vertical-align': 'middle', 'text-align': 'left'}),
                ], style={'display': 'flex', 'justify-content': 'flex-start', 'align-items': 'center', 'margin-top': '1%'}),
            ], style={'margin-left': '3%', 'width': '50%'}),
            html.Div([
                html.Img(src='/assets/currency_ruble.png', style={'height': '35vw', 'position': 'relative', 'margin-left': '60%', 'margin-top': '-5%'}),
                html.Img(src='/assets/attach_money.png',
                         style={'height': '26vw', 'position': 'relative', 'margin-left': '70%', 'margin-top': '-28%'}),
            ], style={'position': 'relative', 'width': '100%', 'height': '0'}),
            html.Div([
                html.Img(src='/assets/calendar_month.png', style={'height': '2vw', 'margin-right': '1vw'}),
                dcc.DatePickerRange(
                    id='date-picker-range-3',
                    start_date_placeholder_text="Начало",
                    end_date_placeholder_text="Конец",
                    calendar_orientation='horizontal',
                ),
                html.Button('Загрузить данные', id='load-data-button-3', n_clicks=0, className='btn btn-primary ml-3', style={
                    'background-color': '#30D9CA',
                    'border-color': '#30D9CA',
                    'margin-left': '1vw',
                }),
            ], style={
                'display': 'flex',
                'align-items': 'center',
                'margin-left': '3%',
                'margin-top': '1%',
            }),
            dbc.Row([
                dbc.Col(dbc.Card([
                    dbc.CardBody([
                        html.H4("столбчатая диаграмма", className="card-title"),
                        dcc.Graph(id='bar-chart', figure=go.Figure(
                            go.Bar(x=['Category A', 'Category B', 'Category C'], y=[10, 20, 30])), style={'height': '50vh'}),
                    ])
                ]), width=6, style={'margin-left': '3%'}),
            ], className='mb-4', style={'z-index': '-1', 'margin-top': '1%'}),
        ], style={'height': '90vh', 'position': 'relative', 'z-index': '-1'}),

        # подвал
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
                'position': 'relative',
                'width': '7vw',
                'height': '4vw',
                'top': '45%',
                'left': '55%',
                'transform': 'translate(-50%, -50%)',
                'text-align': 'center',
            }), ],
            style={
                'background-color': 'rgba(30, 30, 30, 1)',
                'height': '15vh',
                'background-size': 'cover',
                'background-position': 'center center',
                'position': 'relative',
                'z-index': '-1',
            }),
    ], style={ 'z-index': '-1'})
    return layout

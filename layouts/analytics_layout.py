from dash import html, dcc
import dash_bootstrap_components as dbc
import plotly.graph_objs as go

def create_analytics_layout():
    layout = html.Div([
        html.H1("Аналитика", className="text-center mt-5"),
        html.Div([
            dcc.DatePickerRange(
                id='date-picker-range',
                start_date_placeholder_text="Start Period",
                end_date_placeholder_text="End Period",
                calendar_orientation='horizontal',
            ),
            html.Div(style={'margin-left': '20px'}),  # Adjust the pixel amount as needed
            html.Button('Загрузить данные', id='load-data-button', n_clicks=0, className='btn btn-primary ml-3'),
        ], className='d-flex align-items-center mb-3'),  # Делаем строку из элементов и выравниваем по центру
        dbc.Row([
            dbc.Col(dbc.Card([
                dbc.CardBody([
                    html.H4("График 1", className="card-title"),
                    dcc.Graph(id='graph-1', figure=go.Figure()),
                ])
            ]), width=4),
            dbc.Col(dbc.Card([
                dbc.CardBody([
                    html.H4("График 2", className="card-title"),
                    dcc.Graph(id='graph-2', figure=go.Figure()),
                ])
            ]), width=4),
            dbc.Col(dbc.Card([
                dbc.CardBody([
                    html.H4("График 3", className="card-title"),
                    dcc.Graph(id='graph-3', figure=go.Figure()),
                ])
            ]), width=4),
        ], className='mb-4'),
        dbc.Row([
            dbc.Col(dbc.Card([
                dbc.CardBody([
                    html.H4("Таблица 1", className="card-title"),
                    dcc.Loading(id="loading-1", children=[html.Div(id='table-1')])
                ])
            ]), width=12),
        ], className='mb-4'),
    ], className="container-fluid")

    return layout




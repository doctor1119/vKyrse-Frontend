from dash import html, dcc, Input, Output, State
import dash_bootstrap_components as dbc
import dash_ag_grid as dag
import plotly.graph_objs as go
import pandas as pd
import requests
from app import app


def send_requests(start_date="2024-01-01", end_date="2024-01-02"):
    url = "http://localhost:8000/get-articles-by-period"
    request_body = {
        "start_date": start_date,
        "end_date": end_date
    }

    with requests.Session() as session:
        response = session.get(url=url, json=request_body)
    return response.json()


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


@app.callback(
    [Output('graph-1', 'figure'),
     Output('graph-2', 'figure'),
     Output('graph-3', 'figure'),
     Output('table-1', 'children')],
    [Input('load-data-button', 'n_clicks')],
    [State('date-picker-range', 'start_date'),
     State('date-picker-range', 'end_date')]
)
def update_data(n_clicks, start_date, end_date):
    if n_clicks > 0 and start_date and end_date:
        df = pd.DataFrame(send_requests(start_date, end_date))

        graph_1_figure = go.Figure()
        graph_2_figure = go.Figure()
        graph_3_figure = go.Figure()

        if df.empty:
            placeholder = html.Div('Нет данных для отображения', style={'textAlign': 'center', 'marginTop': '50px'})
            return graph_1_figure, graph_2_figure, graph_3_figure, placeholder
        else:
            grid = dag.AgGrid(
                id="quickstart-grid",
                rowData=df.to_dict("records"),
                columnDefs=[{"field": i} for i in df.columns],
                defaultColDef={"resizable": True, "sortable": True, "filter": True, "minWidth": 125},
                columnSize="sizeToFit",
            )
        return graph_1_figure, graph_2_figure, graph_3_figure, grid

    placeholder = html.Div('Выберите период и нажмите "Загрузить данные"', style={'textAlign': 'center', 'marginTop': '50px'})
    return go.Figure(), go.Figure(), go.Figure(), placeholder

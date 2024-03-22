from dash import html, dcc, Dash, Input, Output, State
import dash_ag_grid as dag
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
        html.Div(id='page-content', children=[
            html.H1("Таблица с данными", className="text-center mt-5"),
            html.P("Выберите период:", style={'fontSize': '18px', 'color': 'black'}),
            dcc.DatePickerRange(
                id='date-picker-range',
                start_date_placeholder_text="Start Period",
                end_date_placeholder_text="End Period",
                calendar_orientation='horizontal',
            ),
            html.Button('Загрузить данные', id='submit-button', n_clicks=0),
            html.P("Таблица ниже", style={'fontSize': '18px', 'color': 'black'})
        ]),
        html.Div(id="quickstart-output")
    ])
    return layout


@app.callback(
    Output('quickstart-output', 'children'),
    [Input('submit-button', 'n_clicks')],
    [State('date-picker-range', 'start_date'),
     State('date-picker-range', 'end_date')]
)
def update_output(n_clicks, start_date, end_date):
    if n_clicks > 0:
        df = pd.DataFrame(send_requests(start_date, end_date))
        grid = dag.AgGrid(
            id="quickstart-grid",
            rowData=df.to_dict("records"),
            columnDefs=[{"field": i} for i in df.columns],
            defaultColDef={"resizable": True, "sortable": True, "filter": True, "minWidth": 125},
            columnSize="sizeToFit",
        )
        return grid
    return html.Div()

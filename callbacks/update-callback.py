from dash import Input, Output, State, html
import dash_ag_grid as dag
import plotly.graph_objs as go
import pandas as pd
from app import app
from services.send_requests import send_requests


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
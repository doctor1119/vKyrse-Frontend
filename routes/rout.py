from dash import dcc, html
from dash.dependencies import Input, Output

from app import app
from layouts.main_layout import create_main_layout
from layouts.analytics_layout import create_analytics_layout
from components.navbar import create_navbar


def serve_layout():
    return html.Div(style={'display': 'flex', 'flexDirection': 'row'}, children=[
        create_navbar(),
        html.Div(id='page-content', style={'margin-left': '100px', 'padding': '20px', 'flex': '1'}),
        dcc.Location(id='url', refresh=False),
    ])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/currency-analysis':
        return create_analytics_layout()

    elif pathname == '/':
        return create_main_layout()


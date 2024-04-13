from dash import dcc, html
from dash.dependencies import Input, Output

from app import app
from layouts.main_layout import create_main_layout
from layouts.analytics_layout import create_analytics_layout
from layouts.contacts_layout import create_contacts_layout
from components.navbar import create_navbar


def serve_layout():
    return html.Div(style={'display': 'flex', 'flexDirection': 'row'}, children=[
        create_navbar(),
        html.Div(id='page-content', style={
            'flex': '1',
            'padding-top': '120px',  # Отступ, чтобы содержимое начиналось ниже navbar
        }),
        dcc.Location(id='url', refresh=False),
    ])



@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/currency-analysis':
        return create_analytics_layout()
    if pathname == '/contact':
        return create_contacts_layout()

    elif pathname == '/':
        return create_main_layout()


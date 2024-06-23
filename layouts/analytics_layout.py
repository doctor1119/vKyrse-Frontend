from dash import Dash, html, dcc, Input, Output, State
import dash_bootstrap_components as dbc
import plotly.graph_objs as go
from datetime import datetime
from services.send_requests import send_requests

# Sample topics - you can fetch these from your backend
TOPICS = ["Economy", "Politics", "Technology", "Health", "Entertainment"]

app = Dash(__name__)


def create_analytics_layout():
    layout = html.Div([
        # Common date picker and load data button
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
                'z-index': '0'
            }),
        ], style={
            'display': 'flex',
            'align-items': 'center',
            'margin-left': '3%',
            'margin-top': '1%',
            'position': 'relative',
        }),

        # 1 slide
        html.Div([
            html.Div([
                html.Div([
                    html.H1("ТЕКУЩИЙ КУРС ВАЛЮТЫ", className='main-layout-header-text-2',
                            style={'text-align': 'left', 'margin-top': '3%'}),
                    html.Div([
                        html.Img(src='/assets/bookmarks.png', style={'height': '3vw', 'margin-right': '0.5vw'}),
                        html.H2(
                            "На этом графике можно посмотреть, как меняется курс рубля по отношению к доллару за конкретный промежуток времени.",
                            className='text',
                            style={'display': 'inline', 'vertical-align': 'middle', 'text-align': 'left'}),
                    ], style={'display': 'flex', 'justify-content': 'flex-start', 'align-items': 'center',
                              'margin-top': '1%'}),
                ], style={'margin-left': '3%', 'width': '50%'}),
                html.Div([
                    html.Img(src='/assets/currency_ruble.png',
                             style={'height': '35vw', 'position': 'relative', 'margin-left': '60%',
                                    'margin-top': '-5%'}),
                    html.Img(src='/assets/attach_money.png',
                             style={'height': '26vw', 'position': 'relative', 'margin-left': '70%',
                                    'margin-top': '-28%'}),
                ], style={'position': 'relative', 'width': '100%', 'height': '0'}),
            ], style={'position': 'relative', 'z-index': '-1'}),
            dbc.Row([
                dbc.Col(dbc.Card([
                    dbc.CardBody([
                        html.H4("График 1", className="card-title"),
                        dcc.Graph(id='graph-1', figure=go.Figure(), style={'height': '50vh'}),
                    ])
                ]), width=6, style={'margin-left': '3%'}),
            ], className='mb-4', style={'margin-top': '1%', 'position': 'relative', 'z-index': '-1'}),
        ], style={'height': '90vh', 'position': 'relative'}),

        # 2 slide
        html.Div([
            html.Div([
                html.Div([
                    html.H1("КУРС ВАЛЮТЫ ПО СОБЫТИЯМ", className='main-layout-header-text-2',
                            style={'text-align': 'left', 'margin-top': '3%'}),
                    html.Div([
                        html.Img(src='/assets/bookmarks.png', style={'height': '3vw', 'margin-right': '0.5vw'}),
                        html.H2(
                            "Вы можете настроить графики по событиям и увидеть, какое из них оказало наибольшее влияние курс рубля за месяц.",
                            className='text',
                            style={'display': 'inline', 'vertical-align': 'middle', 'text-align': 'left'}),
                    ], style={'display': 'flex', 'justify-content': 'flex-start', 'align-items': 'center',
                              'margin-top': '1%'}),
                ], style={'margin-left': '3%', 'width': '50%'}),
                html.Div([
                    html.Img(src='/assets/currency_ruble.png',
                             style={'height': '35vw', 'position': 'relative', 'margin-left': '60%',
                                    'margin-top': '-5%'}),
                    html.Img(src='/assets/attach_money.png',
                             style={'height': '26vw', 'position': 'relative', 'margin-left': '70%',
                                    'margin-top': '-28%'}),
                ], style={'position': 'relative', 'width': '100%', 'height': '0'}),
            ], style={'position': 'relative', 'z-index': '-1'}),
            html.Div([
                dcc.Dropdown(
                    id='topic-dropdown',
                    options=[{'label': topic, 'value': topic} for topic in TOPICS],
                    placeholder="Выберите тему",
                    style={'width': '20vw'}
                ),
            ], style={'display': 'flex', 'align-items': 'center', 'margin-left': '5%', 'margin-top': '1%',
                      'position': 'relative'}),
            dbc.Row([
                dbc.Col(dbc.Card([
                    dbc.CardBody([
                        html.H4("График 2", className="card-title"),
                        dcc.Graph(id='graph-2', figure=go.Figure(), style={'height': '50vh'}),
                    ])
                ]), width=6, style={'margin-left': '3%'}),
            ], className='mb-4', style={'margin-top': '1%', 'position': 'relative', 'z-index': '-1'}),
            html.Div(id='search-results', style={'margin-top': '20px', 'margin-left': '3%'}),
        ], style={'height': '90vh', 'position': 'relative'}),

        # 3 slide
        html.Div([
            html.Div([
                html.Div([
                    html.H1("КОЭФФИЦИЕНТ ВЛИЯНИЯ НОВОСТЕЙ", className='main-layout-header-text-2',
                            style={'text-align': 'left', 'margin-top': '3%'}),
                    html.Div([
                        html.Img(src='/assets/bookmarks.png', style={'height': '3vw', 'margin-right': '0.5vw'}),
                        html.H2(
                            "На графике показано, какой вес вносит каждое событие на общий курс изменения валюты в течение месяца. Чем выше коэффициент, тем больше влияние.",
                            className='text',
                            style={'display': 'inline', 'vertical-align': 'middle', 'text-align': 'left'}),
                    ], style={'display': 'flex', 'justify-content': 'flex-start', 'align-items': 'center',
                              'margin-top': '1%'}),
                ], style={'margin-left': '3%', 'width': '50%'}),
                html.Div([
                    html.Img(src='/assets/currency_ruble.png',
                             style={'height': '35vw', 'position': 'relative', 'margin-left': '60%',
                                    'margin-top': '-5%'}),
                    html.Img(src='/assets/attach_money.png',
                             style={'height': '26vw', 'position': 'relative', 'margin-left': '70%',
                                    'margin-top': '-28%'}),
                ], style={'position': 'relative', 'width': '100%', 'height': '0'}),
            ], style={'position': 'relative', 'z-index': '-1'}),
            html.Div([
                dcc.Dropdown(
                    id='topic-dropdown-3',
                    options=[{'label': topic, 'value': topic} for topic in TOPICS],
                    placeholder="Выберите тему",
                    style={'width': '300px'}
                ),
            ], style={'display': 'flex', 'align-items': 'center', 'margin-left': '5%', 'margin-top': '1%',
                      'position': 'relative'}),
            dbc.Row([
                dbc.Col(dbc.Card([
                    dbc.CardBody([
                        html.H4("Cтолбчатая диаграмма", className="card-title"),
                        dcc.Graph(id='bar-chart', figure=go.Figure(
                            go.Bar(x=['Category A', 'Category B', 'Category C'], y=[10, 20, 30])),
                                  style={'height': '50vh'}),
                    ])
                ]), width=6, style={'margin-left': '3%'}),
            ], className='mb-4', style={'margin-top': '1%', 'position': 'relative', 'z-index': '-1'}),
        ], style={'height': '90vh', 'position': 'relative'}),

        # Footer
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
    ], style={'z-index': '-1'})
    return layout


app.layout = create_analytics_layout()


# Define callback to update graphs based on topic and date range
@app.callback(
    [Output('graph-1', 'figure'),
     Output('graph-2', 'figure'),
     Output('bar-chart', 'figure')],
    Input('load-data-button', 'n_clicks'),
    State('date-picker-range', 'start_date'),
    State('date-picker-range', 'end_date'),
    State('topic-dropdown', 'value'),
    State('topic-dropdown-3', 'value')
)
def update_graphs(n_clicks, start_date, end_date, topic1, topic2):
    if n_clicks == 0 or start_date is None or end_date is None:
        return go.Figure(), go.Figure(), go.Figure(
            go.Bar(x=['Category A', 'Category B', 'Category C'], y=[10, 20, 30]))

    # Convert start_date and end_date to datetime objects for easier manipulation
    start_date = datetime.strptime(start_date, "%Y-%m-%d")
    end_date = datetime.strptime(end_date, "%Y-%m-%d")

    # Call the send_requests function
    send_requests(start_date, end_date)

    # Placeholder: Replace with actual logic to fetch and display data for graph 1
    fig1 = go.Figure()
    fig1.add_trace(go.Scatter(x=[1, 2, 3], y=[2, 1, 3], mode='lines', name='Sample Data'))

    # Placeholder: Replace with actual logic to fetch and display data for graph 2
    fig2 = go.Figure()
    fig2.add_trace(go.Scatter(x=[1, 2, 3], y=[3, 2, 1], mode='lines', name='Sample Data'))

    # Placeholder: Replace with actual logic to fetch and display data for bar chart
    bar_chart = go.Figure(go.Bar(x=['Category A', 'Category B', 'Category C'], y=[10, 20, 30]))

    return fig1, fig2, bar_chart

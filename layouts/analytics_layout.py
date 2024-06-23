from dash import Dash, html, dcc, Input, Output, State
import dash_bootstrap_components as dbc
import plotly.graph_objs as go
from datetime import datetime
from services.send_requests import send_requests
from app import app

# Sample topics - you can fetch these from your backend
TOPICS = ["Economy", "Politics", "Technology", "Health", "Entertainment"]

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
                        dcc.Loading(
                            id="loading-graph-1",
                            type="circle",
                            children=dcc.Graph(id='graph-1', figure=go.Figure(), style={'height': '50vh'})
                        ),
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
            dbc.Row([
                dbc.Col(dbc.Card([
                    dbc.CardBody([
                        html.H4("График 2", className="card-title"),
                        dcc.Loading(
                            id="loading-graph-2",
                            type="circle",
                            children=dcc.Graph(id='graph-2', figure=go.Figure(), style={'height': '50vh'})
                        ),
                    ])
                ]), width=6, style={'margin-left': '3%'}),
            ], className='mb-4', style={'margin-top': '1%', 'position': 'relative', 'z-index': '1'}),
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
            dbc.Row([
                dbc.Col(dbc.Card([
                    dbc.CardBody([
                        html.H4("Cтолбчатая диаграмма", className="card-title"),
                        dcc.Loading(
                            id="loading-bar-chart",
                            type="circle",
                            children=dcc.Graph(id='bar-chart', figure=go.Figure(go.Bar(x=['Category A', 'Category B', 'Category C'], y=[10, 20, 30])), style={'height': '50vh'})
                        ),
                    ])
                ]), width=6, style={'margin-left': '3%'}),
            ], className='mb-4', style={'margin-top': '1%', 'position': 'relative', 'z-index': '1'}),
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
    [Input('load-data-button', 'n_clicks')],
    [State('date-picker-range', 'start_date'),
     State('date-picker-range', 'end_date')]
)
def update_graphs(n_clicks, start_date, end_date):
    if n_clicks == 0 or start_date is None or end_date is None:
        fig1 = go.Figure()
        fig2 = go.Figure()
        bar_chart = go.Figure()
        return fig1, fig2, bar_chart

    # Convert start_date and end_date to datetime objects for easier manipulation
    start_date_str = datetime.strptime(start_date, '%Y-%m-%d').strftime('%Y-%m-%d')
    end_date_str = datetime.strptime(end_date, '%Y-%m-%d').strftime('%Y-%m-%d')

    # Call the send_requests function and parse the response
    response = send_requests(start_date_str, end_date_str)
    data = response.get('data', [])

    # Extract dates and currency values for graph-1
    dates = [entry['published_dt'] for entry in data]
    currency_values = [entry['currency_curs'] for entry in data]

    # Create the figure for graph-1
    fig1 = go.Figure()
    fig1.add_trace(go.Scatter(x=dates, y=currency_values, mode='lines', name='Currency Rate'))

    # Process data for graph-2
    event_labels = []
    cluster_ids = []

    for entry in data:
        relevant_events = entry.get('events', [])
        if relevant_events:
            max_event = max(relevant_events, key=lambda x: abs(x['impact_factor']))
            event_labels.append(max_event['cluster_name'])
            # Find the cluster_id with the maximum absolute impact_factor
            cluster_ids.append(max_event['cluster_id'])
        else:
            event_labels.append('')
            cluster_ids.append('')

    hover_text = [
        f"Дата: {datetime.strptime(entry['published_dt'][:10], '%Y-%m-%d').strftime('%d-%m-%Y')}<br>Курс: {entry['currency_curs']:.2f}<br>Кластер ID: {cluster_id}"
        for entry, cluster_id in zip(data, cluster_ids)]

    # Create the figure for graph-2
    fig2 = go.Figure()
    fig2.add_trace(go.Scatter(x=[entry['published_dt'] for entry in data],
                              y=[entry['currency_curs'] for entry in data],
                              mode='lines+markers',
                              text=event_labels,
                              hoverinfo='text+x+y',
                              hovertext=hover_text,
                              name='Currency Rate with Events'))

    # Update date format for x-axis in fig1 and fig2
    fig1.update_layout(
        xaxis=dict(
            tickformat='%d-%m-%Y'
        )
    )

    fig2.update_layout(
        xaxis=dict(
            tickformat='%d-%m-%Y'
        )
    )

    # Process data for bar-chart
    bar_dates = []
    impact_factors = []
    cluster_ids_for_hover = []
    for entry in data:
        relevant_events = entry.get('events', [])
        if relevant_events:
            max_event = max(relevant_events, key=lambda x: abs(x['impact_factor']))
            bar_dates.append(entry['published_dt'])
            impact_factors.append(max_event['impact_factor'])
            cluster_ids_for_hover.append(max_event['cluster_id'])

    # Create the bar chart with hover text
    bar_chart = go.Figure(go.Bar(x=bar_dates, y=impact_factors,
                                 hovertext=[f"Cluster ID: {cluster_id}" for cluster_id in cluster_ids_for_hover],
                                 hoverinfo='x+y+text',
                                 name='Impact Factor'))

    # Update date format for x-axis in bar_chart
    bar_chart.update_layout(
        xaxis=dict(
            tickformat='%d-%m-%Y'
        ),
        yaxis_title='Impact Factor'
    )

    return fig1, fig2, bar_chart


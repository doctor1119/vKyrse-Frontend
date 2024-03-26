# from dash import Dash, html, dcc, Output, Input
# import pandas as pd
# import requests
# import dash_ag_grid as dag
#
#
# def send_requests(start_date="2024-01-01", end_date="2024-01-02"):
#     url = "http://localhost:8000/get-articles-by-period"
#     request_body = {
#         "start_date": start_date,
#         "end_date": end_date
#     }
#
#     with requests.Session() as session:
#         response = session.get(url=url, json=request_body)
#     return response.json()
#
#
# df = pd.DataFrame(send_requests())
#
# # Initialize the app
# app = Dash(__name__)
#
# grid = dag.AgGrid(
#     id="quickstart-grid",
#     rowData=df.to_dict("records"),
#     columnDefs=[{"field": i} for i in df.columns],
#     defaultColDef={"resizable": True, "sortable": True, "filter": True, "minWidth": 125},
#     columnSize="sizeToFit",
# )
#
# # app.layout = html.Div([
# #     #     dcc.DatePickerSingle(
# #     #         id='start-date',
# #     #         date=date()
# #     #       #display_format='YYYY-MM-DD'
# #     #     ),
# #     #     html.Button('Submit', id='submit-button'),
# #     #     html.Div(id='output-container-button',
# #     #              children='Enter a date and press submit')
# #     # ]),
# #     dcc.Location(id='url', refresh=False),
# #     html.Nav([
# #         html.Ul([
# #             html.Li(html.A('Главная', href='/')),
# #             html.Li(html.A('Анализ валют', href='/currency-analysis')),
# #             html.Li(html.A('О проекте', href='/about')),
# #             html.Li(html.A('Контакты', href='/contact'))
# #         ], style={'list-style-type': 'none', 'margin': 0, 'padding': 0, 'overflow': 'hidden',
# #                   'background-color': '#333'}),
# #     ], style={'margin-bottom': '20px'}),
# #     html.Div(id='page-content'),
# #
# #     html.H4("Simple interactive grid"),
# #     grid,
# #     html.Div(id="quickstart-output")
# # ])
#
# app.layout = html.Div(style={'display': 'flex', 'flexDirection': 'row'}, children=[
#     # Навигационное меню слева
#     html.Div([
#         html.Ul([
#             html.Li(html.A('Главная', href='/')),
#             html.Li(html.A('Анализ валют', href='/currency-analysis')),
#             html.Li(html.A('О проекте', href='/about')),
#             html.Li(html.A('Контакты', href='/contact'))
#         ], style={
#             'list-style-type': 'none',
#             'padding': 0,
#             'height': '100vh',  # Высота на всю высоту окна просмотра
#             'width': '200px',  # Ширина блока навигации
#             'background-color': '#f0f0f0',  # Цвет фона
#             'position': 'fixed'  # Фиксированное положение
#         })
#     ], style={'flex': '0 0 200px'}),  # Задаем фиксированную ширину для блока навигации
#
#     # Контент справа
#     html.Div(id='page-content', style={'margin-left': '200px', 'padding': '20px', 'flex': '1'}),
#     # Отступ слева под блок навигации
# ])
#
#
# # app.layout = html.Div([
# #     dcc.DatePickerSingle(
# #         id='start-date',
# #         date=date(2017, 9, 19)
# #     ),
# #     html.Button('Submit', id='submit-button'),
# #     html.Div(id='output-container-button',
# #              children='Enter a date and press submit')
# # ])
#
# @app.callback(Output('page-content', 'children'),
#               [Input('url', 'pathname')])
# def display_page(pathname):
#     if pathname == '/currency-analysis':
#         return html.H1('Анализ валют')
#     elif pathname == '/about':
#         return html.H1('О проекте')
#     elif pathname == '/contact':
#         return html.H1('Контакты')
#     else:
#         return html.H1('Главная страница')
#
#
# app.layout.children.append(dcc.Location(id='url', refresh=False))
#
# # Run the app
# if __name__ == '__main__':
#     app.run(debug=False)

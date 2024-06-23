from dash import Dash, html, dcc, Input, Output
import dash_bootstrap_components as dbc
from app import app



def create_main_layout():
    layout = html.Div([
        # 1 слайд
        html.Div([
            # Фоновый слой
            html.Div(style={
                'background-image': 'url(/assets/main-dark.png)',
                'height': '90vh',
                'background-size': 'cover',
                'background-position': 'center center',
                'position': 'absolute',
                'width': '100%',
                'z-index': '-1',
            }),
            # Контентный слой
            html.Div([
                html.H1('Будь в Курсе', className='main-layout-header-text', style={
                    'color': 'white',
                    'margin-bottom': '1vw',
                    'z-index': '-1',
                }),
                html.P([
                    'место, где собраны все новости,',
                    html.Br(),  # Перенос строки
                    'изменившие курс рубля не только сегодня'
                ], className='main-layout-text',
                    style={'font-size': '2vw', 'color': 'white', 'margin-bottom': '2vw', 'z-index': '-1'}),
                html.A(html.Button([
                    html.Span('Следить за курсом', className='follow-text'),
                ], id='follow-currency-button', className='follow-currency-button',
                    style={'height': '3vw', 'width': '15vw', 'display': 'flex', 'align-items': 'center',
                           'justify-content': 'center', 'z-index': '1'}),
                    href='/currency-analysis', style={'text-decoration': 'none'}),
            ], style={
                'display': 'flex',
                'flex-direction': 'column',
                'align-items': 'center',
                'justify-content': 'center',
                'height': '100%',
                'text-align': 'center',
                'position': 'relative',
            }),
        ], style={
            'height': '90vh',
            'position': 'relative',
        }),
#2 слайд
        html.Div([
                   html.H1('О нас', className='main-layout-header-text-2', style={
                       'position': 'absolute',
                       'top': '25%',
                       'left': '8%',
                   }),
                    html.P([
                        'Обычные студенты, воплощающие свои идеи',
                        html.Br(),
                        'в жизнь!'],
                        className='main-layout-text', style={
                       'position': 'absolute',
                       'top': '35%',
                       'left': '8%'}),
            html.P([
                'Мы создали место, где каждый может',
                html.Br(),
                'отслеживать курс рубля и узнавать, как самые',
                html.Br(),
                'актуальные новости влияют на валюту'],
                className='main-layout-text', style={
                    'font-weight': 'bold',
                    'position': 'absolute',
                    'top': '50%',
                    'left': '6.5%',
                    'padding-left': '20px',  # Добавляем отступ слева для декоративной полоски
                    'border-left': '4px solid #30D9CA',
                }),
             html.A(html.Button([
                 html.Span('Зачем смотреть курс рубля', className='follow-text'),
                 ], id='why-follow-currency-button', className='follow-currency-button',
                 style={'height': '3.3vw', 'width': '21vw', 'display': 'flex', 'align-items': 'center',
                        'justify-content': 'center',
                        'position': 'absolute',
                        'top': '62%',
                        'left': '13%'
                        }),
                 href='/currency-analysis', style={'text-decoration': 'none'}),
    html.Div([
        html.Div([
            html.Img(src='/assets/image1.jpg', style={'width': '16vw', 'height': '16vw', 'margin-right': '20px'}),
            html.Img(src='/assets/image2.png', style={'width': '16vw', 'height': '16vw', 'margin-top': '40px'}),
        ], style={'display': 'flex'}),
        html.Div([
            html.Img(src='/assets/image3.png', style={'width': '16vw', 'height': '16vw', 'margin-right': '20px'}),
            html.Img(src='/assets/image4.jpg', style={'width': '16vw', 'height': '16vw', 'margin-top': '40px'}),
        ], style={'display': 'flex'}),
    ], style={'position': 'absolute', 'top': '7%', 'right': '7%'}),


        ], style={
            'background-color': 'rgba(217, 217, 217, 0.26)',
            'height': '90vh',
            'background-size': 'cover',
            'background-position': 'center center',
            'position': 'relative',
            'z-index': '-1',
        }),

#3 слайд
        html.Div([ html.H1('Следить за курсом, чтобы', className='main-layout-header-text-2',
                           style={'position': 'absolute',
                                    'top': '15%',
                                    'left': '10%'}),
        html.Div([
            html.Div([
                html.Img(src='/assets/img1.png',
                         style={'width': '4vw',
                                'height': '4vw',
                                'margin-left': '95px'
                                }),
                html.P(['знать все актуальные события',
                       html.Br(),
                'и новости мира'],
                       className='text',
                       style={'text-align': 'center', 'margin-top': '20px'}),
            ], style={'display': 'inline-block',
                      'position': 'absolute',
                      'vertical-align': 'top',
                       'top': '30%',
                       'left': '20%'}),
            html.Div([
                html.Img(src='/assets/img2.png', style={'width': '3.5vw', 'height': '4vw','margin-left': '55px'}),
                html.P(['регулировать свои',
                       html.Br(),
                       'сбережения'],
                       className='text',
                       style={'text-align': 'center', 'margin-top': '20px'}),
            ], style={'display': 'inline-block',
                      'position': 'absolute',
                       'top': '30%',
                       'left': '48%'}),
            html.Div([
                html.Img(src='/assets/img3.png', style={'width': '4vw', 'height': '4vw','margin-left': '65px'}),
                html.P(['создавать свою стратегию',
                       html.Br(),
                       'инвестирования'],
                       className='text',
                       style={'text-align': 'center', 'margin-top': '20px'}),
            ], style={'display': 'inline-block',
                      'position': 'absolute',
                       'top': '30%',
                       'left': '70%'}),
        ]),
        html.H1('А также вы можете', className='main-layout-header-text-2',
                           style={'position': 'absolute',
                                    'top': '55%',
                                    'left': '10%'}),
        html.Div([
            html.Div([
                html.Img(src='/assets/img4.png', style={'width': '4vw', 'height': '4vw','margin-left': '70px'}),
                html.P(['прогнозировать изменения',
                       html.Br(),
                       'курса рубля'],
                       className='text',
                       style={'text-align': 'center', 'margin-top': '20px'}),
            ], style={'display': 'inline-block',
                      'position': 'absolute',
                       'top': '70%',
                       'left': '20%'}),
            html.Div([
                html.Img(src='/assets/img5.png', style={'width': '4vw', 'height': '4vw','margin-left': '75px'}),
                html.P(['оценивать  экономическое',
                       html.Br(),
                       'положение России в текущий',
                       html.Br(),
                       'момент и перспективы'],
                       className='text',
                       style={'text-align': 'center', 'margin-top': '20px'}),
            ], style={'display': 'inline-block',
                      'position': 'absolute',
                       'top': '70%',
                       'left': '45%'}),
            html.Div([
                html.Img(src='/assets/img6.png', style={'width': '7.5vw', 'height': '4vw','margin-left': '30px'}),
                html.P(['анализировать текущую',
                       html.Br(),
                       ' обстановку на рынке'],
                       className='text',
                       style={'text-align': 'center', 'margin-top': '20px'}),
            ], style={'display': 'inline-block',
                      'position': 'absolute',
                       'top': '70%',
                       'left': '70%'}),
        ]),
                  ], style={
            'background-image': 'url(assets/woman-light.png)',
            'height': '90vh',
            'background-size': 'cover',
            'background-position': 'center center',
            'position': 'relative',
            'z-index': '-1',
        }),

#4 слайд
        html.Div([
            html.Div([
                html.Img(src='/assets/vector-question-icon.png', style={'height': '3vw'}),
                html.H1('Часто задаваемые вопросы', className='main-layout-header-text-2', style={'margin': '1vw'}),
            ], style={'display': 'flex', 'align-items': 'center', 'margin-left': '5vw', 'padding-top': '2.5vw'},
            ),
            html.Div([
                html.Img(src='/assets/arrow_right-icon.png', id='button1', style={'cursor': 'pointer', 'height': '1.5vw'}),
                html.P(['Как вы анализируете изменения курса?'], className='main-layout-header-text-3',
                       style={'margin': '1vw'})
            ], style={'display': 'flex', 'align-items': 'center', 'margin-left': '10vw', 'padding-top': '1vw'}),
            html.Div(id='output-container-button1',
                     style={'margin-left': '15vw'}),
            html.Div([
                html.Img(src='/assets/arrow_right-icon.png', id='button2',
                         style={'cursor': 'pointer', 'height': '1.5vw'}),
                html.P(['Почему нам можно доверять?'], className='main-layout-header-text-3',
                       style={'margin': '1vw'})
            ], style={'display': 'flex', 'align-items': 'center', 'margin-left': '10vw', 'padding-top': '0vw'}),
            html.Div(id='output-container-button2',
                     style={'margin-left': '15vw'}),
            html.Div([
                html.Img(src='/assets/arrow_right-icon.png', id='button3',
                         style={'cursor': 'pointer', 'height': '1.5vw'}),
                html.P(['Для кого подойдет?'], className='main-layout-header-text-3',
                       style={'margin': '1vw'})
            ], style={'display': 'flex', 'align-items': 'center', 'margin-left': '10vw', 'padding-top': '0vw'}),
            html.Div(id='output-container-button3',
                     style={'margin-left': '15vw'})
        ], style={
            'background-color': 'rgba(217, 217, 217, 0.26)',
            'height': '90vh',
            'background-size': 'cover',
            'background-position': 'center center',
            'position': 'relative',
            'z-index': '-1',
        }),


#5 слайд
        html.Div([
            html.Div([
                html.H1('Будь в Курсе', className='main-layout-header-text', style={
                    'position': 'relative',
                    'top': '50%',
                    'left': '50%',
                    'transform': 'translate(-50%, 0%)',
                    'text-align': 'center',
                    'color': 'white',
                }),
                html.Div([
                    html.P(['вместе с нами'],
                           className='main-layout-text', style={'font-size': '2vw', 'text-align':'center'}),
                    html.A(html.Button([
                        html.Span('Быть в курсе', className='follow-text'),
                    ], id='follow-currency-button', className='follow-currency-button',
                        style={'height': '3vw', 'width': '15vw', 'display': 'flex', 'align-items': 'center',
                               'justify-content': 'center',
                               'margin-left': 'auto', 'margin-right': 'auto'}),
                        href='/currency-analysis', style={'text-decoration': 'none'}),
                ]),
            ], style={
                'position': 'absolute',
                'top': '50%',
                'left': '50%',
                'transform': 'translate(-50%, -50%)',
                'text-align': 'center',
                'color': 'white',
            }),

                  ], style={
            'background-image': 'url(assets/notebook.png)',
            'height': '90vh',
            'background-size': 'cover',
            'background-position': 'center center',
            'position': 'relative',
            'z-index': '-1',
        }),

# 6 слайд
        html.Div([
            html.Div([
                html.H1("НАШИ КОНТАКТЫ", className="text-bold", style={
                    'position': 'absolute',
                    'top': '22%',
                    'left': '50%',
                    'transform': 'translate(-50%, -50%)',
                    'text-align': 'center',
                    'color': 'black',
                }),
                html.H1(['+1 234 567 89 00',
                         ],className="main-layout-header-text-2", style={
                    'position': 'absolute',
                    'top': '35%',
                    'left': '50%',
                    'transform': 'translate(-50%, -50%)',
                    'text-align': 'center',
                    'color': 'black',
                }),
                html.H1(['hello@company.com',
                         ], className="main-layout-header-text-2", style={
                    'position': 'absolute',
                    'top': '47%',
                    'left': '50%',
                    'transform': 'translate(-50%, -50%)',
                    'text-align': 'center',
                    'color': 'black',
                }),
            ]),
            html.Div([
                html.H1("Мы в социальных сетях", className="text-bold", style={
                    'position': 'absolute',
                    'top': '67%',
                    'left': '50%',
                    'transform': 'translate(-50%, -50%)',
                    'text-align': 'center',
                    'color': 'black',
                }),
                html.A(
                    html.Img(src='/assets/link-tg.png', className="tg-link-big"),
                    href='https://t.me/parfenowakate',
                    style={
                        'position': 'absolute',
                        'top': '80%',
                        'left': '47%',
                        'transform': 'translate(-50%, -50%)',

                    }
                ),
                html.A(
                    html.Img(src='/assets/vector-vk-icon.png', className="vk-link"),
                    href='https://vk.com/maksim.kamenev',
                    style={
                        'position': 'absolute',
                        'top': '80%',
                        'left': '53%',
                        'transform': 'translate(-50%, -50%)',

                    }
                )
            ]),


                ], style={
                     'background-color': 'rgba(217, 217, 217, 0.26)',
                     'height': '75vh',
                     'background-size': 'cover',
                     'background-position': 'center center',
                     'position': 'relative',
                     'z-index': '-1',
                 }),



# 7 слайд
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
        }),],
                 style={
                     'background-color': 'rgba(30, 30, 30, 1)',
                     'height': '15vh',
                     'background-size': 'cover',
                     'background-position': 'center center',
                     'position': 'relative',
                     'z-index': '-1',
                 }),

], style={'height': '100vh', 'z-index': '-1'}),


    return layout

@app.callback(
    Output('output-container-button1', 'children'),
    [Input('button1', 'n_clicks')]
)
def update_output(n_clicks):
    if n_clicks is None:
        return ' '
    else:
        return html.Div([
            'В разделе Аналитика на графиках и таблицах собраны последние события, изменившие курс рубля.',
            html.Br(),
            'На основании этих данных можно судить о динамике изменения национальной валюты.'
        ], className='text-bubble')

@app.callback(
    Output('output-container-button2', 'children'),
    [Input('button2', 'n_clicks')]
)
def update_output(n_clicks):
    if n_clicks is None:
        return ' '
    else:
        return html.Div([
            'Мы используем различные источники информации и современные методы обработки данных, чтобы как можно реалистичнее взглянуть на экономическую обстановку и оценить новостной фон. '
            'С нами вы можете быть уверены, что прогноз на курс рубля окажется реалистичным!',
        ], className='text-bubble')

@app.callback(
    Output('output-container-button3', 'children'),
    [Input('button3', 'n_clicks')]
)
def update_output(n_clicks):
    if n_clicks is None:
        return ' '
    else:
        return html.Div([
            'Для всех, кто желает не терять время на самостоятельное изучение рынка, а сразу хочет посмотреть на экономическую обстановку, перспективы и прогнозы.',
        ], className='text-bubble')
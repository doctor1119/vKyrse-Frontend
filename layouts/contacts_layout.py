from dash import html, dcc

def create_contacts_layout():
    layout = html.Div([
        # 1 слайд
        html.Div([
            # Фоновый слой
            html.Div(style={
                'background-color': 'rgba(245, 245, 245, 1)',
                'height': '90vh',
                'background-size': 'cover',
                'background-position': 'center center',
                'position': 'absolute',
                'width': '100%',
                'z-index': '-1',
            }),
            # Контентный слой
            html.Div([
                html.Div([
                    html.H1([
                        'Наша команда стремится создать для вас лучший',
                        html.Br(),
                        'сервис по анализу курса рубля'
                    ], className='main-layout-header-text-2', style={
                        'text-align': 'left',
                        'color': 'black',
                        'margin-top': '7%',
                        'margin-left': '7%',
                        'z-index': '-1',
                    }),
                    html.P('Будем рады услышать ваши честные отзывы!',
                           className='main-layout-text', style={
                                'text-align': 'left',
                                'font-size': '2vw',
                                'color': 'black',
                                'margin-top': '2vw',
                                'margin-left': '7%',
                            'z-index': '-1',
                           }),
                    html.A(html.Button([
                        html.Span('Оставить отзыв', className='follow-text'),
                    ], id='follow-currency-button', className='follow-currency-button',
                        style={
                            'height': '3vw',
                            'width': '15vw',
                            'display': 'flex',
                            'align-items': 'center',
                            'justify-content': 'center',
                            'margin-left': '45%',
                            'margin-top': '2vw',  # отступ сверху от текста
                            'z-index': '-1',
                        }),
                        href='https://forms.gle/46Y8vvtya9eCse6F6', style={'text-decoration': 'none'}),
                ], style={
                    'display': 'flex',
                    'flex-direction': 'column',
                    'align-items': 'flex-start',  # выравнивание по левому краю
                }),
                html.Img(src='/assets/Vectorcontacts1.png', style={
                    'height': '60%',
                    'margin-top': '10%',
                    'margin-left': '60%',
                    'position': 'absolute',
                    'z-index': '-1',
                }),
            ], style={
                'display': 'flex',
                'flex-direction': 'column',
                'height': '100%',
                'text-align': 'center',
                'position': 'relative',
            }),
        ], style={
            'height': '90vh',
            'position': 'relative',
        }),

        # 2 слайд
        html.Div([
            # Фоновый слой
            html.Div(style={
                'background-color': 'rgba(89, 95, 95, 1)',
                'height': '90vh',
                'position': 'absolute',
                'width': '100%',
                'z-index': '-1',
            }),
            # Контентный слой
            html.Div([
                html.Div([
                    html.H1('УЗНАВАЙТЕ', className='big-header', style={
                        'text-align': 'left',
                    }),
                    html.H1('НОВОСТИ', className='big-header', style={
                        'text-align': 'left',
                        'margin-top': '5vh',  # отступ сверху
                    }),
                    html.H1('ПЕРВЫМИ', className='big-header-black', style={
                        'text-align': 'left',
                        'margin-top': '5vh',  # отступ сверху
                    }),
                ], style={
                    'margin-top': '10vh',
                    'margin-left': '5%',# отступ сверху для контейнера с заголовками
                }),
                html.Div([
                    html.A(
                        html.Img(src='/assets/link-tg.png', className="tg-link-big"),
                        href='https://t.me/parfenowakate',
                        style={
                            'position': 'absolute',
                            'top': '85%',
                            'left': '20%',
                            'transform': 'translate(-50%, -50%)',
                        }
                    ),
                    html.A(
                        html.Img(src='/assets/vector-vk-icon.png', className="vk-link"),
                        href='https://vk.com/maksim.kamenev',
                        style={
                            'position': 'absolute',
                            'top': '85%',
                            'left': '12%',
                            'transform': 'translate(-50%, -50%)',
                        }
                    ),
                    html.A(
                        html.Img(src='/assets/hand-holding-megaphone-for-protest.png'),
                        style={
                            'position': 'absolute',
                            'top': '5%',
                            'right': '0%',
                        }
                    )
                ]),
            ], style={
                'display': 'flex',
                'flex-direction': 'column',
                'align-items': 'flex-start',
                'justify-content': 'flex-start',
                'height': '100%',
                'padding-left': '2vw',
                'position': 'relative',
                'z-index': '-1',
            }),
        ], style={
            'height': '90vh',
            'position': 'relative',
            'z-index': '-1',
        }),

        # 3 слайд
        html.Div([
            html.Div([
                html.P(['Мы всегда открыты к предложениям',
                       html.Br(),
                       ' и сотрудничеству!'],
                       className='main-layout-header-text-2', style={
                        'text-align': 'center',
                        'font-size': '4vw',
                        'left': '18%',
                        'position': 'absolute',
                        'top': '20%',
                        'color': 'black',
                    }),
                html.H1("НАШИ КОНТАКТЫ", className="text-bold", style={
                    'position': 'absolute',
                    'top': '60%',
                    'left': '50%',
                    'transform': 'translate(-50%, -50%)',
                    'text-align': 'center',
                    'color': 'black',
                }),
                html.H1(['+1 234 567 89 00',
                         ], className="main-layout-header-text-2", style={
                    'position': 'absolute',
                    'top': '70%',
                    'left': '50%',
                    'transform': 'translate(-50%, -50%)',
                    'text-align': 'center',
                    'color': 'black',
                }),
                html.H1(['hello@company.com',
                         ], className="main-layout-header-text-2", style={
                    'position': 'absolute',
                    'top': '80%',
                    'left': '50%',
                    'transform': 'translate(-50%, -50%)',
                    'text-align': 'center',
                    'color': 'black',
                }),
            ]),

        ], style={
            'background-color': 'rgba(217, 217, 217, 0.26)',
            'height': '75vh',
            'background-size': 'cover',
            'background-position': 'center center',
            'position': 'relative',
            'z-index': '-1',
        }),

        # подвал
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

    ], style={'height': '100vh', 'z-index': '-1'}),

    return layout

from dash import html, dcc

def create_contacts_layout():
    layout = html.Div([
        # 1 слайд
        html.Div([
            html.Div([
                html.Div([
                    html.H1([
                        'Наша команда стремится создать для вас лучший',
                        html.Br(),
                        'сервис по анализу курса рубля'
                    ], className='main-layout-header-text-2', style={
                        'text-align': 'left',
                        'margin-top': '8vw',
                        'color': 'black',
                    }),
                    html.P('Будем рады услышать ваши честные отзывы!',
                           className='main-layout-text', style={
                               'text-align': 'left',
                               'font-size': '2vw',
                               'margin-top': '2vw'  # отступ сверху, чтобы текст не был вплотную к заголовку
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
                            'margin-top': '2vw',  # отступ сверху от текста
                        }),
                        href='https://forms.gle/46Y8vvtya9eCse6F6', style={'text-decoration': 'none'}),
                ], style={
                    'display': 'flex',
                    'flex-direction': 'column',
                    'align-items': 'flex-start',  # выравнивание по левому краю
                }),
                html.Img(src='/assets/Vectorcontacts1.png', style={
                    'height': '22vw',  # высота изображения, измените по необходимости
                    'margin-left': '0.4vw',  # отступ слева от изображения
                    'margin-top': '13vw',
                }),
            ], style={
                'display': 'flex',
                'align-items': 'flex-start',  # выравнивание по левому краю внутри блока
                'margin-left': '5vw',  # отступ слева от внешнего блока
                'margin-top': '0vw',  # отступ сверху от внешнего блока
                'color': 'black',
            }),
        ], style={
            'background-color': 'rgba(245, 245, 245, 1)',
            'height': '90vh',
            'background-size': 'cover',
            'background-position': 'center center',
            'position': 'relative',
            'z-index': '-1',
        }),

        # 2 слайд
        html.Div([
            html.Div([
                html.H1('Второй слайд', className='main-layout-header-text-2', style={
                    'text-align': 'left',
                    'color': 'black',
                    'margin-top': '0vh',  # отступ сверху
                }),
                html.Div([
                    html.Img(src='/assets/icon1.png', style={'height': '5vw', 'margin-top': '2vh', 'margin-left': '2vw'}),
                    html.Img(src='/assets/icon2.png', style={'height': '5vw', 'margin-top': '2vh', 'margin-left': '2vw'}),
                ], style={'display': 'flex'}),
                html.Img(src='/assets/hand-holding-megaphone-for-protest.png', style={'height': '40vh', 'margin-top': '5vh', 'margin-right': '5vw', 'float': 'right'}),
            ], style={
                'background-color': 'rgba(89, 95, 95, 1)',
                'height': '90vh',
                'position': 'relative',
            })
        ], style={'position': 'relative', 'z-index': -1}),

        # 3 слайд
        html.Div([
            html.H1('Третий слайд', className='main-layout-header-text-2', style={
                'text-align': 'left',
                'color': 'black',
                'margin-top': '0vh',  # отступ сверху
            }),
        ], style={
            'background-color': 'rgba(245, 245, 245, 1)',
            'height': '55vh',
            'position': 'relative',
            'z-index': '-1',
        })
    ])
    return layout

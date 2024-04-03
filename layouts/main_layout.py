from dash import html
import dash_bootstrap_components as dbc


def create_main_layout():
    layout = html.Div([
        html.Div([
            html.Div([
                html.H1('Будь в Курсе', className='main-layout-header-text', style={
                    'position': 'relative',
                    'top': '0%',
                    'left': '20%',
                    'transform': 'translate(-50%, -50%)',
                    'text-align': 'center',
                    'color': 'white',
                }),
                html.P('место, где собраны все новости, изменившие курс рубля не только сегодня',
                       className='main-layout-text'),
            ], style={
                'position': 'absolute',
                'top': '40%',
                'left': '50%',
                'transform': 'translate(-50%, -50%)',
                'text-align': 'center',
                'color': 'white',
            }),
        ], style={
            'background-image': 'url(/assets/main_jpeg.jpg)',
            'height': '87vh',
            'background-size': 'cover',
            'background-position': 'center center',
            'background-repeat': 'no-repeat',
            'position': 'relative',
        }),
    ], style={'height': '100vh', 'overflow': 'hidden'})  # Общий стиль для контейнера
    return layout

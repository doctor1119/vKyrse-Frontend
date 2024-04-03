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
                html.Div([
                    html.P('место, где собраны все новости, изменившие курс рубля не только сегодня',
                           className='main-layout-text'),
                    html.A(html.Button([
                        html.Span('Следить', className='follow-text'),
                        html.Span(' за курсом', className='currency-text')
                    ], id='follow-currency-button', className='follow-currency-button'), href='/currency-analysis'),
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
            'background-image': 'url(/assets/main_jpeg.jpg)',
            'height': '90vh',
            'background-size': 'cover',
            'background-position': 'center center',
            'position': 'relative',
        }),
        html.Div([ "Второй фон"
        ], style={
            'background-color': 'rgba(217, 217, 217, 0.26)',
            'height': '90vh',
            'background-size': 'cover',
            'background-position': 'center center',
            'position': 'relative',
        } ),
        html.Div(["Третий фон"
                  ], style={
            'background-image': 'url(assets/woman.jpg)',
            'height': '90vh',
            'background-size': 'cover',
            'background-position': 'center center',
            'position': 'relative',
        }),
        html.Div(["Четвертый фон"
                  ], style={
            'background-color': 'rgba(245, 245, 245, 1)',
            'height': '90vh',
            'background-size': 'cover',
            'background-position': 'center center',
            'position': 'relative',
        }),
        html.Div(["Пятый фон"
                  ], style={
            'background-image': 'url(assets/notebook.jpg)',
            'height': '90vh',
            'background-size': 'cover',
            'background-position': 'center center',
            'position': 'relative',
        }),
    ], style={'height': '100vh'})

    return layout

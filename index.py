from app import app
from routes.rout import serve_layout

app.layout = serve_layout

if __name__ == '__main__':
    app.run_server(debug=True)
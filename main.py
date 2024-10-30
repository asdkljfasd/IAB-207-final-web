from RhythmRally import create_app
from RhythmRally.views import mainbp

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
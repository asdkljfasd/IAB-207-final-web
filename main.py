from RhythmRally import create_app

# if database is not initialised, please run the command "python create_db.py"

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
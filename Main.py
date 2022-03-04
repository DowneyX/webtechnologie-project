from website import create_app

app = create_app()

if __name__ == '__main__':
    # turn debug off when in production
    app.run(debug=True)

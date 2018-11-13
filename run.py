"""Import creat_app from the base folder."""
from SendITapp import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)

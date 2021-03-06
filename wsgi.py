"""App entry point."""
from main import create_app

app = create_app()

if __name__ == "__main__":
    app.run(host='localhost', port=10216, threaded=False)

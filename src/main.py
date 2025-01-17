from argparse import ArgumentParser

import uvicorn

argparse = ArgumentParser()
argparse.add_argument('--host', default='0.0.0.0', help='Host to bind the server to.')
argparse.add_argument('--port', default=8000, type=int, help='Port to bind the server to.')

args = argparse.parse_args()

def main(host, port):
    """Run the API server."""
    from src import app
    uvicorn.run(app, host=host, port=port)

if __name__ == "__main__":
    main(args.host, args.port)

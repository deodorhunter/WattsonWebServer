from flask import Flask
from src import createApi, createApp
from src.main import HelloWorld
from src.endpoints.auth import authToServer
from src.endpoints.streaming import Streaming

app = createApp()
api = createApi(app)
api.add_resource(HelloWorld, '/')
api.add_resource(authToServer, '/auth')
api.add_resource(Streaming, '/stream')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug = True)

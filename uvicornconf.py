import os
import ssl
import sys
sys.path.insert(0, os.path.join(os.getcwd(), 'api'))

ssl_context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
ssl_context.load_cert_chain('/etc/letsencrypt/live/back.where2race.ru/fullchain.pem',
                            '/etc/letsencrypt/live/back.where2race.ru/privkey.pem')

if __name__ == "__main__":
    print(os.getcwd())
    print(os.listdir(os.getcwd()))
    import uvicorn
    uvicorn.run("api:app", host="127.0.0.1", port=8000, ssl = ssl_context)
    # uvicorn.run("api:app", host="0.0.0.0", port=8000)
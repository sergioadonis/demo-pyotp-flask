from flask import Flask, request
from flask.json import jsonify
from pyotp import TOTP, random_base32

from .clients import Client, ClientRepository


app = Flask(__name__)
def log(message): return app.logger.info(message)


TOTP_INTERVAL = 60


@app.route('/clients', methods=['GET'])
def get_clients():
    return jsonify(ClientRepository.get_clients())


@app.route('/clients', methods=['POST'])
def create_client():
    id = ClientRepository.get_next_id()
    name = request.json['name']
    phone = request.json['phone']
    secret = random_base32()
    client = Client(id, name, phone, secret)

    ClientRepository.save_client(client)

    return jsonify(client)


@app.route('/otp/<int:client_id>')
def generate_otp(client_id):
    client = ClientRepository.get_client_by_id(client_id)
    if (client):
        log(client)
        totp = TOTP(client.secret, interval=TOTP_INTERVAL)
        code = totp.now()
        log(f'Sending otp code {code}')
        return ('Code sent', 200)

    return ('Client not found', 404)


@app.route('/otp/<int:client_id>/<code>')
def verify_otp(client_id, code):
    client = ClientRepository.get_client_by_id(client_id)
    if (client):
        log(client)
        totp = TOTP(client.secret, interval=TOTP_INTERVAL)
        result = totp.verify(code)
        log(f'Is otp code {code} valid {result}')
        if (result):
            return ('Valid', 200)

        return ('Code not valid', 400)

    return ('Client not found', 404)

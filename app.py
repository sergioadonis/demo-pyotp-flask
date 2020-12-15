import os
from flask import Flask, request
from flask.json import jsonify
from pyotp import TOTP, random_base32


app = Flask(__name__)
def log(message): return app.logger.info(message)


TOTP_INTERVAL = 60


@app.route('/otp', methods=['POST'])
def create_totp():
    phone = request.json.get('phone', None)
    log(f'Phone: {phone}')
    email = request.json.get('email', None)
    log(f'Email: {email}')

    secret = random_base32()
    totp = TOTP(secret, interval=TOTP_INTERVAL)
    code = totp.now()
    log(f'Sending otp code {code}')

    response = {
        'ok': True,
        'message': 'Code sent',
        'secret': secret
    }

    return jsonify(response)


@app.route('/otp/<secret>/<code>', methods=['GET'])
def verify_totp_code(secret, code):
    log(f'Secret: {secret}')
    log(f'Code: {code}')

    totp = TOTP(secret, interval=TOTP_INTERVAL)
    result = totp.verify(code)
    log(f'Is otp code {code} valid {result}')
    if (result):
        return ('Valid', 200)

    return ('Code not valid', 400)


port = os.environ.get('PORT', default=5000)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, debug=True)

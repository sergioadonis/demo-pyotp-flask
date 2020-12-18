from os import environ
from flask import Flask, request
from flask.json import jsonify
from pyotp import TOTP, random_base32


app = Flask(__name__)

interval = int(environ.get('TOTP_INTERVAL', default=60))  # in seconds


@app.route('/generate-otp')
def generate_otp():
    try:
        phone = request.args.get('phone', None)
        app.logger.info(f'Phone: {phone}')
        shared_key = random_base32()
        app.logger.info(f'Shared key: {shared_key}')
        totp = TOTP(shared_key, interval=interval)
        code = totp.now()
        app.logger.info(f'Otp code: {code}')

        return jsonify({
            'ok': True,
            'message': f'Code sent to {phone}',
            'shared_key': shared_key
        })

    except Exception as error:
        app.logger.error(f'Exception {error}')
        return ('Error', 500)


@app.route('/verify-otp/<shared_key>/<code>')
def verify_otp(shared_key, code):
    try:
        app.logger.info(f'Shared key: {shared_key}, Code: {code}')
        totp = TOTP(shared_key, interval=interval)
        result = totp.verify(code)
        app.logger.info(f'Is otp code {code} valid? {result}')

        if (result):
            return ('Valid', 200)

        return ('Code not valid', 400)

    except Exception as error:
        app.logger.error(f'Exception {error}')
        return ('Error', 500)


port = environ.get('PORT', default=5000)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, debug=True)

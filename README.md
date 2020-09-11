# Demo: OTP Service with pyotp and Flask

This is a simple web service (made with Flask) to generate and verify otp codes for clients. Database is not necesary because pyotp calculate the code based on current time.

## Run locally

Just export the flask app name in FLAS_APP environment var, (optional) enable debug mode.
After that, run the flask app.

```
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```

## Clients

First, register some clients. Edit `data.json` file in order to create a client.
After that, test it with cURL, Postman or whatever.

```
curl 127.0.0.1:5000/clients -X POST -d @data.json -H "Content-Type: application/json"
curl 127.0.0.1:5000/clients
```

## OTP

Then, get and verify otp code for your clients.

```
curl 127.0.0.1:5000/otp/<SOME_CLIENT_ID>
curl 127.0.0.1:5000/otp/<SOME_CLIENT_ID>/<SOME_OTP_CODE>
```

Notes:

- Replace <SOME_CLIENT_ID> with some client id that you had post before.
- Replace <SOME_OTP_CODE> with some otp code, you can copy it from STDOUT (your terminal or cmd for example).

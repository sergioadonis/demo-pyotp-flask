# Demo: OTP Service with pyotp and Flask

This is a simple web service (made with Flask) to generate and verify otp codes for clients. Database is not necesary because pyotp calculate the code based on current time.

## Run locally using Docker

Just run the following commands.

```
docker build . -t demo-pyotp
docker run -d -p 81:5000 --name demo demo-pyotp
docker logs -f demo
```

The first one, build the image.
The second one, run the container using de previous image in detach mode and doing a porting to 81 port in the host.
The last one is to watch the logs.

**Optional**

You could override the internal port:

```
docker run -d -p 81:8000 -e PORT=8000 --name demo demo-pyotp
```

For example, use the 8000 port instead of 5000 default port.

Also, you could override the Interval Time for OTP (default is 60 seconds):

```
docker run -d -p 81:5000 -e TOTP_INTERVAL=300 --name demo demo-pyotp
```

For example, use the 300 seconds (5 minutes) instead of 60 default seconds.

## Try using cURL

Now, you can try with cURL, or whatever.

```
curl 127.0.0.1:81/generate-otp?phone=00000000
```

Then, verify otp code.

```
curl 127.0.0.1:81/<SOME_SHARED_KEY>/<SOME_OTP_CODE>
```

Notes:

- Replace <SOME_SHARED_KEY> with some shared key that you had received before.
- Replace <SOME_OTP_CODE> with some otp code, you can copy it from STDOUT (your terminal or cmd for example).

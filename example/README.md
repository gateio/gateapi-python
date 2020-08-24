# Example Application

This is a demo application using `gate-api` to show how Gate APIv4 works. 
Instead of running it, it is recommended to read the source code to get a general idea of
how this SDK is used. However, you can modify this code directly to implement your own logic.

## Build

1. Clone this project and make sure it is named with `gateapi-python`
2. Run `./build.sh`, then your demo application will be created beside `gateapi-python`

## Run

**READ THIS BEFORE YOU RUN ANYTHING**

**This application is shown for demo only. It will try to use your input API key and secret to
trade, lend and borrow, etc. Make sure you know exactly what it does before running it.**

> The build.sh script will try to initiate a virtualenv environment if it can find virtualenv
> executable. Follow what the script prints before running the demo application 

```bash
# run futures demo against TestNet
python app.py futures -k <YOUR_TESTNET_API_KEY> -s <YOUR_TESTNET_API_SECRET> -u fx-api-testnet.gateio.ws

# run futures demo against real trading
python app.py futures -k <YOUR_API_KEY> -s <YOUR_API_SECRET>

# run spot demo
python app.py spot -k <YOUR_API_KEY> -s <YOUR_API_SECRET>

# run margin demo
python app.py margin -k <YOUR_API_KEY> -s <YOUR_API_SECRET>
```

# How to Setup mitmproxy

## Install mitmproxy
[Watch this video tutorial](https://youtu.be/AacH2L_D2B8) for detailed instructions on installing mitmproxy.

## Download the Certificate
Ensure that you've downloaded the certificate required for mitmproxy.

## Configure Proxies
Make sure your proxy settings look like this:

![Proxy Settings](https://cdn.discordapp.com/attachments/1253210219127767084/1259369784403820544/image.png?ex=668b6f02&is=668a1d82&hm=c1fc9c53c9554d3fe5f26e215a0b07d487ce3aaccf2b6669328ef971acfc82f3&)

## Install mitmproxy Python Package
```sh
pip install mitmproxy
```

## Run Your Proxy Server
Run your proxy server and then execute the command `mitmdump -s ./main.py`.

## Additional Resources
This [getting started guide](https://docs.mitmproxy.org/stable/overview-getting-started/) might be useful.

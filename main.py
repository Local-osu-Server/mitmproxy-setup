from mitmproxy import http  # type: ignore
from mitmproxy.http import Response

import config

BASE_URL_FOR_OSU_CLIENT_SERVER = "http://localhost:5001"


class MyMitmproxy:
    async def request(self, flow: http.HTTPFlow) -> None:
        if flow.request.pretty_host.endswith(config.TEMPORARY_REDIRECT_DOMAIN):
            subdomain = flow.request.pretty_host.split(".")[0]
            location = flow.request.url.replace(
                f"https://{subdomain}.{config.TEMPORARY_REDIRECT_DOMAIN}",
                f"{BASE_URL_FOR_OSU_CLIENT_SERVER}/{subdomain}",
            )

            flow.response = Response.make(
                status_code=307,
                headers={"Location": location},
            )


addons = [MyMitmproxy()]

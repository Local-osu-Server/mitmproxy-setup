from mitmproxy import http  # type: ignore
from mitmproxy.http import Response

import config


class MyMitmproxy:
    async def request(self, flow: http.HTTPFlow) -> None:
        if flow.request.pretty_host.endswith(config.TEMPORARY_REDIRECT_DOMAIN):
            subdomain = flow.request.pretty_host.split(".")[0]
            location = flow.request.url.replace(
                f"https://{subdomain}.{config.TEMPORARY_REDIRECT_DOMAIN}",
                f"http://localhost:{config.OSU_SERVER_PORT}/{subdomain}",
            )

            flow.response = Response.make(
                status_code=307,
                headers={"Location": location},
            )


addons = [MyMitmproxy()]

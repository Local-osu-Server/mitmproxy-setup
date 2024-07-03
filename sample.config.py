# mitmproxy needs a domain to initially connect to due to DNS issues.
# We redirect the traffic to a private server domain solely for the purpose of redirecting it back to localhost.
# This redirection does not interfere with the private server itself.
TEMPORARY_REDIRECT_DOMAIN = ""  # Example: ripple.moe

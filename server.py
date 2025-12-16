# server.py
# Version: 1.0.5

from mcp.server.fastmcp import FastMCP
import ipaddress

mcp = FastMCP("tf-ip-tools")

@mcp.tool()
def cidrsubnet(base_cidr: str, newbits: int, netnum: int) -> str:
    base = ipaddress.ip_network(base_cidr, strict=False)
    new_prefix = base.prefixlen + newbits

    if new_prefix > base.max_prefixlen:
        raise ValueError("prefix too large")

    subnets = base.subnets(new_prefix=new_prefix)
    for i, subnet in enumerate(subnets):
        if i == netnum:
            return str(subnet)

    raise ValueError("netnum out of range")


@mcp.tool()
def cidrsubnet_params(base_cidr: str, target_ip: str) -> dict:
    """
    Inverse Terraform cidrsubnet.
    Works for IPv4 and IPv6.
    """
    base = ipaddress.ip_network(base_cidr, strict=False)
    target = ipaddress.ip_address(target_ip)

    if target.version != base.version:
        raise ValueError("IP version mismatch")

    if target not in base:
        raise ValueError("target_ip not inside base_cidr")

    offset = int(target) - int(base.network_address)

    # iterate possible subnet sizes
    for new_prefix in range(base.prefixlen + 1, base.max_prefixlen + 1):
        block_size = 1 << (base.max_prefixlen - new_prefix)

        if offset % block_size == 0:
            netnum = offset // block_size
            newbits = new_prefix - base.prefixlen

            return {
                "newbits": int(newbits),
                "netnum": int(netnum),
                "cidr": f"{target}/{new_prefix}",
                "ip_version": base.version
            }

    raise ValueError("unable to compute cidrsubnet parameters")


if __name__ == "__main__":
    mcp.run()

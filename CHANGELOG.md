# Changelog

## 1.0.0
- Initial MCP server skeleton using FastMCP (stdio mode)
- Added basic IPv4 CIDR utilities
- Verified compatibility with LM Studio stdio MCP

## 1.0.1
- Fixed startup/import issues related to incorrect MCP package usage
- Standardized server execution with `mcp.run()`
- Removed all stdout logging to avoid MCP connection drops

## 1.0.2
- Added core Terraform-style helpers:
  - `cidrhost`
  - `ip_to_cidr`
  - `ip_in_cidr`
- Ensured strict MCP stdio behavior (no prints, no logs)

## 1.0.3
- Added Terraform-compatible `cidrsubnet`
- Matches Terraform behavior for `newbits` and `netnum`
- Enables forward CIDR calculation from base network

## 1.0.4
- Added inverse Terraform helper `cidrsubnet_params`
- Computes `newbits` and `netnum` from:
  - base CIDR
  - target subnet start IP
- Eliminates manual subnet math for operators

## 1.0.5
- Added full IPv6 support to:
  - `cidrsubnet`
  - `cidrsubnet_params`
- Enforced IP version consistency (IPv4 vs IPv6)
- Implemented integer-based math safe for large IPv6 spaces
- Optimized to avoid subnet list explosion

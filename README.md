# tf-ip-tools

#OVERVIEW
______________________________________________________________________________________________________
CIDR calculator - ipaddress <-> cidr, and calcules newbits and netnum from a cidr or ipaddress. SUPPORTS IPv6

#INSTALL
______________________________________________________________________________________________________

Clone the repository

git clone https://github.com/jlberlanga/MCP-cidr.git

#Install requeriments
______________________________________________________________________________________________________
pip install -r requeriments.txt


- You can use as MCP/Tool in any client, eg: LMStudio or
JSON FORMAT EXAMPLE:
______________________________________________________________________________________________________
**LMStudio**

"mcpServers": {
  "tf-ip-tools": {
    "command": "python",
    "args": [
      "server.py"
    ]
  }
}

**OPENCODE**

"mcp":{
  "tf-ip-tools": {
    "type": "local",
    "enabled": true,
    "command": [
      "python",
      "server.py"
    ]
  }
}

**CLINE**


"mcpServers": {
  "tf-ip-tools": {
   "command": "/mnt/2TB/Scripts/gemini-codex/MCP-cidr/venv/bin/python",
    "args": [
     "/mnt/2TB/Scripts/gemini-codex/MCP-cidr/server.py"
     ]
  }
}

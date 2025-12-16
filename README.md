# tf-ip-tools

##OVERVIEW
______________________________________________________________________________________________________
CIDR calculator - ipaddress <-> cidr, and calcules newbits and netnum from a cidr or ipaddress. SUPPORTS IPv6


##INSTALL
______________________________________________________________________________________________________

- Clone the repository
```
git clone https://github.com/jlberlanga/MCP-cidr.git
```

- Install requeriments
```
pip install -r requeriments.txt
```


## You can use as MCP/Tool in any client, eg: LMStudio or
JSON FORMAT EXAMPLE:
______________________________________________________________________________________________________

**LMStudio**
```json
"mcpServers": {
  "tf-ip-tools": {
    "command": "python",
    "args": [
      "server.py"
    ]
  }
}
```

**OPENCODE**
```json
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
```

**CLINE**
```json
"mcpServers": {
  "tf-ip-tools": {
   "command": "/mnt/2TB/Scripts/gemini-codex/MCP-cidr/venv/bin/python",
    "args": [
     "/mnt/2TB/Scripts/gemini-codex/MCP-cidr/server.py"
     ]
  }
}
```

<img width="986" height="499" alt="image" src="https://github.com/user-attachments/assets/29925f76-158e-4d19-b833-95524e6cb4c8" />
<img width="340" height="101" alt="image" src="https://github.com/user-attachments/assets/b53d6438-4f09-48a0-9a09-abe5ccb90835" />

from http.server import HTTPServer, SimpleHTTPRequestHandler
import socketserver
import requests
from sys import argv
import os

class Util:
    def __init__(self):
        self.tools = {
            "winpeas.exe": "https://github.com/carlospolop/PEASS-ng/releases/download/20230122/winPEASany.exe",
            "privesccheck.ps1": "https://raw.githubusercontent.com/itm4n/PrivescCheck/master/PrivescCheck.ps1",
            "ncat.zip": "https://nmap.org/dist/ncat-portable-5.59BETA1.zip",
            "accesschk.zip": "https://download.sysinternals.com/files/AccessChk.zip",
            "accessenum.zip": "https://download.sysinternals.com/files/AccessEnum.zip"
        }
        
    def get_tool(self, file, url):
        # thanks stackoverflow
        lf = "downloads/"+file
        with requests.get(url, stream=True) as r:
            r.raise_for_status()
            with open(lf, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192): 
                    f.write(chunk)
        return lf, url.split(".")[-1]

    def download_tools(self):
        if not os.path.isdir("downloads"):
            os.mkdir("downloads")

        print("Downloading all the tools!")
        for tool in self.tools:
            print(f"Downloading {tool}...")
            self.get_tool(tool, self.tools[tool])

if __name__ == "__main__":
    PORT = 8000
    DIRECTORY = "./downloads"
    class Handler(SimpleHTTPRequestHandler):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, directory=DIRECTORY, **kwargs)

        def log_request(content="-", size="-"):
            pass

    util = Util()

    if len(argv) < 2:
        print(f"Usage: python3 {argv[0]} <function>")
        print("Functions: download, serve")
        exit()

    arg = argv[1]

    if arg == "download":
        util.download_tools()
    elif arg == "serve":
        socketserver.TCPServer.allow_reuse_address = True
        httpd = socketserver.TCPServer(("", PORT), Handler)
        print("Serving at port", PORT, "- REQUESTS ARE NOT BEING LOGGED!")
        try:
            httpd.serve_forever()
        except:
            httpd.shutdown()
            httpd.server_close()
    else:
        print("Unknown function")
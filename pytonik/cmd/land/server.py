from pytonik import serv
import os

LOCAL_PORT = 6060

port = int(os.environ.get("PORT", LOCAL_PORT))
host = "localhost" if os.environ.get("PORT") == None else ""
serv.run(host=host, port=port)

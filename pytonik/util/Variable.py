# Author : BetaCodings
# Author : info@betacodings.com
# Maintainer By: Emmanuel Martins
# Maintainer Email: emmamartinscm@gmail.com
# Created by BetaCodings on 3/4/20.
import os, sys
from pytonik import Version


class Variable:

    def __getattr__(self, item):
        return item

    def __init__(self):
        return None

    def put(self, path="", host="", port="", para="", status=200, accept="", method="GET", cookies="", session="", referral="", remoter_addr="", remoter_port="", script_file="", server_proto="", server_ver="", protocol_ver="", redirect_url="", ssl_v=""):
        uri, query_string = "", ""  # path.split('/')[-1]+str(para)
        host = str(host) if str(
            host) != "" else os.environ.get("HTTP_HOST", "")
        
        port = str(port) if str(
            port) != "" else os.environ.get("SERVER_PORT", "")
        
        path = str(path) if str(
            path) != "" else os.environ.get("PATH_INFO", "")
    
        ssl_v = str(ssl_v) if str(
            ssl_v) != "" else os.environ.get("HTTPS", "")
        
        
        status = str(status) if status != "" else os.environ.get(
            "REDIRECT_STATUS", "")
        
        
        
        remoter_addr = str(remoter_addr) if remoter_addr != "" else os.environ.get(
            "REMOTE_ADDR", "")
        
        remoter_port = str(remoter_port) if remoter_port != "" else os.environ.get(
            "REMOTE_PORT", "")
         
        script_file = str(script_file) if script_file != "" else os.environ.get(
            "SCRIPT_FILENAME", "")
        
        

        server_ver = str(server_ver) if server_ver != "" else os.environ.get(
            "SERVER_VERSION", "")

        cookies = str(cookies) if str(
            cookies) != "" else os.environ.get("HTTP_COOKIE", "")
        

        session = str(session) if str(
            session) != "" else os.environ.get("HTTP_SESSION", "")
        
        v_referral = ""
        if os.environ.get("HTTP_REFERER", "") != "":
            if para == referral:
                v_referral = ""
            else:
                v_referral = referral if referral != "" else os.environ.get("HTTP_REFERER", "")
        else:
            v_referral = para
       
        server_proto = str(server_proto) if str(
            server_proto) != "" else os.environ.get("SERVER_PROTOCOL", "")
      
        protocol_ver = str(protocol_ver) if str(
            protocol_ver) != "" else os.environ.get("PROTOCOL_VERSION", "")
        
        redirect_url = str(redirect_url) if str(
            redirect_url) != "" else os.environ.get("REDIRECT_URL", "")
      
        if para.find("?") == True:
            parts = para.split('?')
            if len(parts) > 1:
                uri = parts[0]
                query_string = parts[1]
            else:
                uri = ""
                query_string = parts[0]

        else:
            query_string = ""
            uri = ""
        server_software = Version.AUTHOR+"/"+Version.VERSION_TEXT if Version.AUTHOR != "" else os.environ.get("SERVER_SOFTWARE", "")
        env = {
            "Framework": Version.AUTHOR if Version.AUTHOR != "" else os.environ.get("Framework", ""),
            "X-Version": Version.VERSION_TEXT if Version.VERSION_TEXT != "" else os.environ.get("X-Version", ""),
            "X-Organisation": Version.ORG if Version.ORG != "" else os.environ.get("X-Organisation", ""),
            "PATH_INFO": para,
            "HTTP_HOST": host,
            "HTTPS": ssl_v,
            "SERVER_PORT": port,
            "HTTP_COOKIE": cookies,
            "HTTP_SESSION": session,
            "REDIRECT_STATUS": status,
            "REMOTE_ADDR": remoter_addr,
            "REMOTE_PORT": remoter_port,
            "SCRIPT_FILENAME": script_file,
            "HTTP_CONNECTION": "keep-alive",
            "HTTP_ACCEPT": str(accept) if accept != "" else os.environ.get("HTTP_ACCEPT", ""),
            "DOCUMENT_ROOT": path,
            "REQUEST_METHOD": str(method) if method != "" else os.environ.get("REQUEST_METHOD", ""),
            "QUERY_STRING": str(query_string),
            'SERVER_SOFTWARE': Version.AUTHOR,
            'PATH_TRANSLATED': str(path) + "/public",
            'SERVER_SIGNATURE':  "{server_software} {sys_os} PYTHON/{py_version} Server at {host} Port {port}".format(py_version=str(sys.version_info.major) + "."+ str(sys.version_info.minor) + "."+ str(sys.version_info.micro), sys_os=sys.platform, server_software=server_software,host=host, port=port),
            'HTTP_REFERER': v_referral,
            'SERVER_PROTOCOL': server_proto,
            'SERVER_VERSION': server_ver,
            'REDIRECT_URL': redirect_url,
            'PROTOCOL_VERSION': protocol_ver,
            "REQUEST_URI": "/"+str(os.path.basename(os.getcwd()))+str(para)
        }
        
        if Version.PYVERSION_MA <= 2:
            lt = env.iteritems()
        else:
            lt = env.items()
        if os.environ.get("REQUEST_URI", "") != "" or os.environ.get("REQUEST_URI", "") != None:
            os.environ.clear()
            os.environ.update(dict(env))

        for k, v in lt:
            os.environ.setdefault(str(k), str(v).encode())

        os.environ.update(dict(REQUEST_URI=os.environ.get("REQUEST_URI")))

    def out(self, key, alt=""):
        return os.environ.get(key, alt)

    def see(self):
        return os.environ

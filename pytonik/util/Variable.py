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

    def put(self, accept_lang="", http_user_agt="", http_encode="",  http_connect="", path="", host="", port="", para="", status=200, accept="", method="", referral="", remoter_addr="", remoter_port="", script_file="", server_proto="", server_ver="", protocol_ver="", redirect_url="", ssl_v=""):
        
        uri, query_string = "", ""  # path.split('/')[-1]+str(para)
        
        host = str(host) if str(host) != "" else os.environ.get("HTTP_HOST", "")
        para_v = "/"+str(os.path.basename(os.getcwd()))+str(para) if str(para) != "" else os.environ.get("REQUEST_URI", "")
        
        port = str(port) if str(port) != "" else os.environ.get("SERVER_PORT", "")
        
        path = str(path) if str(path) != "" else os.environ.get("PATH_INFO", "")
        
        accept_lang = str(accept_lang) if str(accept_lang) != "" else os.environ.get("HTTP_ACCEPT_LANGUAGE", "")
        
        http_connect  = str(http_connect) if str(http_connect) != "" else os.environ.get("HTTP_CONNECTION", "")
        
        http_user_agt = str(http_user_agt) if str(http_user_agt) != "" else os.environ.get("HTTP_USER_AGENT", "")
        
        http_encode = str(http_encode) if str(http_encode) != "" else os.environ.get("HTTP_ACCEPT_ENCODING", "")
    
        ssl_v = str(ssl_v) if str(ssl_v) != "" else os.environ.get("HTTPS", "")
        
        
        status = str(status) if status != "" else os.environ.get("REDIRECT_STATUS", "")
        status = str(status) if status != "" else os.environ.get("REDIRECT_REDIRECT_STATUS", "")

        http_status = str(status) if status != "" else os.environ.get("HTTP_STATUS", "")
        
        remoter_addr = str(remoter_addr) if remoter_addr != "" else os.environ.get("REMOTE_ADDR", "")
        
        remoter_port = str(remoter_port) if remoter_port != "" else os.environ.get("REMOTE_PORT", "")
         
        script_file = str(script_file) if script_file != "" else os.environ.get("SCRIPT_FILENAME", "")
    
        server_ver = str(server_ver) if server_ver != "" else os.environ.get("SERVER_VERSION", "")

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
        
        
        
        redirect_url = str(redirect_url) if str(redirect_url) != "" else os.environ.get("REDIRECT_URL", "")
      
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
            "HTTP_HOST": host.replace(":80", ""),
            "HTTP_STATUS": http_status,
            "HTTPS": ssl_v,
            "SERVER_PORT": port,
            "REDIRECT_STATUS": status,
            "REDIRECT_REDIRECT_STATUS": status,
            "REMOTE_ADDR": remoter_addr,
            "REMOTE_PORT": remoter_port,
            "SCRIPT_FILENAME": script_file,
            "HTTP_CONNECTION": http_connect, 
            "HTTP_ACCEPT_LANGUAGE": accept_lang,
            "HTTP_ACCEPT_ENCODING": http_encode,
            "HTTP_USER_AGENT": http_user_agt,
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
            "REQUEST_URI": para_v
        }
        
        
        if Version.PYVERSION_MA <= 2:
            lt = env.iteritems()
        else:
            lt = env.items()
        if os.environ.get("REQUEST_URI", "") != "" or os.environ.get("REQUEST_URI", "") != None:
            #os.environ.clear()
            os.environ.update(dict(env))
        
        for k, v in lt:
            if k not in os.environ:
                self.default(str(k), str(v).encode())
            else:
                upd = {str(k): str(v)}
                self.update(dict(upd))
            

    def out(self, key, alt=""):
        return os.environ.get(key, alt)

    def see(self):
        return os.environ
    
        
    def default(self, key, value):
        if key in os.environ:
            upd = {str(key) : str(value)}
            return self.update(dict(upd))
        else:
            return os.environ.setdefault(str(key), str(value))
    
              
    def update(self, value=dict):
        return os.environ.update(value)
    
        
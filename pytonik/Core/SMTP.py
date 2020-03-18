###
# Author : Betacodings
# Author : info@betacodings.com
# Maintainer By: Emmanuel Martins
# Maintainer Email: emmamartinscm@gmail.com
# Created by Betacodings on 2019.
###


import smtplib, string, random
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os

from pytonik import Router, Config, Log
log_msg = Log.Log()


class SMTP():

    def __init__(self):

        self.Router = Router.Router()
        self.envSMTP = self.Router.env()

        Conf = Config.Config()

        Conf.add(self.envSMTP)
        setting = Conf.get('SMTP')
        self.server = setting.get('server', '')
        self.port = setting.get('port', '')
        self.username = setting.get('username', '')
        self.password = setting.get('password', '')

        self.con = None
        self.result = None
        self.response = None
        self.attachfile = None
        self.connect()
        return None

    def connect(self):
        try:
            self.response = smtplib.SMTP(self.server, self.port)
            self.response.starttls()
            self.response.login(self.username, self.password)
            return self.response
        except Exception as err:
            log_msg.error(err)


    def close(self):
        return self.response.quit()


    def send(self, from_send, to_recipient, message_subject= "", messege_content = "", header="html"):
        try:
            body = messege_content
            msg = MIMEMultipart()
            msg['From'] = from_send
            msg['To'] = to_recipient
            msg['Subject'] = message_subject
            msg.attach(MIMEText(body, header))
            if self.attachfile != None:
                msg.attach(self.attachfile)

            context = msg.as_string()
            self.response.sendmail(from_send, to_recipient, context)
            self.close()
            return True
        except Exception as err:
            log_msg.error(err)
            return err

    def attach(self, atfile = "", rename=""):
        if atfile != "":
            try:
                ext = os.path.splitext(atfile)[1][1:]
                filename = atfile if rename == "" else str(rename) + '.' + str(ext)
                attach_file = open(atfile, 'rb')
                attach_load = MIMEBase('application', 'octet-stream')
                attach_load.set_payload(attach_file.read())
                encoders.encode_base64(attach_load)
                attach_load.add_header('Content-Disposition', 'attachment', filename=filename)
                self.attachfile = attach_load

            except Exception as err:
                try:
                    ext =  os.path.splitext(atfile.filename)[1][1:]
                    filename = atfile.filename if rename == "" else str(rename)+'.'+str(ext)
                    attach_load = MIMEBase('application', 'octet-stream')
                    read_attach_file = (atfile.file).read()
                    attach_load.set_payload(read_attach_file)
                    encoders.encode_base64(attach_load)
                    attach_load.add_header('Content-Disposition', 'attachment',  filename=filename)

                    self.attachfile = attach_load

                except Exception as err:

                    log_msg.error(err)

        return self


    def retrieve(self):
        return self.response.getreply()
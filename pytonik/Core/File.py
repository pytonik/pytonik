###
# Author : Betacodings
# Author : info@betacodings.com
# Maintainer By: Emmanuel Martins
# Maintainer Email: emmamartinscm@gmail.com
# Created by Betacodings on 2019.
###


import os, base64, struct, io
from pytonik import App, Log

log_msg = Log.Log()

try:
    from PIL import Image as IMG
except Exception as err:
    log_msg.critical(err)



type_to_content_type = {
    "gif": "image/gif",
    "jpg": "image/jpeg",
    "jpeg": "image/jpeg",
    "pdf": "application/pdf",
    "png": "image/png",
}
type_to_standardized = {
    "gif": "gif",
    "jpg": "jpg",
    "jpeg": "jpg",
    "pdf": "pdf",
    "png": "png",
}


def upload(fileitem, uploaddir, rename=""):
    if os.path.isdir(os.path.dirname(uploaddir)):
        if fileitem.filename != "":
            if rename == "":
                fname = os.path.basename(fileitem.filename)
            else:
                fname = str(rename) + os.path.basename(fileitem.filename)

            try:
                
                with open(str(uploaddir)+str(fname), 'wb') as result:
                    result.write(fileitem.file.read())
                    result.close()
                return True
            except Exception as err:
                log_msg.critical(err)
                return err

        else:
            return ""
    else:
        log_msg.error("Directory {uploaddir} Does not Exist".format(uploaddir=uploaddir))
        return "Directory {uploaddir} Does not Exist".format(uploaddir=uploaddir)


def delete(directory, file):
    if os.path.isfile(str(directory)+str(file)):
        return os.remove(str(directory)+str(file))
    else:
        log_msg.error("The file {file} does not exist ".format(file=file))
        return "The file {file} does not exist ".format(file=file)

def ext(filename):
    fn = os.path.splitext(filename)[1][1:]
    return fn


class Image():


    
    def __init__(self, dir="", items=""):
        self.s = ""
        self.items = items
        self.dir = dir
        self.blobbase = ""
        self.buffer = ""
        self.pickle = ""
        self.App = App.App()
        self.ext = ""
        self.w = ""
        self.h = ""

        if self.items != "":

            self.read = self.items.file.read()
            self.filename = self.items.filename
        else:
            self.read = ""
            self.filename = ""

    def size(self):
        size = len(self.items.value)
        return size

    def resize(self, width, height, rename=str("")):

        if rename == "":
            fname = os.path.basename(self.items.filename)
        else:
            fname = str(rename) + os.path.basename(self.items.filename)
        try:
            self.blob()
            self.w = width
            self.h = height
            self.ext = ext(self.filename)
            self.filename = str(width) + 'x' + str(height) + '_' + str(fname)
            result = self.creator()
            return True


        except Exception as err:
            log_msg.critical(err)
            return err

    def blob(self):
        self.blobbase = base64.b64encode(self.read)
        return self.blobbase

    def dimension(self):
        height = -1
        width = -1
        head = self.read
        size = len(head)
        fhandle = self.items.file

        if size >= 10 and head[:6] in (b'GIF87a', b'GIF89a'):

            # Check to see if content_type is correct
            try:
                width, height = struct.unpack("<hh", head[6:10])
            except struct.error:
                raise ValueError("Invalid GIF file")
        # see png edition spec bytes are below chunk length then and finally the
        elif size >= 24 and head.startswith(b'\211PNG\r\n\032\n') and head[12:16] == b'IHDR':

            try:
                width, height = struct.unpack(">LL", head[16:24])
            except struct.error:
                raise ValueError("Invalid PNG file")
        # Maybe this is for an older PNG version.
        elif size >= 16 and head.startswith(b'\211PNG\r\n\032\n'):

            # Check to see if we have the right content type
            try:
                width, height = struct.unpack(">LL", head[8:16])
            except struct.error:
                raise ValueError("Invalid PNG file")
        # handle JPEGs
        elif size >= 2 and head.startswith(b'\377\330'):
            # \xff\xd8\xff\xe0\x00
            try:

                fhandle.seek(0)  # Read 0xff next
                size = 2
                ftype = 0
                while not 0xc0 <= ftype <= 0xcf or ftype in [0xc4, 0xc8, 0xcc]:
                    # fhandle.seek(size, 1)
                    byte = fhandle.read(1)
                    while ord(byte) == 0xff:
                        byte = fhandle.read(1)
                    ftype = ord(byte)
                    size = struct.unpack('>H', fhandle.read(2))[0] - 2
                # We are at a SOFn block
                fhandle.seek(1, 1)  # Skip `precision' byte.
                height, width = struct.unpack('>HH', fhandle.read(4))

            except struct.error:
                raise ValueError("Invalid JPEG file")
        # handle JPEG2000s
        elif size >= 12 and head.startswith(b'\x00\x00\x00\x0cjP  \r\n\x87\n'):
            fhandle.seek(48)

            try:
                height, width = struct.unpack('>LL', fhandle.read(8))
            except struct.error:
                raise ValueError("Invalid JPEG2000 file")


        # handle big endian TIFF
        elif size >= 8 and head.startswith(b"\x4d\x4d\x00\x2a"):
            offset = struct.unpack('>L', head[4:8])[0]
            fhandle.seek(offset)
            ifdsize = struct.unpack(">H", fhandle.read(2))[0]
            for i in range(ifdsize):
                tag, datatype, count, data = struct.unpack(">HHLL", fhandle.read(12))
                if tag == 256:
                    if datatype == 3:
                        width = int(data / 65536)
                    elif datatype == 4:
                        width = data
                    else:
                        raise ValueError("Invalid TIFF file: width column data type should be SHORT/LONG.")
                elif tag == 257:
                    if datatype == 3:
                        height = int(data / 65536)
                    elif datatype == 4:
                        height = data
                    else:
                        raise ValueError("Invalid TIFF file: height column data type should be SHORT/LONG.")
                if width != -1 and height != -1:
                    break
            if width == -1 or height == -1:
                raise ValueError("Invalid TIFF file: width and/or height IDS entries are missing.")
        elif size >= 8 and head.startswith(b"\x49\x49\x2a\x00"):
            offset = struct.unpack('<L', head[4:8])[0]
            fhandle.seek(offset)
            ifdsize = struct.unpack("<H", fhandle.read(2))[0]
            for i in range(ifdsize):
                tag, datatype, count, data = struct.unpack("<HHLL", fhandle.read(12))
                if tag == 256:
                    width = data
                elif tag == 257:
                    height = data
                if width != -1 and height != -1:
                    break
            if width == -1 or height == -1:
                raise ValueError("Invalid TIFF file: width and/or height IDS entries are missing.")

        return width, height

    def show(self, target="image/png"):
        decode = self.blobbase.decode('utf-8')
        data = "data:{};base64,{}".format(target, decode)
        return data

    def open(self):
        if self.file_exist() == True:
            try:

                with open(str(self.dir) + str(self.filename), 'rb') as rb:
                    self.read = rb.read()
                    return self.read
            except Exception as err:
                log_msg.critical(err)
                return err

    def save(self, img_tmp):
        try:
            with open(self.dir + self.filename, 'wb') as result:
                result.write(img_tmp)
                result.close()
            return True
        except Exception as err:
            log_msg.critical(err)
            return err

    def dir_exist(self):
        if os.path.isdir(os.path.dirname(self.dir)):
            return True
        else:
            return False

    def file_exist(self):
        if os.path.isfile(str(self.dir) + str(os.path.basename(self.filename))):
            return True
        else:
            return False

    def upload(self, rename=str(""), uploaddir=""):

        if self.items.filename != "":
            if rename == "":
                fname = os.path.basename(self.items.filename)
            else:
                fname = str(rename)+ str(os.path.basename(self.items.filename))
            
            if uploaddir != "":
                dir_folder = uploaddir
            else:
                dir_folder = self.dir  
            try:

                # result = open(self.dir + fname, 'wb')
                with open(str(dir_folder)+str(fname), 'wb') as result:
                    result.write(self.read)
                    result.close()
                return True
            except Exception as err:
                log_msg.critical(err)
                return err

        else:
            return ""



    def creator(self):

        for k in type_to_content_type:
            if self.ext.lower() in k:
                decode = base64.b64decode(self.blobbase)
                try:
                    img = IMG.open(io.BytesIO(decode))
                    resizedIMG = img.resize((self.w, self.h), IMG.ANTIALIAS)
                    resizedIMG.save(self.dir + self.filename, img.format)
                except Exception as err:
                    log_msg.critical(err)
                    return err

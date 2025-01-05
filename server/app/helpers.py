from flask import request
import qrcode
import io
import base64

#Creates QRcode
def getQRcode(uuid):
    img = qrcode.make(f'{request.host}/controller/{uuid}')
    img_io = io.BytesIO()
    img.save(img_io, 'JPEG')
    img_io.seek(0)

    

    return img_io



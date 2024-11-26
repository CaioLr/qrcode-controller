import qrcode
import io

def getQRcode(uuid):
    img = qrcode.make(f'http://127.0.0.1:5000/controller/{uuid}')
    img_io = io.BytesIO()
    img.save(img_io, 'JPEG')
    img_io.seek(0)

    return img_io
import qrcode as qr

class qr_generator:
    def create_qr(self):
        img = qr.make("https://www.facebook.com/jkd786")
        img.save("jd_fb.png")

    def create_qr_with_boarder(self):
        qrCode = qr.QRCode(version=1, error_correction=qr.constants.ERROR_CORRECT_H,box_size=15, border=6)
        qrCode.add_data("https://www.facebook.com/jkd786")
        qrCode.make(fit=True)
        img = qrCode.make_image()
        img.save("jd_fb_1.png")

    


if __name__ == '__main__':
    qg = qr_generator
    print(qg.create_qr(qg))
    print(qg.create_qr_with_boarder(qg))

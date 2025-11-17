# install all the libraries needeed 
# create a function that collectss the text and coverts it to qr code
# save the qr code as an image
# run the function

import qrcode
def generate_qr(text):

    qr = qrcode.QRCode(
        version=1,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    ) 
    qr.add_data(text)
    qr.make(fit=True)
    img= qr.make_image(fill_color="pink",back_color="white")
    img.save("qrimg.png")

generate_qr("https://github.com/AjurshaDahal")    
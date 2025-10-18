import qrcode

data = input('Enter the text or URL: ').strip()
filename = input('Enter the filename to be saved on the QR code: ').strip()
                        #  image file extension check
if not filename:
    filename = 'qr.png'
elif not filename.lower().endswith(('.png', '.jpg', '.jpeg')):
    filename += '.png'

                      # build QR
qr = qrcode.QRCode(box_size=10, border=4)
qr.add_data(data)
qr.make(fit=True)                    # <<-- generate the QR matrix

                      # create and save image
img = qr.make_image(fill_color='black', back_color='white')
img.save(filename)                   # <<-- save the PIL Image

print(f"QR code saved as {filename}")


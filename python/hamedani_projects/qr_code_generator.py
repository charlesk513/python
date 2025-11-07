import qrcode
# data = input('Enter the text or URL: ').strip()
# filename = input('Enter the filename: ').strip()
# qr = qrcode.QRCode(box_size = 10, border = 4)
# qr.add_data(data)
# qr.make_image(fill_color = 'black', back_color = 'white')
# qr.save(filename)
# print(f"QR code saved as {filename}")


# data = input('Enter the text or URL: ').strip()
# filename = input('Enter the filename to be saved on the QR code: ').strip()
# #  image file extension check
# if not filename:
#     filename = 'qr.png'
# elif not filename.lower().endswith(('.png', '.jpg', '.jpeg')):
#     filename += '.png'

# # build QR
# qr = qrcode.QRCode(box_size=10, border=4)
# qr.add_data(data)
# qr.make(fit=True)                    # <<-- generate the QR matrix

# # create and save image
# img = qr.make_image(fill_color='black', back_color='white')
# img.save(filename)                   # <<-- save the PIL Image

# print(f"QR code saved as {filename}")



# simpler code using qrcode.make()
data = input('Enter the text or URL: ').strip()
filename = input('Enter filename (e.g. qr.png): ').strip() or 'qr.png'
if not filename.lower().endswith('.png'):
    filename += '.png'

img = qrcode.make(data)  # returns a PIL Image
img.save(filename)

print(f"Saved {filename}")

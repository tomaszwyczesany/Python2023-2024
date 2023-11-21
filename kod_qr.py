# pip3 install qrcode
# Importing library
import qrcode

# Data to be encoded
data = 'https://lo-niepolomice.pl'

# Encoding data using make() function
img = qrcode.make(data)

# Saving as an image file
img.save('lo.png')
print("QR Code generated successfully.")
#modules
import qrcode
import os

QRfilename = "QRcode{}.JPG"
count = 0

codewords = input("What would you like embedded in your QR code?: ")
qrcolor = input("What color do you want your QR code?: ")

#checks if file already exist, if it does it creates a new file as not too over write the old one
while os.path.isfile(QRfilename.format(count)):
    count += 1
QRfilename= QRfilename.format(count)


#qr customization
codesize = qrcode.QRCode(version =1 , box_size = 5, border =5)

codesize.add_data(codewords)


codesize.make(fit = True)
img = codesize.make_image(fill_color = qrcolor,
					back_color = 'white')


img.save(QRfilename)

print ("Fantastic! your file has been saved as " + QRfilename)


    

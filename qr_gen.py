import qrcode as qr 
import sys 
try:
    text = sys.argv[1]
    if text == "-h":
        print("Syntax: qr_gen.py <string>")
    else:
        img = qr.make(text)
        img.save("QR_"+text+".jpg")
except:
    print("Please provide single string to generate code for")
    
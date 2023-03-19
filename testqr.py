# importing qrcode module

import qrcode


if __name__ == "__main__":
  print("Генератор QR")
  print("Checking Compability")
  print("Govnosborkinosoft 2023")

  text = input("Qr Text: ") # Enter the text you want to make the QR Code of..
  filename = input("Enter Filename: ") # Enter the file name you want to saved after the QR Code is made

  img = qrcode.make(text) # Making the QR Code via make() function of qrcode
  img.save(filename + ".png") # Saving it

  print("Success!!")
  print("file" + filename + ".png" + "Created")
  print("Vk.com/cackemc")

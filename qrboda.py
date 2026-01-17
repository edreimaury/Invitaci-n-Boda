import qrcode

url = "https://edreimaury.github.io/Boda-de-Lis-y-Edrei/"

qr = qrcode.make(url)
qr.save(r"C:\Users\Usuario\OneDrive\Desktop\Python\asistente\QR_bodadelisedrei.png")

print("QR creado con éxito 💖🎄")
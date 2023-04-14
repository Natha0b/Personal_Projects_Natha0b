import pyqrcode

# Crear una instancia del QR code
qr = pyqrcode.create("¡Hola, mundo!")

# Guardar el QR code en un archivo PNG
qr.png("qr_code.png", scale=8)


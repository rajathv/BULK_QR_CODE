# Import QR Code library
import qrcode
import csv

with open('gdg.csv', 'r') as f:
  reader = csv.reader(f)
  your_list = list(reader)
print(your_list)

  # Create qr code instance
for i in your_list:
	qr = qrcode.QRCode(
		version = 1,
		error_correction = qrcode.constants.ERROR_CORRECT_H,
		box_size = 10,
		border = 4,
	)
	name=i[0]
	branch=i[1]
	code=i[2]
	str=" Name:"+name+" Branch:"+branch+" ID:"+code
	# The data that you want to store
	data = str

	# Add data
	qr.add_data(data)
	qr.make(fit=True)

	# Create an image from the QR Code instance
	img = qr.make_image()
	fname=i[0]+".png"
	# Save it somewhere, change the extension as needed:
	img.save(fname)

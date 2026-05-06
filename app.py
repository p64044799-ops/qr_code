if st.button("Generate QR"):
if data:
# All these lines must be aligned perfectly
qr = qrcode.make(data)
qr.save("qr.png")
img = Image.open("qr.png")
with open("qr.png", "rb") as f:
st.download_button("Download QR", f, file_name="qr.png")
else:
st.warning("Please enter some text")



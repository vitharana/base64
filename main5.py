#not working sometimes paste the code in the commandline to get the image



import base64
import webbrowser

# Get base64-encoded data from the user
encoded_data_input = input("Paste the base64-encoded data here and press Enter:\n")

# Add padding if missing
padding = '=' * (4 - (len(encoded_data_input) % 4) % 4)
encoded_data_input += padding

# Decode the base64-encoded data
try:
    decoded_data = base64.b64decode(encoded_data_input)
except Exception as e:
    print("Error decoding base64 data:", e)
    exit(1)

# Save the decoded data to an image file
with open("image_decoded.jpg", "wb") as f:
    f.write(decoded_data)

# Open the image file in the default web browser
webbrowser.open("image_decoded.jpg")

#run the code to decode a text file with base64 encoding to see the picture


import base64

with open("encoded.txt","rb") as f:
    encoded_data = f.read()
    
    print(encoded_data)
    decoded_data = base64.b64decode(encoded_data)

    with open ("image_decoded.jpg","wb") as g:
        g.write(decoded_data)


import webbrowser

webbrowser.open("image_decoded.jpg")

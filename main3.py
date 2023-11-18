
#run the code to encode the image to a txt file

import base64

with open("pic.jpg","rb") as f:
    data = f.read()

    #print(data)

    encoded_data = base64.b64encode(data)
    print(encoded_data)

    with open("encoded.txt","wb") as g:
        g.write(encoded_data)











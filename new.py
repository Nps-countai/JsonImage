import base64
with open("image.jpg", "rb") as img_file:
    my_string = base64.b64encode(img_file.read())
print(my_string)



encoded_data = my_string
decoded_data=base64.b64decode((encoded_data))

#write the decoded data back to original format in  file
img_file = open('qqqqq.jpg', 'wb')

img_file.write(decoded_data)
img_file.close()
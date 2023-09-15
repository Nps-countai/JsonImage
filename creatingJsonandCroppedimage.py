import json
import base64
from PIL import Image 

import os
 
# Get the list of all images
path = "/home/santhosh/NPS/JsonImage/Pimages"
img_list = os.listdir(path)

# reading parent json
with open('sample.json')as file:
    data = json.load(file)

for image in img_list:
        
    # image = img_list[0]
    name = image[:-4]
    print(image, name)

    # converting image into base64
    with open(('/home/santhosh/NPS/JsonImage/Pimages/%s'%(image)), "rb") as img_file:
        my_string = base64.b64encode(img_file.read())
        my_string = my_string.decode()
        
        
    with open(('/home/santhosh/NPS/JsonImage/output/json/%s.json')%(name),'w+')as f:
        # print('---------------------------------------------before----------------------------------------------------------------------------------------')
        # print(data['imageData'])
        data['imageData'] = my_string 
        # print('---------------------------------------------after----------------------------------------------------------------------------------------')
        # print(data['imageData'])
        json.dump(data,f, indent=2)

        # getting image data
        # p = data['flags']['points'] -> ctual 
        x1,y1 = [120,48]
        x2,y2 = [900,650]

    # print(data['imageData'])
    img_data = data['imageData']
    # print(type(img_data))

    encoded_data = img_data

    # 64 to image
    #decode base64 string data
    decoded_data=base64.b64decode((encoded_data))

    #write the decoded data back to original format in  file
    img_file = open(('/home/santhosh/NPS/JsonImage/output/croppedImage/%s.jpg'%(name)), 'wb')
    img_file.write(decoded_data)
    img_file.close()



    img = Image.open('/home/santhosh/NPS/JsonImage/output/croppedImage/%s.jpg'%(name)) 
    img_res = img.crop((x1 , y1, x2, y2)) 


    # img_res.show() 
    img_res.save(('/home/santhosh/NPS/JsonImage/output/croppedImage/%s.jpg'%(name)))


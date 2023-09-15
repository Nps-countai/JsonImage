import json
import os

json_list = os.listdir('/home/santhosh/NPS/JsonImage/output/croppedImage/labelMe')
# jn = json_list[0]

for jn in json_list: 
    print(jn)
    with open('/home/santhosh/NPS/JsonImage/output/croppedImage/labelMe/%s'%(jn)) as lmfile:
        lm_data = json.load(lmfile)
    lmfile.close()
        
    with open('/home/santhosh/NPS/JsonImage/output/json/%s'%(jn)) as jsnfile:
        jsn_data = json.load(jsnfile)
    jsnfile.close()
        
    lm = lm_data['shapes'][0]['points']
    jsn = jsn_data['shapes'][0]['points']
    jsn_data['shapes'][0]['points'] = lm

    print(jsn_data['shapes'][0]['points'])

    with open('/home/santhosh/NPS/JsonImage/output/json/%s'%(jn),'w+') as jsnfile:
        json.dump(jsn_data,jsnfile, indent=2 )
    jsnfile.close()
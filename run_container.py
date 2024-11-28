import requests

url = "http://localhost:5025/SEGMENT"
# use the path from the "perspective of the conatiner"
data = {"input_path": "/app/images/Well96_CH2_00.tiff"}
response = requests.post(url, json=data)

if response.status_code == 200:
    print('Image processed successfully:', response.json())
else:
    print('Error:', response.json())

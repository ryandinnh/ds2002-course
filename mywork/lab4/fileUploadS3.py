#!/usr/bin/python3

import boto3
import requests

#start s3 client
s3 = boto3.client('s3', region_name='us-east-1')

#prompt user to get bucket name
BUCKET = input("What is the name of your desired bucket (without the s3:// protocol)? : ")

#get file from internet using urllib or requests 
#https://realpython.com/python-requests/#other-http-methods
#function to download file
def download_file(url, file_path):
    #use requests library to get the json detail 
    response = requests.get(url)

    #check if the request was successful (code 200 means succesful)
    if response.status_code == 200:
        with open(file_path, 'wb') as file: #'wb' mode is 'w' = write 'b' binary. Needed the 'b' because the files being uploaded are not text
            file.write(response.content)
    else:
        print(f"Failed to download file: status code {response.status_code}")

#prompt user for file url
URL = input("What is the url of the file you want uploaded to your bucket?: " )
        
#prompt user for what to name the file
FILE = input("What do you want to name the file? (ex. vuelta.jpg): " )

download_file(URL, FILE)

#upload file to s3 bucket
resp = s3.put_object(
    Body = FILE,
    Bucket = BUCKET,
    Key = FILE
)

#presign url:
response = s3.generate_presigned_url(
    'get_object',
    Params={'Bucket': BUCKET, 'Key': FILE},
    ExpiresIn=604800
    )

#output presigned url:
print(f"The presigned url for your uploaded file is: {response}")
#example output: The presigned url for your uploaded file is: https://ds2002-rqd3qmk.s3.amazonaws.com/carti.gif?AWSAccessKeyId=AKIAW3MD7KABQJRXTQMF&Signature=SCYLjHl0XBHqbepfPd8QaYKYdbQ%3D&Expires=1711029330



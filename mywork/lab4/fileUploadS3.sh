#!/bin/bash

#clear the screen
clear

#promt user for the bucket
read -p "Please enter the name of the bucket without the s3:// protocol: " BUCKET

#prompt user for file url
read -p "Please enter the url of the file you want to upload to the s3 bucket: " URL

#promt user for the name of the file
read -p "Please enter the name of the file: " NAME

#retrieve the file
curl $URL > $NAME

#upload file to s3 bucket
aws s3 cp $NAME s3://$BUCKET

#presign the file
aws s3 presign --expires-in 604800 s3://$BUCKET/$NAME

#When executing during testing this is the presigned url:
#https://ds2002-rqd3qmk.s3.us-east-1.amazonaws.com/black_chrome.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAW3MD7KABQJRXTQMF%2F20240314%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240314T015841Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=06440d9433d57fa2af08655de6ac0bbf5117c6dba1ed2873b99be33f7beee341
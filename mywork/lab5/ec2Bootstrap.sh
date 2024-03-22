#!/bin/bash

#OS updates from step 1
/usr/bin/apt update -y
/usr/bin/apt upgrade -y

#choosing to install these three to the ec2 instance: python3, git, and nginx
/usr/bin/apt install -y python3
/usr/bin/apt install -y git
/usr/bin/apt install -y nginx #note to test nginx in the instance had to use sudo in the instance shell
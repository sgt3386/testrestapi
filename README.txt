# steps to setup the extrahop rest api for passwd
# NOTE: ran on ubuntu 18.04 (windows subsystem), python 3.6 and pip3 (9.0.1)

##install flask
pip3 install flask-restful
pip3 install request

#needed for postman on ubuntu 18
sudo apt-get install libgtk2.0-0
sudo apt-get install gconf-service libxext6 libxfixes3 libxi6 libxrandr2 libxrender1 libcairo2 libcups2 libdbus-1-3 libexpat1 libfontconfig1 libgcc1 libgconf-2-4 libgdk-pixbuf2.0-0 libglib2.0-0 libgtk-3-0 libnspr4 libpango-1.0-0 libpangocairo-1.0-0 libstdc++6 libx11-6 libx11-xcb1 libxcb1 libxcomposite1 libxcursor1 libxdamage1 libxss1 libxtst6 libappindicator1 libnss3 libasound2 libatk1.0-0 libc6 ca-certificates fonts-liberation lsb-release xdg-utils wget

##install postman on ubuntu, unpack, and create symbolic link
wget https://dl.pstmn.io/download/latest/linux64 -O postman.tar.gz
sudo tar -xzf postman.tar.gz -C /opt
sudo ln -s /opt/Postman/Postman /usr/bin/postman

### Instructions on running the application ###

-To run python application, navigate to the directory where rest-app.py exists. Then run using 'python3 rest-app.py', else errors will occur.

URL: http://127.0.0.1:5000/

-To list users
	GET - /passwd/list_users

-To update passwd file
	PUT - /passwd/add_users/[user:pass:uid:gid:user_info:home_path:startup_script]
	
EXAMPLES:
	curl -X GET http://127.0.0.1:5000/passwd/list_users
	curl -X PUT http://127.0.0.1:5000/passwd/add_users/testuser:x:sample_UID:sample_GID:sample_info:sample:sample
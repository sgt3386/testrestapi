#!/usr/bin/env python3
from flask import Flask
from flask import request
import time

app = Flask(__name__)
passwd_path = "./assets/passwd"

def info_on_file():
    # build array from file, return delimited list
    # user:pass:uid:gid:user_info:home_path:startup_script
    user_data = []
    lines = [line.rstrip('\n') for line in open(passwd_path)]
    for x in range(len(lines)):
        user_data.append(lines[x].split(':'))
    return(user_data)

def append_user_in_file(newuser):
    # user:pass:uid:gid:user_info:home_path:startup_script
    _string = info_on_file()
    test_string = newuser.split(':')
    if test_string[0] not in str(_string):
        try:
            with open(passwd_path, "a+") as passwdfile:
                passwdfile.write(str(newuser) + "\n")
                passwdfile.close()
            return("passwd file updated successfully", 200)
        except:
            return("unable to update passwd file", 404)
    else:
        return("User exists", 200)

@app.route('/', methods=['GET'])
def hello_world():
    return('Hello, World!')

@app.route('/passwd/list_users', methods=['GET'])
def getUsers():
    user_list = []
    passwd_data = info_on_file()
    for items in range(len(passwd_data)):
        user_list.append(passwd_data[items][0])
    if user_list: # if list is populated, return 200
        return(str(user_list)), 200
    return "Users not found", 404

@app.route('/passwd/add_users/<string:newuser>', methods=['PUT'])
def putOne(newuser):
    #_status = append_user_in_file(newuser)
    _status = append_user_in_file(newuser)
    return(_status)

# info_on_file()
# _string = append_user_in_file("test")
# print(_string)


if __name__ == "__main__":
    app.run(debug=True)

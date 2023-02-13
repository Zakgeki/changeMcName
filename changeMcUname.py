# Copyright © 2023 Zachary Wells
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the “Software”), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import sys
import os
from mojang import API, Client

def main():
    # The new Minecraft username you want to use
    usernames = [ "list", "of", "usernames" ]
    email = ask_for_email()
    password = ask_for_password()
    # using mojangs api, check if the username is availablejjj
    api = API()

    # loop indefinitely
    while 1:
        # iterate over the list of names
        for name in usernames:
            # check if name is available. If so, change the account name
            if not api.get_uuids([name]):
                change_account_name(email, password, name)
                os._exit(0)


def change_account_name(email, password, new_username):
    client = Client(email, password)
    
    # if the clients name can be changed, change the name. Else, ask for new
    # account information and try again. 
    if client.get_name_change_info():
        data = client.change_username(new_username)
        if not data["success"]:
            print(data["error"])
        elif data["success"]:
            print(f"Username successfully changed from {current_username} to {new_username}!")
    else:
        print("This account can't have it's name changed. Provide a new account.")
        email = ask_for_email()
        password = ask_for_password()
        change_account_name(email, password, new_username)

# asks for email, will loop until a non-empty string is given
def ask_for_email():
    email = input("email: ")
    if not email:
        print("No email given.")
        email = ask_for_email()
    return email

def ask_for_password():
    password = input("password: ")
    if not password:
        print("No password given.")
        password = ask_for_password()
    return password

if __name__ == "__main__":
    main()

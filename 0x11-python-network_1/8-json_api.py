#!/usr/bin/python3
"""
A Python script that takes in a letter
and sends a POST request to
http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        arg = ""
        print("No result")
    else:
        arg = sys.argv[1]
        data = {"q": arg}
        req = requests.post('http://0.0.0.0:5000/search_user', data)

        try:
            json_data = req.json()
            if json_data == {}:
                print("No result")
            else:
                print("[{}] {}".format(
                    json_data.get("id"), json_data.get("name")))
        except ValueError:
            print("Not a valid JSON")

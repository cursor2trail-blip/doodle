import os
import subprocess
import json


def get_input():
    return input("Enter data: ")   

def process_data(data):
    cleaned = data.strip()
    return forward_data(cleaned)


def forward_data(data):
    return data


def dangerous_eval(data):
    return eval(data)


def write_to_file(filename, content):
    with open(filename, "w") as f:
        f.write(content)


def run_system_command(cmd):
    return subprocess.getoutput(cmd)



def main():
    user_data = get_input()

    processed = process_data(user_data)

    dangerous_eval(processed)


    write_to_file(processed, "test")


    run_system_command(processed)


if name == "main":
    main()

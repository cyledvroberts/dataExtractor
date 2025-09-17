"""
Cyle Roberts
CS 485 Project 1
Dependencies:
regex library
This program extracts email address and phone numbers from
disk images or memory images that are in raw/dd format.
The program takes in 2 Command line arguments using the argparse library. 
A -phonenumber flag and a -email flag.
The program writes the list of phone numbers to a phonenumber.txt file and the
emails to an emails.txt file in the same directory as the program.
For example you can call the program with the command line input 
'python .\\dataExtractor -phonenumbers'.
This program writes to standard out the size of the lists for the total emails,
unique emails, total phone numbers, and unique phone numbers.
This program reads the input file 2 lines at a time to handle cases where a phone
number or email address is broken up by a new line character.
"""

#!/usr/bin/python3
import regex
import argparse


def add_unique(item, unique_list):
    if item not in unique_list:
        unique_list.append(item)


r_email = regex.compile(
    rb'([a-z0-9A-Z._]+@[a-z0-9A-Z._]+\.(com|org|edu|gov|uk|net|'
    rb'ca|de|jp|fr|au|us|ru|ch|it|nl|se|no|mil|biz|io|cc|co|info))'
)

r_phone = regex.compile(
    rb'(\(\d{3}\)[-. ]{1}\d{3}[-. ]{1}\d{4})|(\d{3}[-. ]{1}\d{3}[-. ]{1}\d{4})'
)

parser = argparse.ArgumentParser(description="Extract emails and phone numbers.")
parser.add_argument(
    '-email', action='store_true',
    help="Flag to process and extract emails"
)
parser.add_argument(
    '-phonenumber', action='store_true',
    help="Flag to process and extract phone numbers"
)
args = parser.parse_args()

total_emails = []
unique_emails = []
total_phones = []
unique_phones = []

with open('usb256.001', mode='rb', buffering=65536) as dd:
    line1 = dd.readline()
    while line1:
        line2 = dd.readline()
        combined_lines = line1.strip() + b" " + line2.strip()

        if args.email:
            matches = r_email.findall(combined_lines)
            for m in matches:
                email = str(m[0], 'utf-8')
                total_emails.append(email)
                add_unique(email, unique_emails)

        if args.phonenumber:
            matches = r_phone.findall(combined_lines)
            for m in matches:
                phone = m[0] if m[0] else m[1]
                phone = str(phone, 'utf-8')
                total_phones.append(phone)
                add_unique(phone, unique_phones)

        line1 = dd.readline()

if args.email:
    with open('emails.txt', 'w') as email_file:
        for email in total_emails:
            email_file.write(f"{email}\n")
    print(f"Total emails: {len(total_emails)}")
    print(f"Unique emails: {len(unique_emails)}")

if args.phonenumber:
    with open('phones.txt', 'w') as phone_file:
        for phone in total_phones:
            phone_file.write(f"{phone}\n")
    print(f"Total phone numbers: {len(total_phones)}")
    print(f"Unique phone numbers: {len(unique_phones)}")
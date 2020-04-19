A poorly documented Python script to generate all valid phone numbers in one big vcf for a given area code.
Each contact is given a random name thanks to Faker (https://faker.readthedocs.io/en/master/)

Requirements
- Faker

Usage
$ python3 contacts.py <area code>

In my testing, a single area code's phone numbers takes up about a gigabyte of space. 

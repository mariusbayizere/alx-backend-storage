0x01-NoSQL
This project contains scripts and Python programs to interact with MongoDB on Ubuntu 18.04 LTS.

Requirements
General
MongoDB version 4.2 is required.
Python scripts must be written for Python 3.7 and use the PyMongo library version 3.10.
All files should end with a new line.
The first line of all files should be a comment (e.g., // my comment for MongoDB scripts, #!/usr/bin/env python3 for Python scripts).
All files must adhere to the pycodestyle style (version 2.5.*).
The length of all files will be tested using wc.
All Python modules should have documentation (e.g., python3 -c 'print(__import__("my_module").__doc__)').
All Python functions should have documentation (e.g., python3 -c 'print(__import__("my_module").my_function.__doc__)').
Python scripts should not execute when imported (use if __name__ == "__main__":).
Install MongoDB 4.2 on Ubuntu 18.04
To install MongoDB 4.2, follow these commands:

bash
Copy code
wget -qO - https://www.mongodb.org/static/pgp/server-4.2.asc | apt-key add -
echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.2 multiverse" > /etc/apt/sources.list.d/mongodb-org-4.2.list
sudo apt-get update
sudo apt-get install -y mongodb-org
sudo service mongod status
Install PyMongo
To install PyMongo, run the following:

bash
Copy code
pip3 install pymongo
Tasks
0. List all databases
Write a script that lists all databases in MongoDB.

File: 0-list_databases

1. Create a database
Write a script that creates or uses the database my_db.

File: 1-use_or_create_database

2. Insert document
Write a script that inserts a document in the collection school with the attribute name set to "Holberton school".

File: 2-insert

3. All documents
Write a script that lists all documents in the collection school.

File: 3-all

4. All matches
Write a script that lists all documents with name="Holberton school" in the collection school.

File: 4-match

5. Count
Write a script that displays the number of documents in the collection school.

File: 5-count

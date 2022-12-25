# 6156_Project_Contacts
## Introduction
This is the group project of the 6156 Cloud Computing course by Professor Donald Ferguson @ Columbia University

Our interested scenario is online shopping, and this repo represents the "Contacts" microservice, which includes a "Contacts" database for customers and a flask
application that retrieves related data. The "contacts" database include 4 tables, and these 4 tables represent 4 difference wayts to look for customers, including
phone (phoneNo, accountId), email (emailAddress, accountId), address(Id, accountId, street, aptNo, city, state, zip), and payment(cardNo, accountId, cvc,
expiration date, holderFirst, holderLast, cardType, and billingAddressId).

## How to use this repo
###### 1: Generate Data
Use the "generateCSV_contacts.py" as a template to generate some fake data for testing purpose. My code just generates csv files in the same directory. The number of 
files to be generated depends on the database design. In "Contacts", there are 4 tables, which means 4 csv. Do not worry about data type, like whether treat
the phone number to be a big integer or a string. SQL will take care of it.

###### 2. Create Local Database & Table
Use the "Contacts DB Setup.ipynb" as a template to read in csv data and create database and tables. Make sure the correct datatypes are used when running "create 
table..." sql in this notebook. 

###### 3. Flask 
Use the "ContactFlask" folder as a template to build simple applicaiton to get table data. 

I use the environment variable setup, so need to edit configuration to add 3 environment variables (DBUSER, DBPW, DBHOST) before running

pip install -r requirements.txt, to install required packages 

The basic url format is:   (url)/api/(your interested database)/(your interested table)/(accountId), accountId is the customer account id. 


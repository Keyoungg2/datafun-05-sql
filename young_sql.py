"""
   This project is to demonstrate the usage of SQL and Python together. We will use Python and SQLite together to excute sql queries that will involve creating and mangaging databases.
   We will be using different CRUD operations ( Select, Update, etc), joins, and other aggreations to for analysis and creation purposes. 
   
  Code Writer: Kareem Young
  creation date: 02/05/2024
"""

#Imported Standard Libraries 
import sqlite3
import pyarrow 
import csv
import uuid
import pathlib

#Imported External libraries
import pandas as pd 
import logging

#imported local projects
import Key_2_Analytics_utils as utils 

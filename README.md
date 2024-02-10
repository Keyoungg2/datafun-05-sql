# Datafun-05-sql
In this project, we will be working with Python and SQLite to grasp a statistical inference on some data files. 

Coder: Kareem
Project: Library_operations_Python_SQL
Date:02/09/2024

## Setting Project File up
First, we will create a virtual environment and install any exteranl libraires through the terminal. Make sure to create the .gitignore file and report that .venv and .vscode contents are not pushed to your GitHub repo.
```shell
py -m venv .venv
.venv\Scripts\activate
py -m pip install pandas pyarrow
py -m pip freeze > requirements.txt
ni .gitignore
```
# Add folders
Make sure to create the following in Vscode or file explore:
1. Add requirements.txt
2. Add .gitignore file
3. Add Data Folder
 
    -Create Authors.csv

    -Create Books.csv 

    -Create Libraries.csv
    
 4.Add Sql Folder
 
   -Place all sql scripts here
     
 5. young_library_operations_sql.py
   
6. Log.txt 


At any time you want to commit to the project, simply do the following:
```shell
git add.
git commit -m "commit message"
git push
```
# CSV & SQL dataset
The csv dataset book and authors are provided and libraries was created by myself. All sql scripts & tables are written by me to explore this dataset and develope different analysis. Be aware that Bookmanager.py and Demoproject.DB are used for looking and creation of authors and books table. Young_library_operations_sql.py is the python script to recreate books & authors tables. As well additional create the libraries table  to place books with locations. 

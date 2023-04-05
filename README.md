# AirBnB_clone
<img src="hbnb.png" width=100%>

## Description

'0x00. AirBnB clone - The console' group project.

# First step: Write a command interpreter to manage your AirBnB objects.

The first step towards building our first full web application: the AirBnB clone:
	- HTML/CSS templating, database storage, API, front-end integration…

Each tasks are linked and will help to:

- put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances
- create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
- create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
- create the first abstracted storage engine of the project: File storage.
- create all unittests to validate all our classes and storage engine

## Table of Contents
 * [Description](#Description)
 * [Usage](#Usage)
 * [File Description](#File-Description)
 * [Bugs](#Bugs)
 * [Authors](#Authors)
 * [Licences](#Licences)

## Usage
To use this application:
 - Clone this repo 
 - cd into it and make console.py executable ``cd AirBnB_clone; chmod u+x console.py``
 - Check below commands for more help

| Command | Description |
| --- | --- |
| `./console.py` | Opens the `(hbnb)` interpreter |
|  `all` | Prints all string representation of all instances |
| `create` | Creates a new instance of BaseModel |
| `destroy` | Deletes an instance based on the class name and id |
| `show` | Prints the string representation of an instance |
| `update` | Updates an instance based on the class name and id |
| `quit` | QUIT command that exits the program |

### Example usage
Launching console.py, checking available commands, and creating a User
```
$ ./console.py 
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb) create User
11dff8b8-f77f-4eb0-8535-42553d6155e8
(hbnb)
```
## File description

| File | Description |
| :--- | :--- |
| `console.py` | Creates the command line intepreter |
| `models/base_model.py` | Contains a class defining attributes and methods for other classes |
| `models/engine/file_storage.py` | Contains the class for JSON serialization and deserialization |
| `tests/` | All test files to test files, classes, functions with unit tests |

# Second step: MySQL storage
'0x02. AirBnB clone - MySQL'
- replace the file storage by a Database storage
- map your models to a table in database by using an O.R.M.

# Third step: It’s time to make the work public!

- Deploying web_static work. Used Fabric (for Python3).
- Fabric is a Python library and command-line tool for streamlining the use of SSH for application deployment or systems administration tasks.


##  Bugs
- No known bugs

## Authors

| AUTHOR | EMAIL | LINKEDIN |
| :---: | :---: | :---: |
| `Mahlet Seifu` | akotet2123@gmail.com | [@Mahlet Seifu](https://www.linkedin.com/in/mahlet-seifu-1a715a142) |
|  | @gmail.com | [](link) |

## License
No special licenses needed


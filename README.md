# AirBnB Clone

This project is a simple web application similar to AirBnB. It is complete web app which at the end would comprise:

	i. A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging)
	ii. A website (the front-end) that shows the final product to everybody: static and dynamic
	iii. A database or files that store data (data = objects)
	iv. An API that provides a communication interface between the front-end and your data (retrieve, create, delete, update them)

## Project Workflow

A breakdown of the worflow of the project.

### 1. Console
	i. Create data model
	ii. Manage (create, update, destroy, etc) objects via console/command interpreter
	iii. Store and persist objects to a file(JSON file)

### 2. Web static
	i. Create HTML of application
	ii. Create template of each object
	
### 3. MySQL storage
	i. Replace file storage with database storage
	ii. Map models to a table in database using an O.R.M

### 4. Web framework - templating
	i. Create web server in Python
	ii. Make static HTML file dynamic by using objects stored in a file or database

### 5. RESTful API
	i. Expose all objects stored via a JSON web interface
	ii. Manipulate objects via a RESTful API

### 6. Web dynamic
	i. Load objects from client side by using own RESTful API

## Console (Command Interpreter)
The console is a command line interface to create, modify and delete objects in the file storage.

### How to start Console
To run the console in interactive mode, run the console.py by itself
'''
$ ./console.py
'''

### How to use Console
The following are commands that work in the console and their functions:

| Command | Function |
| ------- | -------- |
| create  | create a new instance of a class |
| show    | show the info of an instance of a class |
| destroy | destroy an instance of a class |
| update  | update the info of the objects in an instance |
| all     | show all instances |
| quit    | exit the console |
| help    | show the help of the commands |

### Example Usage
#### create
**Usage:** $ create '<class name>'
'''
$ ./console.py
(hbnb) create BaseModel
49faff9a-6318-451f-87b6-910505c55907
'''

#### show
**Usage:** $ show '<class name>' '<id>'
'''
$ ./console.py
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'first_name': 'Betty', 'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}
'''

#### destroy
**Usage:** $ destroy '<class name>' '<id>'
'''
$ ./console.py
(hbnb) destroy BaseModel 49faff9a-6318-451f-87b6-910505c55907
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
** no instance found **
'''

####  update
**Usage:** $ update '<class name>' '<id>' '<attribute name>' '<attribute value>'
'''
$ ./console.py
(hbnb) update BaseModel 49faff9a-6318-451f-87b6-910505c55907 first_name "Betty"
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'first_name': 'Betty', 'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}
'''

#### all
**Usage:** $ all '<class name>' or $ all
'''
$ ./console.py
(hbnb) all BaseModel
'''

#### quit
**Usage:** $ quit
$ ./console.py
(hbnb) quit
'''

#### help
**Usage:** $ help
'''
$ ./console.py
(hbnb) help
(hbnb) help quit
Quit command to exit the program
'''

## Running the tests

## Authors

* David Ajimati
* Francis Kwafe 

# AirBnB_clone
**Part 1 :  AirBnB_clone 
0x00. AirBnB CLONE - The console**
As aspiring Software Engineers at ALX Software Engineering Programme, we are required to create an AirBnB Clone. The planning of the AirBnB clone has already been done by the ALX Team and students are only expected to replicate it by following a set of instructions. 
The first step to developing this web application is to create a Command Line Interpreter (CLI) to help us manage the Air BnB project’s objects. Creating the Command Line Interpreter is very important because it will pave the way for building and including static and dynamic contents: HTML/CSS/JS templates, DB storage, File Storage, API (Application Programming Interface) and Front-End Integration.


**What is a Command Line Interpreter (CLI)?
**A CLI is a text-based User-Interface (UI) that runs commands and programmes it by managing computer files and interacting with the computer. we  are expected to be able to manage the objects of the project by:
Creating a new object (ex: a new User or a new Place)
Retrieving an object from a file, a database etc…
Doing operations on objects (count, compute stats, etc…)
Updating attributes of an object and 
Destroying an object
Learning Objectives
During and after completion  of this project, we will be able to do the following:
Know how to create a Python package
Know how to create a CLI in Python using the cmd module
Know what is Unit testing and how to implement it in a large project
Know how to serialize and deserialize a Class
Know how to write and read a JSON file
Know how to manage datetime
Know what is an UUID
Know what is *args and how to use it
Know what is **kwargs and how to use it
Know how to handle named arguments in a function
Requirements
The requirements of this project include:
Python Scripts
Allowed editors: vi, vim, emacs
All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
All your files should end with a new line
The first line of all your files should be exactly #!/usr/bin/python3
A README.md file, at the root of the folder of the project, is mandatory
Your code should use the pycodestyle (version 2.8.*)
All your files must be executable
The length of your files will be tested using wc
All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
Python Unit Tests
Allowed editors: vi, vim, emacs
All your files should end with a new line
All your test files should be inside a folder ./tests
You have to use the unittest module
All your test files should be python files (extension: .py)
All your test files and folders should start by test_
Your file organization in the tests folder should be the same as your project
e.g., For models/base_model.py, unit tests must be in: tests/test_models/test_base_model.py
e.g., For models/user.py, unit tests must be in: tests/test_models/test_user.py
All your tests should be executed by using this command: python3 -m unittest discover tests
You can also test file by file by using this command: python3 -m unittest tests/test_models/test_base_model.py
All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
Program Build-up
We are to build the AirBnB Clone web application phase by phase using the SDLC (Software Development Life Cycle)
Problem Definition / Plan
Solution Requirements and Analysis
Solution Design using algorithms, flowcharts, and pseudocodes
Implementation using a choice Programming Language
Solution Testing
Deployment
Maintenance
Note: The problem definition, requirements are already done for us. We only need to design a clone of the original using our own design, implement our code with our choice programming language which in this project is Python Programming Language and test our implementations using Python's unittest module.
**Classes Needed in this Project**
The classes needed in this project include:
Public Instance Attributes
Public Instance Methods
Public Class Attributes
Private Class Attributes


How The Program is Executed
The  shell is expected towork like this in interactive mode
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
But also in non-interactive mode: (like the Shell project in C)
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
AirBnB Clone Console Usage
How to Start The Console
The AirBnB Clone console can be run both interactively and non-interactively.
Running in the Non-Interactive Mode
$ echo "help" | python3 console.py
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb)
$
or
$ echo "help" | ./console.py
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb)
$
Alternatively, it can be run in interactive mode, run the file console.py by itself:
Running in the Interactive Mode
$ ./console.py
(hbnb)

or
$ python3 console.py
(hbnb)

In this README or guide, we will be making most of the documentation with the interactive mode.
When you execute the above command, it displays a prompt (hbnb). This is the prompt required of the project and it awaits inputs from the user.
Quiting the Console
To quit the console, you can type in any of the following:
EOF
quit
or do the following key combinations on your keyboard
CMD+D (Unix) / CRTL+C (Windows)
(hbnb) quit
$

or
(hbnb) EOF
$

or
(hbnb) (CTRL+C)
$

Getting Help
To get help generally
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb)
To get help for a particular command
(hbnb) help all

The `all` command displays the string representation of all class instances present in the storage.

Usage:
(hbnb) all User
(hbnb) help update

The `update` command update a specified instance of a using the class name and the ID of the instance, and and the specifying the attribute to update or adding a new attribute plus the value.

Usage:
(hbnb) update User 1234-5678 email 'test@oop.com'

(hbnb)
Presently, we have nothing in the flat file database, We will create a New User and a BaseModel
(hbnb) all
[]
(hbnb)

Firstly, we have to get help on how to create an instance of a model and what models are available
$ ./console.py
(hbnb) help create

The `create` command creates an instance of a class, saves it to the storage and prints out the ID of the instance created.

Models available includes:

        Amenity
        BaseModel
        City
        Place
        Review
        State
        User

Usage:
(hbnb) create User

(hbnb)
To create a New User model, we type create User and it returns the ID of the User model created
(hbnb) create User
97bf8455-58aa-4d65-a83e-32699de58bbb
(hbnb)
To display the details of the User model that was created,
(hbnb) show User 97bf8455-58aa-4d65-a83e-32699de58bbb
[User] (97bf8455-58aa-4d65-a83e-32699de58bbb) {'id': '97bf8455-58aa-4d65-a83e-32699de58bbb', 'created_at': datetime.datetime(2023, 5, 13, 13, 16, 37, 181187), 'updated_at': datetime.datetime(2023, 5, 13, 13, 16, 37, 181187)}
(hbnb)
To update the details of the User model created, we can specify a new attribute and supply a value for the new attribute or specify an existing attribute and give a new value to replace the previous value.
(hbnb) update User 97bf8455-58aa-4d65-a83e-32699de58bbb nationality "Nigerian"
(hbnb)

(hbnb) show User 97bf8455-58aa-4d65-a83e-32699de58bbb
[User] (97bf8455-58aa-4d65-a83e-32699de58bbb) {'id': '97bf8455-58aa-4d65-a83e-32699de58bbb', 'created_at': datetime.datetime(2023, 5, 13, 13, 16, 37, 181187), 'updated_at': datetime.datetime(2023, 5, 13, 13, 21, 11, 714225), 'nationality': 'Nigerian'}
(hbnb)

(hbnb) update User 97bf8455-58aa-4d65-a83e-32699de58bbb email "test.user@email.com"
(hbnb) show User 97bf8455-58aa-4d65-a83e-32699de58bbb
[User] (97bf8455-58aa-4d65-a83e-32699de58bbb) {'id': '97bf8455-58aa-4d65-a83e-32699de58bbb', 'created_at': datetime.datetime(2023, 5, 13, 13, 16, 37, 181187), 'updated_at': datetime.datetime(2023, 5, 13, 13, 24, 24, 386540), 'nationality': 'Nigerian', 'email': 'test.user@email.com'}
(hbnb)
To remove a model from the flat file database,
(hbnb) destroy User 97bf8455-58aa-4d65-a83e-32699de58bbb
(hbnb) all
[]
(hbnb) all User
[]
(hbnb) show User 97bf8455-58aa-4d65-a83e-32699de58bbb
** no instance found **
(hbnb)

The program is interactive and the documentation from the help file is leading enough.

**Authors
**Thomas Kitaba <thomas.kitaba@gmail.com>,
Hauwa Abdulkadir <ahauwa48@yahoo.com>





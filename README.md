# Shopping-List
[![Build Status](https://travis-ci.org/kisakyegordon/my-shopping-list.svg?branch=master)](https://travis-ci.org/kisakyegordon/my-shopping-list)

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/f59a23defd59496cbd1d46c8d55cc031)](https://www.codacy.com/app/kisakyegordon/my-shopping-list?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=kisakyegordon/my-shopping-list&amp;utm_campaign=Badge_Grade)

[![Coverage Status](https://coveralls.io/repos/github/kisakyegordon/my-shopping-list/badge.svg)](https://coveralls.io/github/kisakyegordon/my-shopping-list)


The shopping list is an application that allows users to record and share things they want to spend money on, hence meeting the needs of keeping track of their shopping lists.


## Functions
 The application has a couple of features as listed below:-

* Register
* Log In
* Create Shopping list
* Add shopping list items
* Edit Items
* Delete Items

 ## Setup
 To start using this application, first clone it to your local machine by running
 
 ```
 git clone https://github.com/kisakyegordon/my-shopping-list
 
 ```
 
  Create the virtual environment and activate it
 
 ```
 virtualenv env
 source env/bin/activate
```
Then install all the required dependencies

```
pip install -r requirements.txt
```

Then run the application

```
python run.py
```

To now view the application head over to
```
http://localhost:5000
```
 
### Testing
You can then run the application tests using
```
cd my-shopping-list
nosetests tests/tests.py
```


# Neighbourhood
# By Joan Nanjala, Maratah Njoroge and Suzie Akinyi.

Live site: View Site 

# Description
This project allows users to post their neigbourhoods for other users to join, a user can also leave neighbourhood according to design, usability, creativity and content.

# User Story
As a user I would like to:

* Sign in with the application to start using.
* Set up a profile about me and a general location and my neighborhood name.
* Find a list of different businesses in my neighborhood.
* Find Contact Information for the health department and Police authorities near my neighborhood.
* Create Posts that will be visible to everyone in my neighborhood.
* Change My neighborhood when I decide to move out.
* Only view details of a single neighborhood.

# Setup and Installation
To get the project :

* Clone the repository:
* https://github.com/kangalah/Neighbourhood
Install and activate Virtual
- python3 -m venv virtual - source virtual/bin/activate  
Navigate into the folder and install requirements with the command:
- pip install -r requirements.txt 

# Setup Database
SetUp your database User,Password, Host then make migrations:

- python manage.py makemigrations hood 
Then Migrate:

-python manage.py migrate 

# Run the application
python manage.py runserver 

# Testing the application
* python manage.py test 
* Open the application on your browser 127.0.0.1:8000.

# Api Endpoints


# Known Bugs


# Contact Information
* If you have any question or contributions, please email us at hood@gmail.com

## License
*MIT* Copyright (c) 2020 

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
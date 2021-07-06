# playboard
A Django application that creates a photo gallery for a user basedd on the pictures they uploaded and they can also be able to share the images by copying them to clipboard.

## author
 https://github.com/ThiraTheNerd

##  Live Link  
 Click [View Site]()  to visit the site
  
## Screenshots 
###### Home page
 
<img src="https://user-images.githubusercontent.com/51013354/124569663-d0649480-de4e-11eb-8259-f8ecf27c649a.png">
 
 ###### Search results
 <img src="https://user-images.githubusercontent.com/51013354/124570736-d5761380-de4f-11eb-8d87-571a2e9cc559.png"> 

 ###### Image Details 
 <img src="https://user-images.githubusercontent.com/51013354/124570584-b4152780-de4f-11eb-947d-8345df108ba1.png">

## User Story  
  
* View different photos that interest them  
* Click a single image to expand it and view the details of that photo  
* Search for different categories   
* Copy a link to the photo to share with my friends.  
* View photos based on the location they were taken.

## Setup and Installation  
To get the project .......  
  
##### Cloning the repository:  
 ```bash 
 https://github.com/ThiraTheNerd/playboard.git 
```
##### Navigate into the folder and install requirements  
 ```bash 
cd Playboard pip install -r requirements.txt 
```
##### Install and activate Virtual  
 ```bash 
- python3 -m venv virtual - source virtual/bin/activate  
```  
##### Install Dependencies  
 ```bash 
 pip install -r requirements.txt 
```  
 ##### Setup Database  
  SetUp your database User,Password, Host then make migrate  
 ```bash 
python manage.py makemigrations posts 
 ``` 
 Now Migrate  
 ```bash 
 python manage.py migrate 
```
##### Run the application  
 ```bash 
 python manage.py runserver 
``` 
##### Testing the application  
 ```bash 
 python manage.py test 
```
Open the application on your browser `127.0.0.1:8000`.  
  
  
## Technology used  
  
* [Python3.6](https://www.python.org/)  
* [Django 1.11](https://docs.djangoproject.com/en/2.2/)  
* [Heroku](https://heroku.com)  
  
  
## Known Bugs  
* The locations tab does not filter the pictures based on their location 
  
## Contact Information   
If you have any question or contributions, please email me at [thiragithinji@gmail.com]  
  
## License 

* [![License](https://img.shields.io/packagist/l/loopline-systems/closeio-api-wrapper.svg)](https://github.com/ThiraTheNerd/playboard/blob/master/LICENSE  
* Copyright (c) 2021 **ThiraTheNerd**

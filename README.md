# Fitness Forum Overview
A fitness oriented forum created using Python and Django framework

# Purpose:
This application was primarily built in order to gain experience making small projects using Python and to mentor new Python developers on Python web development. 

### Dependencies:
* Python 3.9.x
* Django 3.1.x 

### Platform:
This program was developed on Windows but can also run on Unix like operating systems such as Linux and Mac OSX. 

# Development Usage: 
1. Clone repo
2. open project folder in IDE of your choice 
3. Create and activate a virtual environment by running the following commands: 
```
pip install virtualenv
virtualenv dev_env 
.\dev_env\Scripts\activate # for Windows users 
source dev_env/bin/activate # for Linux and Mac users 
```
3. set the following environment variables:
```
export YOUR_GMAIL_ADDRESS=<enter_your_gmail_address>
export YOUR_GMAIL_PASSWORD=<enter_your_gmail_password>
export DJANGO_SETTINGS_MODULE=fitness_forum.settings
```
4. install all dependencies by running: ```pip install -r requirements.txt```
5. run ```python manage.py migrate``` 
6. run ```python manage.py runserver```

# Screenshots: 
Main page:
![Main page](/static/images/screenshot_1.png)

Thread view page:
![Thread view page](/static/images/screenshot_2.png)

Post view page:
![Post view page](/static/images/screenshot_3.png)

Replies for post:
![Reply post image](/static/images/screenshot_4.png)

### Testing:
All unit tests for this project can be found in the ```/tests``` folder

### Contributing:
Please feel free to contribute to this project however possible by forking this repo, making changes and initiating pull requests. Thanks!

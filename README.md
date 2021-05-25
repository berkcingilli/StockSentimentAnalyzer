# Stock Sentiment Analyzer


## Guidelines to run this application

### 1. python 3.8.3 must be installed in your system. Install it if you do not have
### 2. open cmd and execute *pip install venv*. Since this project has all dependencies inside virtual enviroment.
### 3. for Windows execute *./venv/Scripts/activate*. for Linux execute *source venv/bin/activate* (Note : You have locate the correct directory usin *cd /yourfileexists*)
### 4. Since virtual environment is activated now you have install all dependencies in order for this project to run. Which is inside requirements.txt file. Execute *pip install -r requirements.txt* to install into virtual environent otherwise applicaiton wont work without all dependencies like django etc.
## All of the process above had to be done because the dependencies exceeded over 300 MB which file submission had 50 MB limit on QMplus.
### 5. Now you can run the django application using this command *python manage.py runserver*. (Note check if you are in correct directory where manage.py file exists).
### 6. Now you must once login to admin panel by going to this url *localhost:8000/admin*.
### 7. Enter credentials ID:berk      password:123
### 8. Now you can use the application by going this url *localhost:8000*


## Additioal notes
### *localhost:8000/get_sentiment* url will gather all comments from Yahoo Finance & Stockstwits. It will take approx 30 min. However this is not advised since you will have to wait till it finishes and there is already more than a month fo data existing to use the application.
### *localhost:8000/test_endpoint* url is used for testing purposes. This is not advised to entered as well since it serves as test endpoint.
### If you are on linux you can set a periodic task to gather sentiment. To do this settings.py CRONJOBS = [ ... ] uncomment, INSTALLED APPS django-crontab uncomment and cron.py uncomment and it is been set to everyday 19.30 it will gather sentiment. Then run *python manage.py crontab add*. Then again run the server but computer must be left open all the time so this is not advised again. You can use above url to gather sentiment and wait only for 30 min if needed.

![Chart1.PNG](https://github.com/[berkcingilli]/[StockSentimentAnalyzer]/image.png?raw=true)

##Githublink: https://github.com/berkcingilli/StockSentimentAnalyzer

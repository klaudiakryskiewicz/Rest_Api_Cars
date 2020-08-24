# Rest_Api_Cars
Recruitment Task for Netguru
Rest Api collecting data from https://vpic.nhtsa.dot.gov/api/ based on car make and model name, 
allowing to rate cars and sort them by number of rates.

## Endpoints:
POST /cars
* Request body should contain car make and model name
* Based on this data, its existence should be checked here https://vpic.nhtsa.dot.gov/api/
* If the car doesn't exist - return an error
* If the car exists - it should be saved in the database

POST /rate
* Add a rate for a car from 1 to 5

GET /cars
* Should fetch list of all cars already present in application database with their current average rate

GET /popular
* Should return top cars already present in the database ranking based on number of rates (not average rate values, it's important!)

## Requirements and setup
Application build in Django & Django Rest Framework, using PostgreSQL database and Docker Compose.

To start app, run the following commands:
* "docker-compose build"
* "docker-compose run web python manage.py migrate"
* "docker-compose up"

To stop, use ctr + c.

To start test, run
* "docker-compose run web python manage.py test"

## Demo

App deployed on heroku:
https://kkryskiewicz-cars.herokuapp.com/cars/
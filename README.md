# Rest_Api_Cars
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
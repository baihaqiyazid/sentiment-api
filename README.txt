# Sentiment API

============= How to run? =====================

Install Library:
    1. python3 -m pip install flask
    2. python3 -m pip install numpy
    3. python3 -m pip install flask-restx
    4. python3 -m pip install python-dotenv
    5. python3 -m pip install flask-sqlalchemy

Run App:
    1. python3 -m flask run --host=0.0.0.0 --port=5000

============= How to use this program? ========

Using Postman:

    1. route on http://localhost:5000/api/v1/predict
    2. in the Body, select type raw -> JSON
    3. just fill the parameter, ex: 
        {
        "sentence": "agnezmo pintar dan cantik sekali tetapi lintah darat :)"
        }


Using Curl:

    Just type in cmd or command line in your os like this,

    ```
    curl -X POST -H 'Content-Type: application/json' -i 'http://localhost:5000/api/v1/predict' --data '{"sentence":"agnezmo pintar dan cantik sekali tetapi lintah darat :)"}'
    ```

    note: the sentence can change 

============= API Documentation ================
you can access it on http://localhost:5000/

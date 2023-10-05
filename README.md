# Sentiment API

## Clone this repo

<b>Using http</b>
```
git clone https://github.com/baihaqiyazid/sentiment-api.git
```

<b>Using ssh</b>
```
git clone git@github.com:baihaqiyazid/sentiment-api.git
```

## How to run?

<b>Install Library</b>
1. python3 -m pip install flask
2. python3 -m pip install numpy
3. python3 -m pip install flask-restx
4. python3 -m pip install python-dotenv
5. python3 -m pip install flask-sqlalchemy

<b>Run App</b>
1. python3 -m flask run --host=0.0.0.0 --port=5000

## How to use this program?

<b>Using Postman</b>

1. route on http://localhost:5000/api/v1/predict
2. in the Body, select type raw -> JSON
3. just fill the parameter, ex: 
```
{
  "sentence": "agnezmo pintar dan cantik sekali tetapi lintah darat :)"
}
```

<b>Using Curl</b>

Just type in cmd or command line in your os like this,
```
curl -X POST -H 'Content-Type: application/json' -i 'http://localhost:5000/api/v1/predict' --data '{"sentence":"agnezmo pintar dan cantik sekali tetapi lintah darat :)"}'
```
note: the sentence can change 

## API Documentation
you can access this documentation in http://localhost:5000/ on your browser
![image](https://github.com/baihaqiyazid/sentiment-api/assets/89854394/db2ea3f7-1885-40c7-a30b-ccfd9013ad55)

## Result

### Success (200)
![image](https://github.com/baihaqiyazid/sentiment-api/assets/89854394/66346ccc-c0e1-4e8f-8c19-3c02c4e115b2)

### Bad Request (None text / "")
#### 1. Contoh, ""
![image](https://github.com/baihaqiyazid/sentiment-api/assets/89854394/091e6a5c-169d-4605-9504-9344da00e5e5)
#### 2. Contoh, null
![image](https://github.com/baihaqiyazid/sentiment-api/assets/89854394/292507ce-3e99-4307-9e19-36972e41dea4)

### Not Found (jika mengakses route yang tidak ada)
#### 1. Contoh mengakses route /coba_akses
![image](https://github.com/baihaqiyazid/sentiment-api/assets/89854394/34dc4b74-6265-45cd-ad73-3174ea244674)
#### 2. Contoh mengakses route /dashboard
![image](https://github.com/baihaqiyazid/sentiment-api/assets/89854394/60be91eb-2628-40fd-a461-44cefe67e8d3)
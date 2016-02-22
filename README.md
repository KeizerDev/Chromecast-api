# Chromecast-api
Just a chromecast rest api to make the implementation easier for other programs. 


## Build
```
$ pip install -r requirements.txt
$ ./main.py # localhost:5000
```

## Endpoints
```
GET /devices
```
Shows an array of the available chromecasts(`chromecast_name`) in a local network.   
  
  
  
```
GET /devices/:chromecast_name
```
Shows info about the chromecast and if it is reachable. If not it throws a `404`.    
  
   
  
```
GET /devices/:chromecast_name/media/:url  
```
Starts playing the given URIdecoded `url` on `chromecast_name`.

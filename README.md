# sre-logging
Simple Stats for log files using python and Docker


### Development
```
$ git clone https://github.com/natelxon/sre-logging.git
$ pip install -r requirements.txt
$ LOG_FILE=./logs/access_log_20190520-125058.log python3 app/app.py
```

### Build application
Build the Docker image manually by cloning the Git repo.
```
$ git clone https://github.com/natelxon/sre-logging.git
$ docker build -t natelxon/sre-logging .
```

### Run the container
Create a container from the image with a docker volume where logs are located.
```
$ docker run --name sre-logging -d -v $PWD/logs:/logs -e LOG_FILE=logs/access_log_20190520-125058.log -p 8080:8080 natelxon/sre-logging
```

Visit http://localhost:8080/stats
```
{
    "countByIp":{"1.101.53.96":1,"1.109.146.23":1,"1.110.180.78":1},
    "httpCodeDistribution":{"200":9003,"301":373,"404":424,"500":200},
    "logFile":"logs/access_log_20190520-125058.log",
    "topReferers":{"http://www.garcia.com/":4,"https://johnson.com/":5,"https://smith.com/":4,"https://www.johnson.com/":5,"https://www.williams.com/":4},
    "totalRequests":10000,
    "uniqueIps":9884
}
```

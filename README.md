# sre-logging
Simple Stats for log files using python and Docker


### Build application
Build the Docker image manually by cloning the Git repo.
```
$ git clone https://github.com/natelxon/sre-logging.git
$ docker build -t natelxon/sre-logging .
```

### Run the container
Create a container from the image.
```
$ docker run --name sre-logging -d -p 8080:8080 natelxon/sre-logging
```

Visit http://localhost:8080/stats
```
 {

 }
```

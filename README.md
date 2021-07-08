# ModelServingBarrettNibling

Builds Docker image which will make a POST request for predictions for a model.


## Example:
First, build the docker image:

`docker build -t docker-example .`

Then run the image to make a container (include ./3/ or any other saved model):

`docker run -p 5000:5000 docker-example:latest ./3/`

Test with request_test.py:

`python request_test.py`

And open browser to `http://localhost:5000`
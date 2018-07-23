# flask-restful-wsgi - SERVERLESS
Sample flask_restful app with Apache mod_wsgi configs. Well, serverless makes all the apache config and wsgi moot, so ignore the repo title for this branch and let AWS deal with all the provisioning.

## Purpose
This repo illustrates a simplified approach for deploying a flask_restful (Python Flask) app on AWS API GW and Lambda. This just deploys the API portion of the api (/spam-api).

## Pre-reqs and Config?
Not really, assume you have an AWS account and just do this:
* `cd spam-api`
* `virtualenv spam-api-env`
* `source spam-api-env/bin/activate` (make sure your virtualenv is running python3)
* `pip install flask flask_restful zappa`
* `zappa init` (can take all the defaults)

## Deploy
* `zappa deploy`

The deploy will do a number of things, ultimately uploading a lambda function and then deploying an AWS API Gateway to trigger that lambda. So, at the very end it will return a url like: [https://f3nowuh5sj.execute-api.us-east-1.amazonaws.com/dev](https://f3nowuh5sj.execute-api.us-east-1.amazonaws.com/dev). You can just add /api/egg to the end to hit the endpoint, like [https://f3nowuh5sj.execute-api.us-east-1.amazonaws.com/dev/api/egg](https://f3nowuh5sj.execute-api.us-east-1.amazonaws.com/dev/api/egg).

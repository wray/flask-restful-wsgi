# flask-restful-wsgi - SERVERLESS
Sample flask_restful app with Apache mod_wsgi configs. Well, serverless makes all the apache config and wsgi moot, so ignore the repo title for this branch and let AWS deal with all the provisioning.

## Purpose
This repo illustrates a simplified approach for deploying a flask_restful (Python Flask) app on AWS API GW and Lambda. This just deploys the API portion of the api (/spam-api).

## Pre-reqs and Config?
Not really, assume you have an AWS account and just do this:
* `cd spam-api`
* `virtualenv spam-api-env`
* `source spam-api-env/bin/activate`
* `pip install flask flask_restful zappa`
* `zappa init`

## Deploy
* `zappa deploy {env}`

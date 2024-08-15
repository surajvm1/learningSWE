## Project Overview

- End goal (rough):
![project architecture overview](https://github.com/surajvm1/learningSWE/blob/dev/feat1/imgs_for_readme_reference/e2eDevProj.drawio.png)

- Note: Project done in past to understand docker services: https://github.com/surajvm1/LearningMicroservices
To increase complexity of project may add: integrate with ML model, write services in java/go and not just python, add more features to app and make some better usecase

----------------------------------------

(Rough set up updates in project - will clean up readme later)

Download nodejs
 2426  cd webFrontend
 2429  npx create-react-app webapp (all small case)
 2430  cd webapp
 2437  node -v
 2431  npm start

cleanup unnecessary files

 npm install axios

npm install react-router-dom

coding routes and basic code

python service
 2482  cd microservices
 2483  ls
 2484  python3 -m venv microServiceB
 2485  cd microServiceB
 2486  source bin/activate
 2487  pip freeze

pip install fastapi requests "uvicorn[standard]" SQLAlchemy==1.4.46 psycopg2-binary pydantic pandas redis

# to run fastapi service: podman build --no-cache -t internal_weather_service_b_image . 
# podman run -p 8900:8900 --name internalWeatherServiceBCon internal_weather_service_b_image

# to run the compose file: podman-compose up --build

nodemon install: sudo npm install -g --force nodemon
but note its for nodejs proejcts not react projects... 



brew install nginx       
brew services start nginx
it runs in 8080 port
cd /opt/homebrew/etc/nginx

making changes in the config file
here in project added config file just for reference how it looks like
paralelly setup kong gatewaymicroservice

307 is a type of temporary redirect. This HTTP response status code means that the URL someone is requesting has temporarily moved to a different URI (User Resource Identifier), but will eventually be back in its original location.












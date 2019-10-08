Starbook:

Please make shure external port 8080 not bound yet (or replace it by unused port at the docker-compose file) and nginx server is ready to accept http(not https) requests

Secret key stored in /starbook/starbook.env, feel free to change it.

Database credentials stored at postgres/user.env, feel free to change it too.

NOTE: authentication via frontend not developed because of lack of time (need to learn some frontend libraries and tools).
Frontend side can be used for result representation only.

Make it run:

    docker-compose build 
    docker-compose up
___
Starbot: 

Please, dont forget to change url in config.json file

    {
      "urls": {
        "base_url": "http://www.yourdomain.com:8080",
        ...
    }

Make it run:

    python3 -m venv env
    source env/bin/activate
    pip install -r requirements.txt
    python bot.py
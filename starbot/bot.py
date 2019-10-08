import requests
import random
import names
import json
from pwgen import pwgen
import sys

with open('config.json') as config_file:
    CONF = json.load(config_file)

def request(**kwargs):
    def decorator(func):
        def wrapper(*f_args, **f_kwargs):
            url = CONF['urls']['base_url'] + kwargs['url']
            method = kwargs['method']
            response = getattr(requests, method)(url, **func(*f_args, **f_kwargs))
            print(response.status_code, response.content)
            try:
                return json.loads(response.content), response.status_code
            except json.decoder.JSONDecodeError:
                print('Something gone wrong')
                sys.exit()
        return wrapper
    return decorator


class User:

    def __init__(self):
        self.liked_posts = set()
        self.likes_made = 0
        self.tokens = {}
        self.username = names.get_first_name(gender=random.choice(['male', 'female']))
        self.password = pwgen(12)


class Starbook:

    @staticmethod
    @request(method='post', url=CONF['urls']['api_auth'])
    def signup(user):
        return {'json': {'username': user.username, 'password': user.password}}

    @staticmethod
    @request(method='post', url=CONF['urls']['get_token'])
    def get_tokens(user):
        return {'json': {'username': user.username, 'password': user.password}}

    @staticmethod
    @request(method='post', url=CONF['urls']['api_posts'])
    def create_post(user, post_body):
        return {
            'headers': {'Authorization': 'Bearer %s' % user.tokens['access']},
            'json': {
                'body': post_body
            }
        }

    @staticmethod
    @request(method='post', url=CONF['urls']['api_likes'])
    def like_post(user, post_id):
        return {
            'headers': {'Authorization': 'Bearer %s' % user.tokens['access']},
            'json': {
                'id': post_id
            }
        }


class Controller:

    users = []
    all_posts = set()

    def __init__(self):
        self.__dict__.update(CONF)

    @property
    def __random_message(self):
        return random.choice(self.defined_messages)

    def create_users(self):
        while len(self.users) < self.number_of_users:
            self.users += [User() for u in range(self.number_of_users - len(self.users))]

            for user in self.users:
                if user.tokens:
                    continue
                user_credentials, status = Starbook.signup(user)

                if status == 201:
                    tokens, status = Starbook.get_tokens(user)
                    user.tokens.update(tokens)
                else:
                    self.users.remove(user)

    def create_posts(self):
        for user in self.users:

            messages = [self.__random_message for m in range(random.randint(1, self.max_posts_per_user))]
            for mess in messages:
                post, status = Starbook.create_post(user, mess)
                if status == 201:
                    self.all_posts.add(post['id'])

    def like_posts(self):
        for user in self.users:
            while user.likes_made < self.max_likes_per_user and user.liked_posts != self.all_posts:
                post = random.choice(list(self.all_posts.difference(user.liked_posts)))
                Starbook.like_post(user, post)
                user.liked_posts.add(post)
                user.likes_made += 1


if __name__ == '__main__':
    bot = Controller()
    bot.create_users()
    bot.create_posts()
    bot.like_posts()

import json

import redis

from adapters import ActionAdapter
from generators import UserGenerator, ActionGenerator

redis_host = "localhost"
redis_port = 6379
redis_password = ""

table_name = "log"


def write_actions(redis_session, table_name, actions):
    count = 1
    for action in actions:
        redis_session.hset(table_name, count, json.dumps(ActionAdapter.to_json(action)))
        count += 1


def read_actions(redis_session, table_name):
    rows = redis_session.hgetall(table_name)
    actions = list()

    for key, value in rows.items():
        action = ActionAdapter.from_json(json.loads(value))
        actions.append(action)

    return actions


def sort_actions(actions, limit=None):
    top = dict()

    for action in actions:
        key = action.user().id()

        if top.get(key) is None:
            top[key] = 1
        else:
            top[key] += 1

    sorted_users = sorted(top.items(), key=lambda row: row[1], reverse=True)

    limit_users = sorted_users[0: limit if limit is not None else sorted_users.__len__()]

    top_users = list()

    def find(user_id):
        for action in actions:
            user_from_action = action.user()
            if user_from_action.id() == user_id:
                return user_from_action
        return None

    for limit_user in limit_users:
        top_users.append(find(limit_user[0]))

    return top_users


redis_session = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password)

users = UserGenerator().generate_users(100)
actions = ActionGenerator.generate_actions(users, 1000)

write_actions(redis_session, table_name, actions)

parse_actions = read_actions(redis_session, table_name)

top_users = sort_actions(parse_actions, limit=10)

for top_user in top_users:
    print(top_user.__str__())
    print()

print(top_users)

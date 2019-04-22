from datetime import datetime
import random

from models import User, Action


class UserGenerator(object):
    __names = ["name1", "name2", "name3", "name4", "name5"]
    __last_names = ["lastName1", "lastName2", "lastName3", "lastName4", "lastName5"]
    __educations = ["education1", "education2", "education3", "education4", "education5"]

    def generate_users(self, count):
        users = list()

        random_value = lambda iterable_list: iterable_list[random.randint(0, iterable_list.__len__() - 1)]

        for i in range(0, count):
            name = random_value(self.__names)
            last_name = random_value(self.__last_names)
            education = random_value(self.__educations)
            age = random.randint(0, 100)

            users.append(User(id=i, name=name, last_name=last_name, education=education, age=age))

        return users


class ActionGenerator:
    @staticmethod
    def generate_actions(users, count):
        actions = list()
        user_count = users.__len__() - 1

        for i in range(0, count):
            actions.append(Action(i, datetime.now(), users[random.randint(0, user_count)]))

        return actions

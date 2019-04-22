class User (object):
    __id = None
    __name = None
    __last_name = None
    __age = None
    __education = str()

    def __init__(self, id=None, name=None, last_name=None, age=None, education=None):
        print('Test')
        self.__id = id
        self.__name = name
        self.__last_name = last_name
        self.__age = age
        self.__education = education


    def id(self):
        return self.__id

    def name(self):
        return self.__name

    def last_name(self):
        return self.__last_name

    def education(self):
        return self.__education

    def age(self):
        return self.__age

    def __str__(self):
        return 'id = {0}, name = {1}, last_name = {2}, age = {3}, education = {4}'.format(self.__id, self.__name,
                                                                                          self.__last_name, self.__age,
                                                                                          self.__education)
w = User()
w = User(1)
w = User(1, 2)
w = User(1, 2, 3)
w = User(1, 2, 3, 4)
w = User(1, 2, 3, 4, 5)
class Action:
    __user = None
    __timestamp = None

    def __init__(self, timestamp, user):
        self.__user = user
        self.__timestamp = timestamp

    def timestamp(self):
        return self.__timestamp

    def user(self):
        return self.__user

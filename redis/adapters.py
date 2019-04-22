from models import User, Action


class UserAdapter:
    @staticmethod
    def to_json(user):
        return {
            "id": user.id(),
            "name": user.name(),
            "last_name": user.last_name(),
            "education": user.education(),
            "age": user.age()
        }

    @staticmethod
    def from_json(dict):
        id = dict["id"]
        name = dict["name"]
        last_name = dict["last_name"]
        education = dict["education"]
        age = dict["age"]

        return User(id=id, name=name, last_name=last_name, education=education, age=age)


class ActionAdapter:
    @staticmethod
    def to_json(action):
        return {
            "timestamp": action.timestamp().__str__(),
            "user": UserAdapter.to_json(action.user())
        }

    @staticmethod
    def from_json(dict):
        timestamp = dict["timestamp"]
        user = UserAdapter.from_json(dict["user"])

        return Action(timestamp, user)

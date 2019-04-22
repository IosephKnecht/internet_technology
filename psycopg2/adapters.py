class UserAdapter:
    @staticmethod
    def convert_to_sql_params():
        return '({0}, {1}, {2}, {3}, {4})'.format('id', 'name', 'last_name', 'education', 'age')

    @staticmethod
    def convert_to_sql_values(user):
        return '({0}, \'{1}\',\'{2}\', \'{3}\', {4})'.format(user.id(), user.name(), user.last_name(), user.education(),
                                                             user.age())


class ActionAdapter:
    @staticmethod
    def convert_to_sql_params():
        return '({0}, {1}, {2})'.format('id', 'user_id', 'action_time')

    @staticmethod
    def convert_to_sql_values(action):
        return '({0}, {1},\'{2}\')'.format(action.id(), action.user().id(), action.timestamp())

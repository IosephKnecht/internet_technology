from adapters import UserAdapter, ActionAdapter
from db_api import DbManager
from generators import UserGenerator, ActionGenerator

db_name = 'user_database'
user = 'django_user'
password = '123456789'

db_manager = DbManager(db_name=db_name, user=user, password=password)
db_manager.connect()

user_generator = UserGenerator()

users = user_generator.generate_users(100)
actions = ActionGenerator.generate_actions(users, 1000)

# db_manager.insert_values(table_name='user', model_list=users, column_hook=UserAdapter.convert_to_sql_params,
#                          values_hook=UserAdapter.convert_to_sql_values)
#
# db_manager.insert_values(table_name='log', model_list=actions, column_hook=ActionAdapter.convert_to_sql_params,
#                          values_hook=ActionAdapter.convert_to_sql_values)

top_users = db_manager.execute_custom("""SELECT "user".id,
                                            "user".name,
                                            "user".last_name,
                                            "user".education,
                                            "user".age, 
                                            count("user".id) as action_count 
                                            from "log" inner join "user" on "log".user_id = "user".id 
                                            group by 1,2,3,4,5
                                            order by action_count DESC
                                            LIMIT 10""")

for user in top_users:
    user_str = ''
    for param in user:
        user_str += str(param).strip() + ' '
    print(user_str)


db_manager.disconnect()

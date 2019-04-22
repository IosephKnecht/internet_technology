import psycopg2


class DbManager:
    __db_name = None
    __user = None
    __password = None

    __connection = None
    __cursor = None

    def __init__(self, db_name, user, password):
        self.__db_name = db_name
        self.__user = user
        self.__password = password

    def connect(self):
        if self.__cursor is not None:
            self.__cursor.close()
            self.__cursor = None

        self.__connection = psycopg2.connect(dbname=self.__db_name, user=self.__user, password=self.__password)
        self.__cursor = self.__connection.cursor()

    def disconnect(self):
        self.__connection.close()
        self.__cursor.close()

    def insert_values(self, table_name, model_list, column_hook, values_hook):
        models_count = model_list.__len__()
        model_values = ''

        for i in range(0, models_count):
            model_values += values_hook(model_list[i])
            if i < models_count - 1:
                model_values += ','

        self.__insert(table_name, column_hook(), model_values)

    def execute_custom(self, query):
        self.__cursor.execute(query)
        return self.__cursor.fetchall()

    def __insert(self, table_name, str_columns, str_params):
        self.__cursor.execute("""INSERT INTO "{0}" {1} VALUES {2}""".format(table_name, str_columns, str_params))
        self.__connection.commit()

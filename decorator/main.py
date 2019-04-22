import inspect
from datetime import datetime


def decorator_function(wrapped_function):
    def execute(*args, **kwargs):
        start_time = datetime.now()

        def obtain_args_params(wrapped_function, args):
            args_info = list()

            arg_names = inspect.getfullargspec(wrapped_function).args
            right = min(args.__len__(), arg_names.__len__())

            for i in range(right):
                args_info.append('Param №{0}, Name = {1}, Value = {2}'.format(i, arg_names[i], args[i]))

            return args_info

        def obtain_params_info(kwargs):
            args_info = list()
            count = 1

            for arg_name, arg_value in kwargs.items():
                args_info.append('Param №{0}, Name = {1}, Value = {2}'.format(count, arg_name, arg_value))
                count = count + 1

            return args_info

        args_info = obtain_params_info(kwargs) if (kwargs.__len__() > 0) else obtain_args_params(wrapped_function, args)
        returned_value = wrapped_function(**kwargs) if kwargs.__len__() > 0 else wrapped_function(*args)

        for info in args_info:
            print(info)

        print('Wrapped function return = {0}'.format(returned_value))
        print('Time difference = {0}'.format(datetime.now() - start_time))

    return execute


@decorator_function
def decorated_function(param1, param2, param3, param4, param5):
    return 'Hello world'


decorated_function('lol', 'kek', 'mem', 'top', 'fun')

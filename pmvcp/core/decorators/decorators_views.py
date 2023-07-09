""" Decorators for View file for Py MVC Prompt Package """
# __doc__ (Decorators for View file for Py MVC Prompt Package)

import functools


def decorate_intro(num_lines: int) -> str:
    """
    Decorator for intro banner and exit banner
    Repeats lines before and after of each intro or exit message (str)
    """

    def decorator_decorate_intro(func: str):

        @functools.wraps(func)
        def wrapped_decorate_intro(self) -> list:
            line = '-'*49+' \n'
            message = ''
            counter_start = counter_end = 1
            while counter_start <= num_lines:
                message += line
                counter_start += 1

            message += func(self)

            while counter_end <= num_lines:
                message += line
                counter_end += 1

            return message
        return wrapped_decorate_intro
    return decorator_decorate_intro

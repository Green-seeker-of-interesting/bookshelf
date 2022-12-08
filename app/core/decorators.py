import os


def sending_files_decorator(func):
    def wrapper(*args, **kwargs):
        if not os.path.exists("temporary_files"):
            os.mkdir("temporary_files")
        return func(*args, **kwargs)
    wrapper.__name__ = func.__name__ 
    return wrapper
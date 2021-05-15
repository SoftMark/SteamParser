def careful(f):
    def wrapper(cls, arg):
        try: return f(cls, arg)
        except: return None
    return wrapper
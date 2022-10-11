
def intdiv (a,b):
    try:
        return a//b
    except ZeroDivisionError:
        print('please dont divide by zero..')
    except TypeError:
        print('Check operands.. Some of then seems strange..')
    except Exception:
        print('Ups, something went wrong...')
intdiv(90,0)

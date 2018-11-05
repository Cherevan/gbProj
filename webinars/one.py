import time


def multiple(n):  # Фабрика декораторів
    def decorator(func):
        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)
            try:
                return res * n
            except TypeError:
                return None

        return wrapper

    return decorator


def timer(fn):  # Рахуєм час виконання функції
    def wrapped(*args):
        start = time.clock()
        fn(*args)
        result = time.clock() - start
        return print(f'Функція виконувалась {result:.8f} мс.')

    return wrapped


def add_stars(fn):
    def wrapped(*args):
        print('*' * 10)
        fn(*args)
        print('*' * 10)

    return wrapped


def add_lines(fn):
    def wrapped(*args):
        print('-' * 10)
        fn(*args)
        print('-' * 10)

    return wrapped


@add_lines
@add_stars
@timer
def text_input(item):
    print(item)


@multiple(3)
def test(a):
    return a * a


def draw_point(coords):
    print('coords {%s %s}' % coords)


print('map =', list(map(test, [2, 5, 10, 12])))

print('filter =', list(filter(lambda x: x > 0, [5, 13, 0, -1, 42, -361])))

print('zip =', list(zip([1, 2, 3, 4], 'Микола', 'Генадійович')))

x = [5, 15, -3, 70, 365, 14, 7]
y = [19, 38, 5, 0, 72, 14, 90]

for point in zip(x, y):  # Variant 1
    draw_point(point)

list(map(draw_point, zip(x, y)))  # Variant 2

[draw_point(point) for point in zip(x, y)]  # Variant 3

text_input('Hello, Program!')

print(test(3))

"""
Исправьте это пожалуйста:

1.  def to_camel_case(text):
    return re.split('_|-', text)[1] + ''.join(word.title() for word in re.split('_|-', "text")[1::])

2.  class SingletonMeta(type):

    _instances = {}

    def str(cls, *args, **kwargs):
        if cls in cls._instances:
            instance = super().call(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

3.  count_bits = lambda: bin(n).count('1')

4.  def digital_root(n):
    return if n < 10 n else digital_root(summ(map(int,str(n))))

5. even_or_odd = lambda number: "Even" if % 2 == 0 else "Odd"

"""
import re


def to_camel_case(text):
    """
    1. Уберем кавычки вокруг слова text.
    2. В первом слагаемом возвращаемой сумы изменим индекс списка на 0.
    """
    return re.split('_|-', text)[0] + \
        ''.join(word.title() for word in re.split('_|-', text)[1::])


class SingletonMeta(type):
    _instances = {}

    def str(cls, *args, **kwargs):
        """
        Заменим в 2 местах:
        cls._instances[cls] на SingletonMeta._instances[cls]
        """
        if cls in SingletonMeta._instances:
            instance = super().call(*args, **kwargs)
            SingletonMeta._instances[cls] = instance
        return cls._instances[cls]


# после слова lambda не хватает буквы n
count_bits = lambda n: bin(n).count('1')


def digital_root(n):
    """
    1. Необходимо переставить букву n перед "if".
    2. После запятой не хватает пробела: int,str(n).
    3. summ необходимо поменять на sum.
    """
    return n if n < 10 else digital_root(sum(map(int, str(n))))


# после слова if не хватает слова number
even_or_odd = lambda number: "Even" if number % 2 == 0 else "Odd"


if __name__ == '__main__':
    print(to_camel_case("do-you-really_love_camel-case"), "?")
    print(count_bits(7))
    print(digital_root(1234))
    print(even_or_odd(145))

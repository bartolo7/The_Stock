import functools
import math

decimals = ['', ' Thousand', ' Million', ' Billion', ' Trillion']


def calculate_avg_list_of_numbers(numbers=None):
    the_average = functools.reduce(lambda x, y: x + y, numbers) / len(numbers)
    return round(the_average, 2)


def generate_readable_number_with_decimal_description(number):
    number = float(number)
    value = max(0, min(len(decimals) - 1, int(math.floor(0 if number == 0 else math.log10(abs(number)) / 3))))
    return '{:.0f}{}'.format(number / 10 ** (3 * value), decimals[value])


from celery import shared_task
import time
from celery.exceptions import SoftTimeLimitExceeded

@shared_task
def plus(a,b):
    return a+b

@shared_task
def minus(a,b):
    return a-b

@shared_task
def oper1(a,b):
    return a + b

@shared_task
def oper2(a,b):
    return a * b

@shared_task
def oper3(a,b):
    return a / b

@shared_task
def sum_oper(res):
    return sum(res)

@shared_task(soft_time_limit=10,time_limit = 15)
def get_data(a, b):
    try:
        time.sleep(12)
        result = a + b
        print(f"Результат: {result}")
        return result
    except SoftTimeLimitExceeded:
        print("Задача занадто довго виконується, перервана soft time limit")
        return 'task was too long'
    
@shared_task
def hello_one():
    return 'Hello Roma'

@shared_task
def hello_two():
    return 'Hello Yulian'

@shared_task
def hello_tree():
    return 'Hello Vasil'

@shared_task
def hello_four():
    return 'Hello Gleb'

@shared_task
def hello_five():
    return 'Hello Oleg'


'''@shared_task(rate_limit = '5/m')
def check():
    return 'JavaScript'''

@shared_task
def data_check(i):
    print(f'Початок задачі N{i}')
    time.sleep(5)
    print(f'Завершення задачі N{i}')


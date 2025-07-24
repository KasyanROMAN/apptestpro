from django.db.models.signals import pre_save,post_save,pre_delete,post_delete
from django.dispatch import receiver
from .models import Person


@receiver(pre_save,sender = Person)
def before_created(sender,instance,**kwargs):
    if instance.name == 'Sasha':
        instance.name = instance.name.upper()

    else:
        print('Міняти імя ми можемо тільки Sasha')   



@receiver(post_save,sender = Person) # sender - сигналізуватись робота над Person
def notify_create(sender,instance,created,**kwargs):  # instance - екземпляр ( abc )
    if created:                               # created - метод , що ти дійсно створюєш шось 
        print(f'Ви створили людину {instance.name}') # **kwargs - невизначена к-ть параметрів
    
    else:
        print('Ви НЕ створили людину')


@receiver(pre_delete,sender = Person)
def before_delete_person(sender,instance,**kwargs):
    print(f'Ви хочете видалити людину {instance.name}')


@receiver(post_delete,sender = Person)
def delete_person(sender,instance,**kwargs):
    print('Ви видалили людину')

from django.db import models
from .validators import * 

# Create your models here.

class CheckPeople(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(age__gt = 18)
    '''def check_full_age(self,age):
        return self.get_queryset().filter(age__gt = age)
    
    def first_person(self):
        return self.get_queryset().first()'''
    


class Person(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    hobby = models.TextField()
    number = models.IntegerField(default=0)

    people = CheckPeople()


    def __str__(self):
        return f'{self.name}-{self.age}-{self.hobby}'
    
    
    #people = CheckPeople()

class Car(models.Model):
    TYPE_CAR = [
        ('mechanics','механіка'),
        ('automatics','автоматика')
    ]
    name = models.CharField(max_length=20,help_text='Імя машини')
    price = models.DecimalField(blank=True,max_digits=6,decimal_places=5)
    is_active = models.BooleanField(default=True)
    image = models.ImageField(upload_to='photo/')
    owner = models.TextField(unique=True,db_index=True)
    description = models.TextField(verbose_name='Опис', null=True)
    updated = models.DateField(auto_now_add=True)
    published = models.DateTimeField(auto_now=True)
    type_car = models.CharField(max_length=30,choices=TYPE_CAR,default='automatics')
    
    class Meta:
        ordering = ['price']
        db_table = 'db_Cars'
        verbose_name = 'Машина'
        verbose_name_plural = 'Машини'

    def __str__(self):
        return self.name 
    
class Man(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    def __str__(self):
        return self.name

class Business(models.Model):
    business_name = models.CharField(max_length=30)
    man = models.ForeignKey(Man,on_delete=models.CASCADE)
    def __str__(self):
        return self.business_name
    
# відношення один до одного 

class Profile(models.Model):
    name = models.CharField(max_length = 20)
    age = models.IntegerField()

    def __str__(self):
        return self.name
    
    def upper_name(self):
        return f'{self.name.upper()}'
    
    def check_age(self):
        if self.age > 18:
            return 'Big boy'
        else:
            return 'Baby boy'
    

class Account(models.Model):
    nickname = models.CharField(max_length = 30)

    profile = models.OneToOneField(Profile,on_delete = models.CASCADE,related_name='profile_key')

    def __str__(self):
        return self.nickname
    
# створення власних валідаторів  ( певні перевірки над іменем, віком і тд )

class Men(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField(validators=[check_age])

# практика методів для роботи зі строками

'''class Practice(models.Model):

    # бінарні та логічні поля 

    binary_date = models.BinaryField() # бінарні дані (наприклад, байти зображень або файлів).
    is_active  = models.BooleanField(default = True) # логічні значення True/False
    #maybe_accepted = models.NullBooleanbField(null = True ) # пише шо воно застаріле для нових моделей Django  / логічне значенння з можливістю null

    # дата та час 

    birth_date = models.DateField() # лише дата
    start_time = models.TimeField() # лише час 
    event_datetime = models.DateTimeField(auto_now_add = True) # дата та час
    duration = models.DurationField() # тривалість

    # Автоінкрементні числові поля 

    id = models.AutoField(primary_key = True) # втоматичне ціле число (первинні ключі)
    big_id = models.BigAutoField(primary_key = True) # 64-бітове автоінкрементне число
    small_id = models.SmallAutoField(primary_key = True) # 16-бітове автоінкрементне число

    # числові поля 

    age = models.IntegerField()
    big_count = models.BigIntegerField()     # цілі значення різного розміру
    small_count = models.SmallIntegerField()

    positive_age = models.PositiveIntegerField()
    positive_big_value = models.PositiveBigIntegerField()     # лише додатні значення
    positive_small_value = models.PositiveSmallIntegerField()

    price = models.DecimalField(max_digits = 10,decimal_places = 2) # фіксована десяткова точність
    rating = models.FloatField() # число з плаваючою комою

    # текстові поля

    name = models.CharField(max_length = 20) # короткі рядки з обмеженням
    description = models.TextField() # довгі рядки (без обмеження)
    email = models.EmailField() # e-mail (автоматична валідація)
    slug = models.SlugField() # короткі "URL-friendly" назви
    website = models.URLField() # повна перевірена URL-адреса

    # файли та зображення

    upload = models.FileField(upload_to = 'uploads/') # шлях до файлу
    file_path = models.FilePathField(path = 'var/www/files/') # шлях до файлу з системи
    image = models.ImageField(upload_to = 'images/') # зображення (перевірка формату)

    # інше 

    ip_address = models.GenericIPAddressField() # IP-адреса (IPv4 або IPv6)
    #uuid = models.UUIDField(default = uuid.uuid4, editable = False ) # ???? 
    metadata = models.JSONField() # зберігає структуру JSON '''








 



   
    







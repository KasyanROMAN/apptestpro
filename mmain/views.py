from django.db.models import F,Case,When,CharField,Value
from django.db.models import Avg, Min, Max, Sum
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Person,Man,Business,Profile,Account


# Create your views here.

def get(request):
    return HttpResponse('hello')

def get_request(request):
    return HttpResponse('Privet')

def third_page(request):
    return HttpResponse('You are welcome!')

def next_step(request,a,b,c):
    return HttpResponse(f'{a+b+c}')

def bababa(request,d,e):
    if d == e:
        return HttpResponse('+')
    else:
        return HttpResponse('-')

def temp(request):
    return render(request,'index.html')

def temp1(request):
    return render(request,'index1.html')

def test(request):
    a = 777
    data = {'key1':a}
    return render(request,'index2.html',data)

def test_dict2(request):
    data2 = {'name':'Yulian','age':25,'hobby':'IT'}
    return render(request,'index3.html',data2)

def sasha_coolman(request):
    sasha = [1,2,3,4,5]
    a = {'key2':sasha}
    return render(request,'index4.html',a)

def privet(request):
    name = request.GET.get('name','Sasha')
    age = request.GET.get('age',12)
    return HttpResponse(f'{name}-{age}')

def view1(request):
    return HttpResponseRedirect('/Privet')

def data(request):
    return render(request,'data.html')

def post_data(request):
    name = request.POST.get('name')
    age = request.POST.get('age')
    return HttpResponse(f'{name}-{age}')

def iPhones(request):
    return render(request,'iPhone15.html')

def iPhone13(request):
    return render(request,'iPhone13.html')

'''people = Person.objects.all()
#print(people.query)
for i in people:
    print(i.id,i.name,i.age,i.hobby)'''#виводиться всі елементи з таблиці 

'''people = Person.objects.get(id = 1)
print(people.id,people.name,people.age,people.hobby)''' #виводиться певний елемент з таблиці

'''def get_new(request):
    people = Person.objects.all()
    return render(request,'new.html',{'new_key':people})'''

#variable = Person.objects.create(name = 'Yulian', age = 25, hobby = 'IT')

'''people = Person.objects.all()#[0:3]
for i in people:
    print(i.name,i.age,i.hobby)'''

'''kukuku = Person(name = 'Andrey', age = 40, hobby = 'basketball')
kukuku.save()'''

#фільтрація

'''people = Person.objects.filter(name = 'Yulian', age = 25)
for i in people:
    print(i.age,i.name) '''

'''people = Person.objects.exclude(name = 'Yulian')
for i in people:
    print(i.name,i.age)'''

# оператори фільтрації 

'''people = Person.objects.filter(age__gt = 18)
for i in people:
    print(i.age,i.name)'''

'''people = Person.objects.all()
for i in people:
    print(i.age,i.name)'''

'''people = Person.objects.filter(age__in = [18,25])
for i in people:
    print(i.age,i.name)'''

'''people = Person.objects.filter(age__range = (18,26))
for i in people:
    print(i.age,i.name)'''

#person = Person.objects.filter(age = 18).exclude(work=‘IT’)

# видалення 

'''people = Person.objects.all()
for i in people:
    print(i.id,i.name,i.age)'''

'''people = Person.objects.get(id = 6)
people.delete()'''

'''people = Person.objects.all()
for i in people:
    print(i.id,i.name)'''

# оновлення 

'''people = Person.objects.get(id = 5)
people.name = 'Olexanchez'
people.save()'''

'''people = Person.objects.all()
for i in people:
    print(i.id,i.name)''' 

# сортування 

'''people = Person.objects.order_by('-age') # order_by('age) / order_by('?')
for i in people:
    print(i.name,i.age)'''

# певний набір ключів та значень 

'''people = Person.objects.values_list('id','name') # список кортежів
print(people)'''

'''people = Person.objects.values('id','name') # список словників
print(people)'''

# отримання списку певних значень, повністю список певного ключа

'''people = Person.objects.values_list('name',flat = True)
print(people)'''

# отримання першого та останнього елементу

'''people = Person.objects.first()
print(people.name,people.age)''' # перший елемент

'''people = Person.objects.last()
print(people.name,people.age)''' # ост елемент

# агрегатні функції 

'''people = Person.objects.aggregate(Max('age'))
print(people)''' # максимальне значення

'''people = Person.objects.aggregate(Min('age'))
print(people)''' # мінімальне значення

'''people = Person.objects.aggregate(Avg('age'))
print(people)''' # середнє значення

'''people = Person.objects.aggregate(Sum('age'))
print(people) ''' # сума значень

'''people = Person.objects.values_list('name').distinct()
print(people) ''' # унікальність / без дублювання

'''people = Person.objects.bulk_create([
    Person(name = 'Kiril',age = 35,hobby = 'Tennis'),
    Person(name = 'Clint',age = 40,hobby = 'Truck Driver')
])''' # створення набору значень, які додаються

# обмеження таблиць 

# відношення таблиць

'''man = Man.objects.create(name = 'Oleg', age = 33)'''

'''man = Man.objects.get(id = 1)

business = Business.objects.create(business_name = 'Car Wash',man = man)'''

'''man = Man.objects.create(name = 'Sanchous', age = 40)

business = Business.objects.create(business_name = 'Shaurmeshna',man = man)'''

'''man = Man.objects.get(id = 2)

businesses = man.business_set.all()
for i in businesses:
    print(i.business_name,i.man.name)'''


'''profile = Profile.objects.create(name = 'Kaka', age = 33)
account = Account.objects.create(nickname = 'Kaka6784', profile = profile )'''

'''profile = Profile.objects.get(id = 1)

account = Account.objects.get(profile = profile)
print(account.profile.name,account.profile.age)'''

'''account = Account.objects.get(id = 1)
print(account.nickname)
print(account.profile.name,account.profile.age)'''

'''profile = Profile.objects.all()
for i in profile:
    print(i.name,i.age,i.upper_name(),i.check_age())'''

'''profile = Profile.objects.get(id = 1)
print(profile.name,profile.age,profile.upper_name())'''

'''person = Person.objects.annotate(
    res = F('age')*20
)
for i in person:
    print(i.name,i.age,i.res)'''

'''person = Person.objects.annotate(
    check = Case(
        When(age__gte = 18,then = Value('Доросла людина')),
        default = Value('Мала людина'),
        output_field = CharField()
    )
)
for i in person:
    print(i.name,i.age,i.check)'''

'''abc = Person.objects.create(name = 'Sasha',age = 12,hobby = 'IT')

all_users = Person.objects.all()
for i in all_users:
    print(i.name,i.age)'''

# базові виключення в django

'''try:
   person = Person.objects.get(id = 1)
   print(person.name)

except Person.MultipleObjectsReturned:
    print('Знайдено багато людей')'''

'''try:
    person = Person.objects.get(id = 1000000)

except Person.DoesNotExist:
    print('Такої людини немає')'''

'''person = Person.objects.get(id = 2)
person.delete()'''

'''people = Person.people.check_full_age(18)
for i in people:
    print(i.name,i.age)'''

'''people = Person.people.first_person()
print(people.name,people.age)'''

'''people = Person.people.all()

for i in people:
    print(i.name,i.age)'''










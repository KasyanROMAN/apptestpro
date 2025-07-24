from django.urls import path, include
from . import views
urlpatterns = [
    path('gggg',views.get,name = 'hello'),
    path('Privet/',views.get_request),
    path('Third/Page/',views.third_page),
    path('ABC/<int:a>/<int:b>/<int:c>/',views.next_step),
    path('BABABA/<str:d>/<str:e>/',views.bababa),
    path('TEMP/',views.temp,name = 'ppp'),
    path('TEMPOPO/',views.temp1),
    path('TEST/',views.test,name = 'test1'),
    path('DATA/',views.test_dict2,name = 'text'),
    path('SASHA/',views.sasha_coolman),
    path('PRIVET/',views.privet),
    path('PPPP/',views.view1),
    path('',views.data),
    path('result/',views.post_data,name = 'result'),
    path('iPhone15/',views.iPhones),
    path('iPhone13/',views.iPhone13)
    #path('new/',views.get_new)
]
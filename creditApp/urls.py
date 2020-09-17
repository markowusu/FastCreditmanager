from django.urls import path
from . import views

app_name = 'creditApp'

urlpatterns =[
    path('',views.get_user,name='users'),
    path('<int:id>',views.get_individual,name='individual'),
]
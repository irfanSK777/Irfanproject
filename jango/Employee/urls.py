from django.urls import path
from . import views

urlpatterns = [
    path('', views.empDetails, name='empDetails'),
    # path('', views.empDetails, name='empDetails'),
    path('input', views.register, name='inputdata'),
    path('output', views.fetchData),
    path('search', views.search_through_number, name='sea_num'),
    path('delete_emp', views.deleteEmp),
    # path('result_page',views.Result, name='result'),
]

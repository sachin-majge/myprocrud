from django.urls import path
from .views import *

app_name='myapp'

urlpatterns=[
    path('view/',show_view,name='view'),
    path('create/',create_data,name='create'),
    path('update/<int:id>',update_data,name='update'),
    path('delete/<int:id>',delete_data,name='delete')
]
from django.urls import path
# from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns=[
    path('',views.supers_list)
# path('<int:pk>/',views.supers_list)
]

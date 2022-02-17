from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('', views.SupersList.as_view()),
    path('<int:pk>/', views.product_detail),
]



# urlpatterns = format_suffix_patterns(urlpatterns)
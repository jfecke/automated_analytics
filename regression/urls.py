from django.conf.urls import url
from regression import views

# TEMPLATE TAGGING
app_name = 'regression'

urlpatterns = [
    url(r'^$', views.index, name='index'),
]

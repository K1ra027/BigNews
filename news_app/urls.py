from django.urls import path
from .views import home, detail, category,registration,log_out,log_in

urlpatterns = [
    path('',home,name='home'),
    path('detail/<int:id>/',detail, name='detail'),
    path('category/<int:id>/',category,name= 'category'),
    path('registration/', registration,name = 'registration'),
    path('login/',log_in, name='login'),
    path('logout/',log_out,name='logout'),
]
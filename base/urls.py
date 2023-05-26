from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name= 'base-home'),
    path('pharmacy', views.harmacy , name='base-pharmacy'),
    path('drug/drugseach', views.drugsearch , name='base-drugsearch'),
    path('all-pharmacy', views.all_pharmacy , name='base-all-pharmacy'),
    path('pharmacy-details/<uuid:pharmacy_id>', views.pharmacy_details , name='base-pharmacy-details'),
    path('register/pharmacy/', views.register, name='base-register'),
    path('drug-details/<uuid:drug_id>', views.drug_details , name='base-drug-details'),
    path('user_register/creat-account', views.user_register, name='base-user-register'),
    path('addrug/for-each-pharmacy', views.add_drug,name='base-add_drug'),
    path('drug_edit/<uuid:edit_id>', views.edit , name='base-edit-drug'),
    path('event/for-pharmacy', views.event,name='base-event'),
    path('contact/us-for-info', views.contact , name='base-contact')
]

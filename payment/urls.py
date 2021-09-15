from django.urls import path
from .views import donations, donation_done, handle_donation

app_name = 'payment'

urlpatterns = [
    path('donations/', donations, name='donations'),
    path('donations/done', donation_done, name='donations_done'),
    path('donations/handle_order', handle_donation, name='donations_handle'),
]

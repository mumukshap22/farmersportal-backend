from django.urls import path
from contact_us.views import ContactUsCreateView

urlpatterns = [
    path('submit/', ContactUsCreateView.as_view(), name='contactus-submit'),
]
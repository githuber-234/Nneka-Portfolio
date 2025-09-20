from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import (ServicesView, AboutView, ProjectsView, TestimonialView,
                    ContactView)

urlpatterns = [
    path('services/', ServicesView.as_view(), name='services'),
    path('', AboutView.as_view(), name='about'),
    path('projects/', ProjectsView.as_view(), name='projects'),
    path('testimonial/', TestimonialView.as_view(), name='testimonial'),
    path('contact/', ContactView.as_view(), name='contact'),
] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
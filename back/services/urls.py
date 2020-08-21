from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'params/$', views.get_params),
    url(r'enable-service/$', views.enable_service),
    url(r'disable-service/$', views.disable_service),
    url(r'start-service/$', views.start_service),
    url(r'stop-service/$', views.stop_service),
    url(r'restart-service/$', views.restart_service),
    url(r'$', views.get_services),
]

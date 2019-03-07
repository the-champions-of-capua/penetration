from django.conf.urls import url

urlpatterns = [

]

from .api.oauth.urls import urlpatterns as oauth_urlparterns
urlpatterns += oauth_urlparterns

from django.conf.urls import url

urlpatterns = [
    url(r'^login/$','accounts.views.login'),
    url(r'^signup/$','accounts.views.signup', name='signup'),
    url(r'^signup/complete/$', 'accounts.views.signup_complete',name='signup_complete'),
    url(r'^confirm/(?P<token>[a-z0-9\-]+)/', ('accounts.views.signup_confirm')),
]
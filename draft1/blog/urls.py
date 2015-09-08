from django.conf.urls import url

urlpatterns = [
    url(r'^$', 'blog.views.index', name='index'),
    url(r'^apply/$', 'blog.views.apply', name='apply'),
    url(r'^apply/thanks/$', 'blog.views.thanks', name='thanks'),
    url(r'^profile/$','blog.views.profile', name='profile'),
]

from django.conf.urls import patterns, include, url

from rest_framework import routers
from wangli_api.app import views

urlpatterns = patterns('',)

router = routers.DefaultRouter()
router.register(r'router/users', views.UserViewSet)
router.register(r'router/groups', views.GroupViewSet)

urlpatterns += [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
urlpatterns += [
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),

    url(r'^app/snippets/$', views.SnippetList.as_view()),
    url(r'^app/snippets/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view()),
]

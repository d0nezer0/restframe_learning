from django.conf.urls import patterns, include, url

from rest_framework import routers
from wangli_api.app import views

urlpatterns = patterns('',)

router = routers.DefaultRouter()
router.register(r'router/users', views.UserViewSet)
router.register(r'router/groups', views.GroupViewSet)

router.register(r'router/snippets', views.SnippetViewSet)

urlpatterns += [
    url(r'^', include(router.urls)),
    # this is for user to login and logout
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
urlpatterns += [
    url(r'^$', views.api_root),

    # url(r'^users/$', views.UserList.as_view(), name='user-list'),
    # url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), name='user-detail'),
    #
    # url(r'^app/snippets/$', views.SnippetList.as_view(), name='snippet-list'),
    # url(r'^app/snippets/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view(), name='snippet-detail'),
    # url(r'^app/snippets/(?P<pk>[0-9]+)/highlight/$', views.SnippetHighlight.as_view(), name='snippet-highlight'),
]

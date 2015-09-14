from django.conf.urls import patterns, include, url

from rest_framework import routers
from wangli_api.app import views

urlpatterns = patterns('',)

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns += [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
urlpatterns += [
    url(r'^app/snippets/$', views.SnippetList.as_view()),
    url(r'^app/snippets/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view()),
]

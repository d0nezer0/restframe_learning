# -*- coding: utf-8 -*-
from rest_framework import permissions
from permission_settings import API_LEVEL, CLIENT_LEVEL, PRIVILEGE_DICT


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    Now, if you open a browser again, you find that the 'DELETE' and 'PUT' actions only appear on a snippet instance
    endpoint if you're logged in as the same user that created the code snippet.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        print '111'*100
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the snippet.
        return obj.owner == request.user


# class FirstLevelAuthority(permissions.BasePermission):
#     """
#     authority for first level
#     """
#     def has_object_permission(self, request, view, obj):
#         client_name = request.GET.get('promo_token')
#         # api_name = request.GET.get('api')
#         if client_name in API_CLIENT_LEVEL_1:
#             return True
#         else:
#             return False


class AurhorityForRequest(permissions.BasePermission):
    """
    把所有权限一起处理.
    请求地址: http://127.0.0.1:8888/router/snippets/2/?promo_token=360&api=sss
    """
    def has_object_permission(self, request, view, obj):
        client_name = request.GET.get('promo_token')
        api_name = request.GET.get('api')

        try:
            if api_name in PRIVILEGE_DICT[client_name]:
                return True
        except Exception, e:
            print e

        ret = map(lambda x,y: (api_name in x[1] and client_name in y[1]), API_LEVEL, CLIENT_LEVEL)
        return True if True in ret else False

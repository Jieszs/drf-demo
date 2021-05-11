import logging

from rest_framework import serializers
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import exception_handler

from apps.common.basic import GlobalResponse

error_logger = logging.getLogger('error')
info_logger = logging.getLogger('info')


def global_exception_handler(exc, context):
    response = exception_handler(exc, context)
    if response is not None:
        msg = '失败' if response.status_code >= 400 else '成功'
        notification_response = {}
        notification_response['code'] = response.status_code
        notification_response['message'] = msg
        notification_response['detail'] = response.data
        response.data = notification_response
    return response


class CommonPagination(PageNumberPagination):
    '''
    分页设置
    '''
    page_size = 10
    page_size_query_param = 'size'

class TreeSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    label = serializers.CharField(max_length=20, source='name')
    pid = serializers.PrimaryKeyRelatedField(read_only=True)


class TreeAPIView(ListAPIView):
    '''
    自定义树结构View
    '''
    serializer_class = TreeSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        serializer = self.get_serializer(queryset, many=True)
        tree_dict = {}
        tree_data = []
        try:
            for item in serializer.data:
                tree_dict[item['id']] = item
            for i in tree_dict:
                if tree_dict[i]['pid']:
                    pid = tree_dict[i]['pid']
                    parent = tree_dict[pid]
                    parent.setdefault('children', []).append(tree_dict[i])
                else:
                    tree_data.append(tree_dict[i])
            results = tree_data
        except KeyError:
            results = serializer.data
        if page is not None:
            return self.get_paginated_response(results)
        return GlobalResponse(results)

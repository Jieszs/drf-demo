# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action, api_view
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response

from common.custom import CommonPagination
from musics.models import Music, fun_raw_sql_query, fun_sql_cursor_update
from musics.serializers import MusicSerializer

from rest_framework import viewsets, status


# Create your views here.
class MusicViewSet(viewsets.ModelViewSet):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer  # 序列器
    pagination_class = CommonPagination  # 分页
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filter_fields = ('singer',)  # 等于条件?singer=
    search_fields = ('song',)  # 搜索条件，相当于like
    ordering_fields = ('id',)  # 排序

    @action(methods=['get'], detail=False)
    def raw_sql_query(self, request):
        song = request.query_params.get('song', None)
        music = fun_raw_sql_query(song=song)
        serializer = MusicSerializer(music, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(methods=['put'], detail=True)
    def sql_cursor_update(self, request, pk=None):
        song = request.data.get('song', None)
        if song:
            music = fun_sql_cursor_update(song=song, pk=pk)
            return Response(music, status=status.HTTP_200_OK)

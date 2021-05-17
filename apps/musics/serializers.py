from django.utils.timezone import now
from rest_framework import serializers

from apps.musics.models import Music


class ToUpperCaseCharField(serializers.CharField):
    def to_representation(self, value):
        return value.upper()

class MusicSerializer(serializers.ModelSerializer):
    days_since_created = serializers.SerializerMethodField()
    singer = ToUpperCaseCharField()
    class Meta:
        model = Music
        # fields = '__all__'
        fields = ('id', 'song', 'singer', 'last_modify_date', 'created', 'days_since_created')
    song = serializers.CharField(required=True, error_messages={'required': '必填字段'})

    def validate_song(self, value):  # 对单一字段校验
        if "BDYJY" not in value.upper():
            return value
        raise serializers.ValidationError('标题里含有非法字符')  # 抛出错误

    def get_days_since_created(self, obj):
        return (now() - obj.created).days

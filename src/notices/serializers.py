from rest_framework import serializers
from .models import Notice, NoticePost

class NoticeListSerializer(serializers.ModelSerializer):

    message = serializers.SerializerMethodField()
    icon_path = serializers.SerializerMethodField()
    posts = serializers.SerializerMethodField()
    reminders = serializers.SerializerMethodField()
    read = serializers.SerializerMethodField()

    class Meta:
        model = Notice
        fields = [
            'id',
            'message',
            'category_id',
            'icon_path',
            'read',
            'posts',
            'reminders'
        ]
    
    def get_posts(self, instance):
        return {
            'title': instance.noticepost.post_title
        } if hasattr(instance, 'noticepost') else None
    
    def get_reminders(self, instance):
        return {
            'orderitem_ref_code': instance.noticereminder.orderitem.ref_code
        } if hasattr(instance, 'noticereminder') else None
    
    def get_message(self, instance):
        return instance.category.message
    
    def get_icon_path(self, instance):
        return str(instance.category.icon_path)
    
    def get_read(self, instance):
        user = self.context['request'].user
        return not user.notice_set.filter(noticeread__read_at=None,id=instance.id).exists()

class NoticePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = NoticePost
        fields = [
            'id',
            'post_title',
            'text',
            'created_at',
            'last_edited_at',
            'published_at'
        ]
from .models import Video
from rest_framework import serializers

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['video_id', 'like', 'dislike', 'comment', 'reply']

        def create(self, validated_data):
            return Video.objects.create(**validated_data)

        def update(self, instance, validated_data):
            instance.video_id = validated_data.get('video_id', instance.video_id)
            instance.like = validated_data.get('like', instance.like)
            instance.dislike = validated_data.get('dislike', instance.dislike)
            instance.comment = validated_data.get('comment', instance.comment)
            instance.reply = validated_data.get('reply', instance.reply)
            instance.save()
            return instance
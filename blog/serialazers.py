from rest_framework import serializers

from blog.models import Post


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ('url', 'image', 'title', 'text', 'publication_date', 'user_email')
        read_only_fields = ('publication_date', 'user_email')

    def create(self, validated_data):
        post = Post(
            title=validated_data['title'],
            image=validated_data['image'],
            text=validated_data['text'],
            user_email=validated_data['user_email']
        )
        post.save()
        return post

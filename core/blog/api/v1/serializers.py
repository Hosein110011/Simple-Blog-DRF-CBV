from rest_framework import serializers
from ... models import Post, Category
from app.models import Profile



# class PostSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField(max_length=255)

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class PostSerializer(serializers.ModelSerializer):
    snippet = serializers.ReadOnlyField(source='get_snippet')
    relative_url = serializers.ReadOnlyField(source ='get_absolute_api_url')
    absolute_url = serializers.SerializerMethodField(method_name='get_abs_url')
    # category = serializers.SlugRelatedField(many=False, slug_field='name', queryset=Category.objects.all())
    # category = CategorySerializer()
    # content = serializers.ReadOnlyField()
    # content = serializers.CharField(read_only=True)
    class Meta:
        model = Post
        fields = ['id','author', 'image','title', 'content','category' ,'status','snippet', 'absolute_url', 'relative_url','created_date', 'published_date']
        read_only_fields = ['content', 'author']

    def get_abs_url(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(obj.id)


    def to_representation(self, instance):
        request = self.context.get('request')
        rep = super().to_representation(instance)
        rep['state'] = 'list'
        if request.parser_context.get('kwargs').get('pk'):
            rep['state'] = 'single'
            rep.pop('relative_url', None)
            rep.pop('absolute_url', None)
            rep.pop("snippet")
        else:
            rep.pop("content", None)
        rep['appname'] = 'practice00'
        rep['category'] = CategorySerializer(instance.category).data

        return rep
    
    def create(self, validated_data):
        validated_data['author'] = Profile.objects.get(user__id = self.context.get('request').user.id)
        return super().create(validated_data)
from rest_framework import serializers
from .models import Article


class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        #fields = ['id','title','author','email']
        fields = '__all__'
    # title = serializers.CharField(max_length=100)
    # author = serializers.CharField(max_length=100)
    # email = serializers.EmailField(max_length=100)
    # date = serializers.DateTimeField()

    # def create(self, validated_data):
    #     return Article.objects.create(validated_data)

    # def update(self,instance,validated_data):
    #     instance.title = validated_data.get('title',instance.title)
    #     instance.title = validated_data.get('author',instance.author)
    #     instance.title = validated_data.get('email',instance.email)
    #     instance.title = validated_data.get('date',instance.date)
    #     instance.save()
    #     return instance
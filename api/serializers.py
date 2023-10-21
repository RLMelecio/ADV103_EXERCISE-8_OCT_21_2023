from rest_framework.serializers import ModelSerializer
from ..models import Album, Musician, Tag, Category, Article

class AlbumSerializer(ModelSerializer):
    class Meta:
        model = Album
        fields = '__all__'
    
class MusicianSerializer(ModelSerializer):
    class Meta:
        model = Musician
        fields = '__all__'

class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ArticleSerializer(ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'

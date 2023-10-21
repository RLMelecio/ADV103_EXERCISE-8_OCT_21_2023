from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Musician,Album,Tag,Category,Article

# Register your models here.
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    search_fields = ('tag_name',)
    list_display = ('id', 'tag_name')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ('category_name',)
    list_display = ('id', 'category_name')

@admin.register(Musician)
class MusicianAdmin(admin.ModelAdmin):
    search_fields = ('first_name', 'last_name',)
    list_display = ('first_name', 'last_name', 'instrument')

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    search_fields = ('album_name',)
    list_display = ('get_artist_last_name', 'album_name', 'release_date', 'num_stars')

    def get_artist_last_name(self, obj):
        return obj.artist.last_name

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    list_display = ('id', 'title', 'content', 'publish_date')
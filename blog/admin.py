from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import IndexDescription, Post, Contact, PhotoGallery


class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)
    prepopulated_fields = { 'slug': ('title',), }


class GalleryAdmin(admin.ModelAdmin):
    prepopulated_fields = { 'slug': ('title',), }


class IndexAdmin(admin.ModelAdmin):
    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False


admin.site.register(IndexDescription, IndexAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(PhotoGallery, GalleryAdmin)
admin.site.register(Contact)

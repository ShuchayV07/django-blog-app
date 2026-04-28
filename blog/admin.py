from django.contrib import admin
from .models import Tag,Author,Post
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}
    list_filter = ('author','tags','date')
    list_display = ('title','date','author')
admin.site.register(Post,PostAdmin)
admin.site.register(Tag)
admin.site.register(Author)


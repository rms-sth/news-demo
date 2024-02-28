from django.contrib import admin
from newspaper.models import Comment, Contact, Post, Category, Tag, UserProfile

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Contact)
admin.site.register(UserProfile)
admin.site.register(Comment)

from django.contrib import admin

# Register your models here.
from blog.models import Post, Person, Family

admin.site.register(Post)
admin.site.register(Person)
admin.site.register(Family)


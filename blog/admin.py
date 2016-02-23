from django.contrib import admin

# Register your models here.
from blog.models.models import Post, Person, Family, Education

admin.site.register(Post)
admin.site.register(Person)
admin.site.register(Family)
admin.site.register(Education)

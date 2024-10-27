from django.contrib import admin
from .models import user_master,college_master,add_book,book_issuse
admin.site.register(user_master)
admin.site.register(college_master)
admin.site.register(add_book)
admin.site.register(book_issuse)

# Register your models here
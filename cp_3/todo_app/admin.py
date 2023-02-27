from django.contrib import admin
from .models import TodoList, Todo
# Register your models here.


admin.site.register(TodoList)
admin.site.register(Todo)
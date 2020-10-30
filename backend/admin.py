from django.contrib import admin
from .models import Article
from .models import ProjectSql


# Register your models here.
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_online', 'author', 'create_time', 'last_update_time')
    ordering = ('id', )    # 正序id,倒序-id


@admin.register(ProjectSql)
class ProjectSql(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'address_ip', 'create_time', 'modify_time',)
    search_fields = ('project_name', 'address_ip',)
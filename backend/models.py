from django.db import models
from django.contrib.auth.models import User  # 引入用户模型


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)  # auto_now_add=True 添加时自动设置当前时间
    last_update_time = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, default=1)  # default为auth_user的id
    is_online = models.BooleanField(default=False)  # 上下架
    read_num = models.IntegerField(default=100)

    def __str__(self):
        return self.title


class ProjectSql(models.Model):
    project_name = models.CharField(max_length=50, unique=True)     # unique=True设置唯一键
    address_ip = models.CharField(max_length=100)
    account = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    # models.Index(fields=(project_name, )  # 创建索引
    port = models.IntegerField(default=3306)
    create_time = models.DateTimeField(auto_now_add=True)
    modify_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.project_name

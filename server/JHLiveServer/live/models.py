from django.db import models

# Create your models here.
class UserInfo(models.Model):
    # 用户信息
    phone = models.CharField(u'手机号',max_length=20)
    password = models.CharField(u'密码',max_length=20)
    nickname = models.CharField(u'昵称', max_length=100)
    haveLive = models.IntegerField(u'是否在直播', default=1) # 1:没直播 2:正在直播
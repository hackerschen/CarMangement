from django.db import models

# Create your models here.
class passPort(models.Model):
    id = models.AutoField(primary_key=True) # id 会自动创建,可以手动写入
    number = models.CharField(max_length=10) # 护照号码
    name = models.CharField(max_length=64) # 姓名
    sex = models.BooleanField() # 性别
    native_place = models.CharField(max_length=64) # 籍贯
    company_name = models.CharField(max_length=64) # 单位名称
    save_number = models.CharField(max_length=64) # 存档编号
    valid_date = models.IntegerField() # 有效日期
    brith_date = models.DateField(auto_now=True) # 出生日期
    get_date = models.DateField(auto_now=True) # 发证日期
    out_date = models.DateTimeField(auto_now=True) # 出访日期
    last_date = models.DateTimeField(auto_now=True) # 最后更新日期
    state = models.IntegerField() # 护照状态
from django.db import models
from django.utils import timezone


class Category(models.Model):
  name = models.CharField('カテゴリー名',max_length=25)
  created_at = models.DateTimeField('作成日', default=timezone.now)

  def __str__(self):
    return self.name

class Post(models.Model):
  """ブログの記事"""
  title = models.CharField('タイトル',max_length=30)
  text = models.TextField('本文')
  created_at = models.DateTimeField('作成日',default=timezone.now)
  category = models.ForeignKey(Category,verbose_name='カテゴリー',on_delete=models.PROTECT)

  def __str__(self):
    return self.title



# Create your models here.

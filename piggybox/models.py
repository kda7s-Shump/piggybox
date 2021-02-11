import datetime
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils import timezone

class Deal(models.Model):
  CATEGORY_LABEL = (
    ('poc', 'おこずかい'),
    ('sal', '給与'),
    ('oti', 'その他所得'),
    ('foo', '食費'),
    ('boo', '教育'),
    ('tra', '交通費'),
    ('sho', 'ショッピング'),
    ('prs', 'プレゼント'),
    ('ent', '交際費'),
    ('fee', '手数料'),
    ('oto', 'その他消費'),
  )

  # define 
  date = models.DateField('日付', default=timezone.now)
  in_out = models.IntegerField('収支', validators=[MinValueValidator(-999999), MaxValueValidator(999999)])
  category = models.CharField(
    'カテゴリー',
    choices=CATEGORY_LABEL,
    default='foo',
    max_length=3,
  )
  description = models.CharField('内容', blank=True, max_length=50)

  user = models.ForeignKey(
    User,
    on_delete=models.SET_NULL,
    null=True,
  )

  def __str__(self):
    return self.description

class Wishlist(models.Model):
  name = models.CharField('名前', max_length=100)
  image = models.ImageField('画像', upload_to='images/', blank=True)
  price = models.IntegerField('価格',
    validators=[
      MinValueValidator(0),
      MaxValueValidator(9999999)
    ],
    blank=True,
  )
  term = models.IntegerField('期間',
    validators=[
      MinValueValidator(1),
      MaxValueValidator(3653)
    ],
    blank=True,
  )
  url = models.CharField('URL', max_length=255, blank=True)
  created_at = models.DateTimeField('作成日', auto_now_add=True)
  memo = models.TextField(
    '備考',
    blank=True,
    max_length=300,
    )

  user = models.ForeignKey(
    User,
    on_delete=models.SET_NULL,
    null=True,
  )
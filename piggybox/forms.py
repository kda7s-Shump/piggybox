from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Deal, Wishlist

class DealForm(forms.ModelForm):
  class Meta:
    model = Deal
    fields = ['date', 'in_out', 'category', 'summary']

class SignUpForm(UserCreationForm):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    # HTMLの表示を変更可能にします
    self.fields['username'].widget.attrs['class'] = 'form-control'
    self.fields['username'].widget.attrs['placeholder'] = 'ニックネーム'
    self.fields['email'].widget.attrs['class'] = 'form-control'
    self.fields['email'].widget.attrs['placeholder'] = 'hogehoge@example.com'
    self.fields['password1'].widget.attrs['class'] = 'form-control'
    self.fields['password1'].widget.attrs['placeholder'] = 'パスワード (8文字以上)'
    self.fields['password2'].widget.attrs['class'] = 'form-control'
    self.fields['password2'].widget.attrs['placeholder'] = 'パスワード (確認用)'

  class Meta:
    model = User
    fields = ('username', 'email', 'password1', 'password2')

class WishlistForm(forms.ModelForm):
  class Meta:
    model = Wishlist
    fields = ['name', 'image', 'price', 'term', 'url', 'memo']
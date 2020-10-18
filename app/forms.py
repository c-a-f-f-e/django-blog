from django import forms
from .models import Category


class PostForm(forms.Form):
    category_data = Category.objects.all()
    category_choice = {}
    for category in category_data:
        category_choice[category] = category
        
class PostForm(forms.Form):
    title = forms.CharField(max_length=30, label='タイトル')
    content = forms.CharField(label='内容', widget=forms.Textarea())
    image = forms.ImageField(label='イメージ画像', required=False) # 追加

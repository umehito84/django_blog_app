from django import forms
from .models import Post

class PostCreateForm(forms.ModelForm):
	# DjangoのModelFormでは強力なValidationを使える
	class Meta:
		model = Post # Post モデルと接続し、Postモデルの内容に応じてformを作ってくれる
		fields = ('title', 'text')  #　入力するカラムを指定
		# fields = 'all'と定義して全てのカラムを手入力するように指定も可能
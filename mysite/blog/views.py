from django.views import generic
from django.urls import reverse_lazy
from .forms import PostCreateForm # forms.py で作ったクラスをimport
from .models import Post

# Create your views here.

# class IndexView(generic.TemplateView):
# 	template_name = 'blog/index.html'

class PostListView(generic.ListView):
	model = Post

class PostCreateView(generic.CreateView):
	model = Post # 作成したい modelを指定
	form_class = PostCreateForm # 作成した form　クラスを指定
	success_url = reverse_lazy('blog:post_list')  # 記事作成に成功した時のリダイレクト先を指定
	
class PostDetailView(generic.DetailView):
	model = Post  #pk(primary key)はurls.pyで指定しているのでここではmodelを呼び出すだけで済む

class PostUpdateView(generic.UpdateView):
	model = Post
	form_class = PostCreateForm  # PostCreateFormをほぼそのまま活用できる
	success_url = reverse_lazy('blog:post_detail')

class PostDeleteView(generic.DeleteView):
	model = Post
	success_url = reverse_lazy('blog:post_list')
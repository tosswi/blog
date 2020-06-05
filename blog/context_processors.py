from .models import Category

def common(request):
  """テンプレートに毎回渡す"""
  context = {
    'category_list':Category.objects.all(),
  }
  return context
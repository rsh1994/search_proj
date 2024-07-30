from haystack import indexes
from .models import Book

class BookIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.EdgeNgramField(document=True, use_template=True)
    title = indexes.CharField(model_attr='title')
    author = indexes.CharField(model_attr='author')
    published_date = indexes.DateField(model_attr='published_date')

    def get_model(self):
        return Book

    def index_queryset(self, using=None):
        return self.get_model().objects.all()
# Third party imports.
from rest_framework import serializers

# Local application imports
from blog.models.article_models import Article


class ArticleSerializer(serializers.ModelSerializer):
    category = serializers.ReadOnlyField(source="category.name")
    minister = serializers.ReadOnlyField(source="minister.username")

    class Meta:
        model = Article
        fields = ('category', 'title', 'minister', 'image', 'body',
                  'date_published'
                  )
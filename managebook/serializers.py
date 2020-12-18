from rest_framework.serializers import ModelSerializer
from rest_meets_djongo.serializers import DjongoModelSerializer
from managebook.models import Book, BookThroughFields


class BookSerializer(DjongoModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class BookFieldSerializer(DjongoModelSerializer):
    class Meta:
        model = BookThroughFields
        fields = ['_id',
                  'title',
                  'slug',
                  'body_text',
                  'objects',
                  'pub_date',
                  'rating',
                  ]

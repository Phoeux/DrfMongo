# from djongo import models
# from rest_framework.authtoken.admin import User
#
#
# class Genre(models.Model):
#     title = models.CharField(max_length=50)
#
#     def __str__(self):
#         return self.title
#
#
# # class Genre(models.Model):
# #     title = models.CharField(max_length=20)
# #
# #     class Meta:
# #         abstract = True
#
#
# # class BookRate(models.Model):
# #     rate = models.IntegerField(default=0)
# #
# #     class Meta:
# #         abstract = True
# class Author(models.Model):
#     name = models.CharField(max_length=200)
#     email = models.EmailField()
#
#     def __str__(self):
#         return self.name
#
#
# class CommentLike(models.Model):
#     comment_like = models.BooleanField(default=False)
#
#     class Meta:
#         abstract = True
#
#
# class Comment(models.Model):
#     comment_like = models.EmbeddedField(
#         model_container=CommentLike
#     )
#
#     text = models.CharField(max_length=200)
#     author = models.EmbeddedField(model_container=Author,)
#
#     class Meta:
#         abstract = True
#
#
# class Book(models.Model):
#     # genre = models.ArrayField(
#     #     model_container=Genre,
#     #
#     # )
#     # rate = models.EmbeddedField(
#     #     model_container=BookRate,
#     #     null=True
#     # )
#
#     # _id = models.ObjectIdField()
#     title = models.CharField(max_length=50, unique=True)
#     text = models.CharField(max_length=200)
#     pub_date = models.DateField(auto_now_add=True)
#
#     genre = models.ManyToManyField(Genre)
#     authors = models.ArrayField(
#         model_container=User,
#     )
#
#     rate = models.IntegerField(default=0)
#     cached_rate = models.DecimalField(max_digits=3, decimal_places=2, default=0)
#
#     comment = models.ManyToManyField
#
#     def __str__(self):
#         return self.title

# from djongo import models
#
#
# class Genre(models.Model):
#     title = models.CharField(max_length=100)
#
#     class Meta:
#         abstract = True
#
#
# class MetaData(models.Model):
#     pub_date = models.DateField()
#     mod_date = models.DateField()
#     n_pingbacks = models.IntegerField()
#     rating = models.IntegerField()
#
#     class Meta:
#         abstract = True
#
#
# class Author(models.Model):
#     name = models.CharField(max_length=200)
#     email = models.EmailField()
#
#     class Meta:
#         abstract = True
#
#     def __str__(self):
#         return self.name
#
#
# class Book(models.Model):
#     headline = models.CharField(max_length=255)
#     body_text = models.TextField()
#     pub_date = models.DateField()
#     rating = models.IntegerField()
#     genre = models.EmbeddedField(
#         model_container=Genre,
#     )
#     authors = models.ArrayField(
#         model_container=Author,
#     )
#
#     def __str__(self):
#         return self.headline
from djongo import models
from django.contrib.auth.models import AbstractUser


class GenreField(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название жанра')

    def __str__(self):
        return self.title


class Genre(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название жанра')

    class Meta:
        abstract = True

    def __str__(self):
        return self.title


class AuthorField(models.Model):
    name = models.CharField(max_length=200, verbose_name='Имя автора')

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=200, verbose_name='Имя автора')

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


# class User(models.Model):
#     name = models.CharField()
#
#     class Meta:
#         abstract = True


class CommentLike(models.Model):
    comment_likes = models.IntegerField(default=0, blank=True)

    class Meta:
        abstract = True

    # def __int__(self):
    #     return self.comment_likes



class CommentField(models.Model):
    comment_like = models.ArrayField(
        model_container=CommentLike,
        blank=True
    )

    text = models.TextField(max_length=200)
    User = models.ArrayField(model_container=Author, )

    def __str__(self):
        return self.text


class Comment(models.Model):
    comment_like = models.ArrayField(
        model_container=CommentLike,
        blank=True
    )

    text = models.TextField(max_length=200)
    User = models.ArrayField(model_container=Author, )

    class Meta:
        abstract = True

    # def __str__(self):
    #     return f'{self.text, self.User, self.comment_like}'
        # return self.objects.all()


class Book(models.Model):
    _id = models.ObjectIdField()
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    body_text = models.TextField()
    objects = models.DjongoManager()
    genre = models.ArrayField(
        model_container=Genre,
    )
    authors = models.ArrayField(
        model_container=Author,
    )
    pub_date = models.DateField(auto_now_add=True)
    rating = models.IntegerField(default=0, blank=True)

    # n_comments = models.IntegerField()
    comments = models.ArrayField(
        model_container=Comment,
        blank=True
    )

    def __str__(self):
        return self.title


class BookThroughFields(models.Model):
    _id = models.ObjectIdField()
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    body_text = models.TextField()
    objects = models.DjongoManager()
    genre = models.ArrayReferenceField(
        to=GenreField,
        on_delete=models.CASCADE,
    )
    authors = models.ArrayReferenceField(
        to=AuthorField,
        on_delete=models.CASCADE,
    )
    pub_date = models.DateField(auto_now_add=True)
    rating = models.IntegerField(default=0, blank=True)
    # n_comments = models.IntegerField()
    comments = models.ArrayReferenceField(
        to=CommentField, on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title

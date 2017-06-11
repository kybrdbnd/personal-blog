from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=120, unique=True)
    created = models.DateField(auto_now_add=True, auto_now=False)
    updated = models.DateField(auto_now_add=False, auto_now=True)
    slug = models.SlugField(max_length=100)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:category', kwargs={'slug': self.slug})


class Author(models.Model):
    name = models.CharField(max_length=120)
    created = models.DateField(auto_now_add=True, auto_now=False)
    updated = models.DateField(auto_now_add=False, auto_now=True)
    slug = models.SlugField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blog:author', kwargs={'slug': self.slug})


class Comment(models.Model):
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    comment = models.TextField()
    given_by = models.ForeignKey(User)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.comment


class Blog(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100)
    content = models.TextField()
    created = models.DateField(auto_now_add=True, auto_now=False)
    updated = models.DateField(auto_now_add=False, auto_now=True)
    category = models.ForeignKey(Category)
    author = models.ForeignKey(Author)
    likes = models.ManyToManyField(User,
                                   blank=True,
                                   related_name='blog_like')
    dislikes = models.ManyToManyField(User,
                                      blank=True,
                                      related_name='blog_dislike')
    comments = models.ManyToManyField(Comment,
                                      blank=True,
                                      related_name='blog_comment')

    class Meta:
        ordering = ['-updated']

    def __str__(self):
        return self.title

    def likes_count(self):
        return self.likes.count()

    def dislikes_count(self):
        return self.dislikes.count()

    def comments_count(self):
        return self.comments.count()

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'slug': self.slug})

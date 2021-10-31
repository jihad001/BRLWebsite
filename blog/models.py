from os import EX_DATAERR
from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE, PROTECT
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name_plural = 'Categories'
        
        
        
class Post(models.Model):
    
    class PostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='published')
    
    options = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    
    category = models.ForeignKey(Category, on_delete=PROTECT, default=1)
    title = models.CharField(max_length=255)
    excerpt = models.TextField()
    content = models.TextField()
    slug = models.SlugField(max_length=255, unique_for_date='published')
    published = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=CASCADE, related_name='blog_posts')
    status = models.CharField(max_length=10, choices=options, default='published')
    
    objects = models.Manager()
    postobjects = PostObjects()
    
    class Meta:
        ordering = ('-published',)
        
    
    def __str__(self):
        return self.title
    
    

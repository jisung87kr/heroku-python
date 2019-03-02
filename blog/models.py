from django.utils import timezone
from django.db import models
from ckeditor.fields import RichTextField
from django.db.models.signals import post_delete
from django.dispatch import receiver

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete = models.CASCADE)
    title = models.CharField(max_length=200, null=False, blank=False)
    # content = models.TextField(null=False, blank=False)
    content = RichTextField(null=False, blank=False)
    upload = models.ImageField(upload_to='%Y/%m/%d/', null=True, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

#게시글 삭제시 업로드된 파일도 삭제
@receiver(post_delete, sender=Post)
def submission_delete(sender, instance, **kwargs):
    instance.upload.delete(False) 
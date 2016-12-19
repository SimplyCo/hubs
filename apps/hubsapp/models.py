from django.db import models
from django.utils.translation import ugettext_lazy as _
#####
from django.utils import timezone
from apps.accounts.models import CustomUser
#####

class Tag(models.Model):

    class Meta:
        ordering = ['name']

    name = models.CharField(max_length=400, verbose_name=_('Name'))
    slug = models.SlugField(max_length=400, verbose_name=_('Slug'))

    def __str__(self):
        return self.name


class PostImage(models.Model):

    image = models.ImageField(_('Image'), upload_to='course_record_images', blank=True, default='')
    created_at = models.DateTimeField(_('Creation date'), auto_now_add=True, blank=False)

    def __str__(self):
        if self.has_image():
            return self.image.url
        return ''

    def has_image(self):
        return self.image and hasattr(self.image, 'url')


#####
class Hub(models.Model):
    author = models.ForeignKey(CustomUser)
    title = models.CharField(max_length=400, verbose_name=_('Title'))
    slug = models.SlugField(max_length=400, verbose_name=_('Slug'))
    description = models.TextField(verbose_name=_('Description'))
    image = models.ImageField(_('Image'), upload_to='hub_images', blank=True, default='')
    created_date = models.DateTimeField(_('Creation date'), auto_now_add=True, blank=False)

    def __str__(self):
        return self.title


class Post(models.Model):
    class Meta():
        db_table = "post"

    author = models.ForeignKey(CustomUser)
    title = models.CharField(max_length=400, verbose_name=_('Title'))
    slug = models.SlugField(max_length=400, verbose_name=_('Slug'))
    leading_image = models.ImageField(_('Image'), upload_to='hub_images', blank=True, default='')
    short_text = models.TextField(verbose_name=_('Short Text'))
    full_text = models.TextField(verbose_name=_('Full Text'))
    published_date = models.DateTimeField(_('Published Date'), auto_now_add=True, blank=False)
    changed_date = models.DateTimeField(_('Changed Date'), auto_now_add=True, blank=False)
    status = models.CharField(max_length=200, default='Draft')
    placement = models.CharField(max_length=200, default='Blog')

    hub = models.ForeignKey(Hub, blank=True, null=True)

    def __str__(self):
        return self.title

#####

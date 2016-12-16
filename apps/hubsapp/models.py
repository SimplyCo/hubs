from django.db import models
from django.utils.translation import ugettext_lazy as _


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
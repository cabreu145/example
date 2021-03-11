import uuid
import os
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from project.templatetags.utils_tags import format_datetime
from .utils import auto_delete_filefields_on_delete



################################################################################
# BaseModel

class BaseModel(models.Model):
    """
    Base class for all models;
    defines common metadata
    """
    class Meta:
        abstract = True
        ordering = ('-created', )  # better choice for UI
        get_latest_by = "-created"

    # Primary key
    id = models.UUIDField('id', default=uuid.uuid4, primary_key=True, unique=True,
        null=False, blank=False, editable=False)

    # metadata
    created = models.DateTimeField(_('created'), null=True, blank=True, )
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_('created by'), null=True, blank=True, related_name='+', on_delete=models.SET_NULL)
    updated = models.DateTimeField(_('updated'), null=True, blank=True, )
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_('updated by'), null=True, blank=True, related_name='+', on_delete=models.SET_NULL)

    def __str__(self):
        return str(self.id)

    def get_admin_url(self):
        return reverse("admin:%s_%s_change" %
            (self._meta.app_label, self._meta.model_name), args=(self.id,))

    def get_absolute_url(self):
        return self.get_admin_url()

    def created_display(self):
        return format_datetime(self.created)
    created_display.short_description = _('Created')
    created_display.admin_order_field = 'created'

    def updated_display(self):
        return format_datetime(self.updated)
    updated_display.short_description = _('Updated')
    updated_display.admin_order_field = 'updated'

    def save(self, *args, **kwargs):
        today = timezone.now()
        if self.created is None:
            self.created = today
        self.updated = today
        return super(BaseModel, self).save(*args, **kwargs)


class File(BaseModel):

    class Meta(BaseModel.Meta):
        abstract = False
        verbose_name = _("Foto")
        verbose_name_plural = _("Fotos")

    description = models.CharField(_('description'), max_length=256, null=False, blank=True)
    file = models.FileField(_('File'), null=True, blank=True, upload_to='uploads/')

    def __str__(self):
        text = self.description
        if len(text) <= 0:
            text = str(self.id)
        return text

models.signals.post_delete.connect(auto_delete_filefields_on_delete, sender=File)


class Categoria(models.Model):
    cat = models.CharField(max_length=100, null=False, blank=False)

    class Meta:
        verbose_name = u'Categoria'
        verbose_name_plural = u'Categorias'

    def __str__(self):
        return self.cat


class URL(models.Model):
    down = models.CharField(max_length=100, null=False, blank=False)

    class Meta:
        verbose_name = u'link de descarga'
        verbose_name_plural = u'Links de descargas'

    def __str__(self):
        return self.down

class Video (models.Model):
    mp4 = models.FileField(upload_to = 'videos/mp4',null=True, blank=True)
    webm = models.FileField(upload_to = 'videos/webm', null=True, blank=True)
    poster = models.FileField(upload_to = 'videos/poster',blank=True)

    class Meta:
        verbose_name = u'video Evento'
        verbose_name_plural = u'Videos Eventos'

    @property
    def mp4_url(self):
        if self.mp4:
            return getattr(self.mp4, 'url', None)
        return None
    @property
    def webm_url(self):
        if self.webm:
            return getattr(self.webm, 'url', None)
        return None
    @property
    def poster_url(self):
        if self.poster:
            return getattr(self.poster, 'url', None)
        return None

class Post(models.Model):
    photo = models.ManyToManyField(File, related_name='extendeds')
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=250)
    video = models.ForeignKey(Video,related_name='vid', null=True, blank=True, on_delete=models.SET_NULL)
    description = models.TextField()
    image = models.FileField(upload_to = 'images/',blank=False)
    download = models.ForeignKey(URL,related_name='urls', null=True, blank=True, on_delete=models.SET_NULL)
    

    class Meta:
        verbose_name = u'Publicacion'
        verbose_name_plural = u'Publicaciones'

    def __str__(self):
        return self.gallery.title
    def __str__(self):
        return self.title
   
    @property
    def image_url(self):
        if self.image:
            return getattr(self.image, 'url', None)
        return None


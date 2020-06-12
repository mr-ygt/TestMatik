from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from ckeditor.fields import RichTextField


# Create your models here.
class Soru(models.Model):
    user = models.ForeignKey('auth.User', verbose_name='HOCA', related_name='sorular')

    sınıf = models.IntegerField()
    ders = models.CharField(max_length=100)
    konu = models.CharField(max_length=100)
    zorluk = models.IntegerField()

    image = models.ImageField()
    slug = models.SlugField(unique=True, editable=False, max_length=130)
    testid = models.CharField(null=True, blank=True, max_length=100)

    def set_quittest_url(self):
        return reverse('soru:quittest', kwargs={'slug': self.slug})

    def __str__(self):
        return self.ders

    def pdf_acma(self):
        return reverse('soru:pdf')

    def set_testid_url(self):
        return reverse('soru:settest', kwargs={'slug': self.slug})

    def get_absolute_url(self):
        return reverse('soru:detail', kwargs={'slug': self.slug})
        # return "/soru/{}".format(self.id)

    def get_create_url(self):
        return reverse('soru:create')

    def get_update_url(self):
        return reverse('soru:update', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('soru:delete', kwargs={'slug': self.slug})

    def get_unique_slug(self):
        slug = slugify(self.ders.replace('ı', 'i'))
        unique_slug = slug
        counter = 1
        while Soru.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, counter)
            counter += 1
        return unique_slug

    def save(self, *args, **kwargs):
        self.slug = self.get_unique_slug()
        return super(Soru, self).save(*args, **kwargs)

    class Meta:
        ordering = ['id']
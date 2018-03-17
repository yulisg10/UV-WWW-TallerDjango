from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.
class Entrada(models.Model):
	"""docstring for Entrada"""
	titulo = models.CharField(max_length=200)
	contenido = models.TextField()
	slug = models.SlugField(editable=False)

	def __unicode__(self):
		return self.titulo

	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = slugify(self.titulo)
		super(Entrada, self).save(*args, **kwargs)
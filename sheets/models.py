from django.db import models
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string


class Sheet(models.Model):
	objects = models.Manager()

	name = models.CharField(max_length=256)
	key = models.SlugField(max_length=56, unique=True, blank=True)
	owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sheets')

	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name

	def save(self, *args, **kwargs):
		self.key = get_random_string(length=56)
		return super(Sheet, self).save(*args, **kwargs)

	def get_absolute_url(self):
		return reverse('sheet:view', args=[self.key])

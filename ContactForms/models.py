from django.db import models

class ContactNumber(models.Model):
	type = models.CharField(max_length = 24)
	contact = models.IntegerField()


class ContactEmail(models.Model):
	type = models.CharField(max_length = 24)
	contact = models.EmailField(max_length = 254)

	def __str__(self):
		return f"{self.contact}"
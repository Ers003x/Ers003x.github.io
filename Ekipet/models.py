from django.db import models



class Trainer(models.Model):
	profile = models.ImageField(default = 'default.jpg', upload_to = 'trainers_profile')
	first = models.CharField(max_length = 32)
	last = models.CharField(max_length = 32)

	description = models.TextField(default = '')


	def __str__(self):
		return f"{self.first} {self.last}"


class Grupmoshat(models.Model):
	fillim = models.IntegerField()
	mbarim = models.IntegerField()

	def __str__(self):
		return f"Ekipi U-{self.mbarim}"







class Ekipet(models.Model):
	image = models.ImageField(default = 'default.jpg', upload_to = 'team_pics')
	category = models.OneToOneField(Grupmoshat, on_delete = models.CASCADE,related_name = "team")
	description = models.TextField()
	trainers = models.ManyToManyField(Trainer,default = None, related_name = 'profesor')


	def __str__(self):
		return f"Ekipi i {self.category}"



from django.db import models
from django.utils import timezone
from django.template.defaultfilters import slugify


class Entry(models.Model):
	title = models.CharField(max_length = 200)
	description = models.TextField()



class Category(models.Model):
	type = models.CharField(max_length = 64)
	def __str__(self):
		return f"{self.type}"




class Post(models.Model):
	title = models.CharField(max_length = 128)
	image = models.ImageField(default = 'default.jpg', upload_to = 'post_pics')
	content = models.TextField()
	date_posted = models.DateTimeField(default = timezone.now)
	category = models.ForeignKey(Category, on_delete = models.CASCADE)

	def __str__(self):
		return f"{self.title} - {self.category}"


def get_image_filename(instance, filename):
	title = instance.post.title 
	slug = slugify(title)
	return "post_images/%s-%s" % (slug, filename)


class Images(models.Model):
	post = models.ForeignKey(Post, default= None, on_delete = models.CASCADE)
	image  = models.ImageField( upload_to = get_image_filename, verbose_name = 'Images')

	def __str__(self):
		return f"imazh per {self.post}"


class FrontSlider(models.Model):
	title = models.CharField(default = None, max_length = 32)
	content = models.CharField(max_length= 128)
	slide = models.ImageField(upload_to = 'slide_pics')
	rendesia = models.IntegerField()

	def __str__(self):
		return f"Postim per : {self.title}"

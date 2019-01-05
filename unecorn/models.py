from django.db import models


class Category(models.Model):
	"""Category for discounts"""
	name = models.CharField(max_length=200)

	class Meta:
		verbose_name_plural = 'categories'

		
	def __str__(self):
		return self.name

class Company(models.Model):
	"""

	Меня Настя заставляет писать комментарии, помогите

	P.S. Класс реализует абстракцию для компаний

	"""
	name = models.CharField(max_length=200)
	url = models.CharField(max_length=200)	
	class Meta:
		verbose_name_plural = 'companies'

	def __str__(self):
		return self.name

class Discount(models.Model):
	"""Discount for students"""
	name = models.CharField(max_length=200)
	text = models.TextField()
	pub_date = models.DateTimeField()
	end_date = models.DateTimeField()
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	company = models.ForeignKey(Company, on_delete=models.CASCADE)

	def __str__(self):
		return self.name
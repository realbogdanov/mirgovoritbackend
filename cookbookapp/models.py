from django.db import models


class Product(models.Model):
	"""Класс предоставляющий продукт с названием и кол-вом раз когда он был использован в рецепте"""
	name = models.CharField(max_length=200)
	count_used = models.IntegerField(default=0)

	def __str__(self):
		return self.name  # Отображение название продуктов в рецепте.


class Recipe(models.Model):
	"""Класс представляющий рецепт с названием и набором продуктов, используемых в рецепте"""
	name = models.CharField(max_length=200)
	products = models.ManyToManyField(Product, through='RecipeProduct')


class RecipeProduct(models.Model):
	"""Класс представляющий связь между рецептом и продуктом, включая вес продукта в рецепте"""
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
	weight = models.IntegerField()

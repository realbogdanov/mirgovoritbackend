from django.contrib import admin
from .models import Product, Recipe, RecipeProduct


class RecipeProductInline(admin.TabularInline):
	"""
	Класс, который связывает модель RecipeProduct с АП Django.
	Это позволяет отображать и редактировать объекты RecipeProduct
	внутри связанных объектов Recipe на странице администратора.
	"""
	model = RecipeProduct
	extra = 1  # Кол-во дополнительных форм которые будут отображаться на страницу администратора.


class ProductAdmin(admin.ModelAdmin):
	"""
	Класс, который связывает модель Product с АП Django.
	Он определяет, какие поля модели Product будут отображаться на странице администратора.
	"""
	list_display = ['name', 'count_used']  # Поля, которые будут отображаться в списке объектов Product


class RecipeAdmin(admin.ModelAdmin):
	"""
	Класс, который связывает модель Recipe с АП Django.
	Он определяет, какие поля модели Recipe будут отображаться на странице администратора,
	а также включает в себя RecipeProductInline для отображения связанных объектов RecipeProduct.
	"""
	inlines = [RecipeProductInline, ]  # Список классов InLineModelAdmin, которые должны быть отображены на АП
	list_display = ['name', ]  # Поля, которые будут отображаться в списке объектов Recipe


# Регистрация моделей и их административных классов в АП Django
admin.site.register(Product, ProductAdmin)
admin.site.register(Recipe, RecipeAdmin)

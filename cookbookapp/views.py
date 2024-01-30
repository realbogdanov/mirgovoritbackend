from django.views.generic import ListView, UpdateView

from .models import Product, Recipe, RecipeProduct


class AddProductToRecipeView(UpdateView):
	"""Класс, который добавляет к указанному рецепту указанный продукт с указанным весом"""
	model = RecipeProduct
	fields = ['weight']


class CookRecipeView(UpdateView):
	"""Класс, который увеличивает на единицу кол-во приготовленных блюд для каждого продукта, входящего в рецепт"""
	model = Recipe
	fields = ['products']

	def form_valid(self, form):
		"""
		Переопределённый метод, который вызывается, когда пользователь отправляет действительную форму.
		Увеличивает на единицу кол-во приготовленных блюд для каждого продукта, входящего в рецепт.
		:param
			form (Form): Форма, которую отправил пользователю
		:return:
			Response (HttpResponse): Ответ HTTP, который будет отправлен пользователю.

		P.s. Не могу разобраться почему не увеличивается счётчик!
		"""
		response = super().form_valid(form)
		recipe = self.object

		for recipe_product in recipe.recipeproduct_set.all():
			product = recipe_product.product
			product.count_used += 1
			product.save()

		return response


class ShowRecipesWithoutProductView(ListView):
	"""Класс, который возвращает HTML страницу, на которой размещена таблица."""
	model = Recipe
	template_name = 'cookbookapp/recipes.html'

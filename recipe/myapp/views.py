from django.shortcuts import render

# Sample data
recipes = [
    {'id': 1, 'name': 'Spaghetti Carbonara', 'description': 'A classic Italian pasta dish.'},
    {'id': 2, 'name': 'Chicken Curry', 'description': 'A spicy and flavorful dish.'},
    {'id': 3, 'name': 'Chocolate Brownies', 'description': 'A sweet and decadent dessert.'},
    {'id': 4, 'name': 'Vegetable Stir-Fry', 'description': 'A healthy and colorful dish.'},
    {'id': 5, 'name': 'Tacos', 'description': 'A Mexican dish with seasoned fish.'},
    {'id': 6, 'name': 'Pumpkin Soup', 'description': 'A creamy and comforting soup.'},
    {'id': 7, 'name': 'Apple Pie', 'description': 'A classic American dessert.'},
    {'id': 8, 'name': 'Shrimp Scampi', 'description': 'A flavorful seafood dish.'},
    {'id': 9, 'name': 'Mushroom Risotto', 'description': 'A creamy and savory rice dish.'},
    {'id': 10, 'name': 'Banana Bread', 'description': 'A moist and delicious bread.'},
]

def recipe_list(request):
    return render(request, 'recipe_list.html', {'recipes': recipes})

def recipe_detail(request, recipe_id):
    recipe = next((recipe for recipe in recipes if recipe['id'] == recipe_id), None)
    return render(request, 'recipe_detail.html', {'recipe': recipe})

def user_profile(request, recipe_id):
    recipe = next((recipe for recipe in recipes if recipe['id'] == recipe_id), None)
    return render(request, 'user_profile.html', {'recipe': recipe})
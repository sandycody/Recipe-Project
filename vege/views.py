from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
# Create your views here.


def recipes(request):
    if request.method == "POST":    
        data = request.POST;
        recipe_name = data.get('Recipe_Name');
        recipe_description = data.get('Recipe_Description');
        recipe_image = request.FILES.get('Recipe_Image');

        # print(recipe_name);
        # print(recipe_description);
        # print(recipe_image);

        Recipe.objects.create(
            recipe_name = recipe_name, 
            recipe_description = recipe_description, 
            recipe_image = recipe_image
        )

        return redirect('/recipes/')
    
    querySet = Recipe.objects.all();

    if request.GET.get('search'):
        print(request.GET.get('search'));
        querySet = querySet.filter(recipe_name__icontains = request.GET.get('search'));
   
    return render(request, 'recipes.html', context = {'page' : 'Food Recipes', 'recipes' : querySet});

def deleteRecipe(request, id):
    querySet = Recipe.objects.get(id = id);
    querySet.delete();
    return redirect('/recipes/');

def updateRecipe(request, id):
    querySet = Recipe.objects.get(id = id);

    if request.method == "POST" :
        data = request.POST;
        recipe_name = data.get('Recipe_Name');
        recipe_description = data.get('Recipe_Description');
        recipe_image = request.FILES.get('Recipe_Image');
    
        querySet.recipe_name = recipe_name;
        querySet.recipe_description = recipe_description;
        
        if recipe_image:
            querySet.recipe_image = recipe_image;
    
        querySet.save();
        return redirect('/recipes/');
    
    return render(request, 'update_recipes.html', context={'recipe' : querySet});

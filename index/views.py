from django.shortcuts import render
from .models import Product, Category, Cart
import random

messi_images = [
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQe82d1P7W7j0Dgnx0bVmy-ICZ_HAKKkqiYiQ&s',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRHRVNuogny_0nPUImPpRZd0Za9UydMvgfvkw&s',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQjFkwsHvp6ICnlBedLNCIqlnS1-dKQ_qQdBA&s',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSyQcMTKnSzsLthPuZp0JQY0Hb4m0tilABZ-w&s',
    'https://www.anhnghethuatdulich.com/wp-content/uploads/2025/08/messi-meme-face-khac-hoa-chan-thuc-bieu-cam-kho-quen-cua-sieu-sao-argentina.jpg',
    'https://i.pinimg.com/originals/12/98/0f/12980f9b45cf3660e848ca2b70f29621.jpg',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSWjkYQqGOk7al4vzW5g9FpPizmggJa9hhpXg&s',
    'https://tomauchotre.com/wp-content/uploads/2025/10/messi-meme-22.jpg',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSPr9Iz0_QNBBkrbDCL41GEjjbOvhuNcqoNPQ&s'
]

# Create your views here.
# Главная страница
def home_page(request):
    # Достаем данные из БД
    categories = Category.objects.all()
    products = Product.objects.all()
    # Передаем данные на фронт
    context = {
        'products': products,
        'categories': categories,
        'image': random.choice(messi_images)
    }
    return render(request, 'home.html', context)

# Страница с категорией
def category_page(request, pk):
    # Достаем данные из БД
    category = Category.objects.get(id=pk)
    products = Product.objects.filter(product_category=category)
    # Передаем данные на фронт
    context = {
        'category': category,
        'products': products,
        'image': random.choice(messi_images)
    }
    return render(request, 'category.html', context)

# Страница с товаром
def product_page(request, pk):
    # Достаем данные из БД
    product = Product.objects.get(id=pk)
    # Передаем данные на фронт
    context = {
        'product': product,
        'image': random.choice(messi_images)
    }
    return render(request, 'product.html', context)

# Поиск товара по названию
def search(request):
    if request.method == 'POST':
        # Достаем данные с формы
        searched_product = request.POST.get('search-product')
        # Достаем данные из БД
        get_product = Product.objects.filter(product_name__iregex=searched_product)
        # Передаем данные на фронт
        context = {}
        if get_product:
            context.update(user_pr=searched_product, products=get_product, image=random.choice(messi_images))
        else:
            context.update(user_pr=searched_product, products='', image=random.choice(messi_images))
        return render(request, 'result.html', context)
    
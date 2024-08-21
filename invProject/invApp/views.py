from django.shortcuts import render, redirect
from .forms import ProductForm
from .models import Product

#  home page 
def home_view(request):
    return render(request, "invApp/home.html")

# products page 
def product_list_view(request):
    products_list  = Product.objects.all()
    return render(request, "invApp/product_list.html", {"products": products_list})

#  create product 
def create_product(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
        else:
            print(form.errors)  # Print form errors to the console or log them
    return render(request, "invApp/product_form.html", {'form': form})


# delete product in product list 
def delelte_view(request, product_id):
    products = Product.objects.get(product_id = product_id)
    if( request.method == 'POST'):
        products.delete()
        return redirect('product_list')
    return render(request, 'invApp/confirm_delete.html', {"product": products})

# update view for products 
def update_view(request, product_id):
    product = Product.objects.get(product_id=product_id)
    form = ProductForm()
    if(request.method == "POST"):
        form = ProductForm(request.POST, instance=product)
        if (form.is_valid):
            form.save()
            return redirect("product_list")
    return render(request, 'invApp/product_form.html', {'form':form}) 



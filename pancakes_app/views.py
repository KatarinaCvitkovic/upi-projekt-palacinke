from django.shortcuts import render,redirect
from .models import Category, Product
from .forms import CategoryForm, ProductForm
from django.contrib import messages
from django.http import HttpResponseRedirect

#home
def home(request):
    price = ""
    categories = Category.objects.all
    products = Product.objects.filter(is_enable=True)
    request.session['home_flag'] = 1
    # price order
    if request.method == 'POST':
        price = request.POST.get("price", "")
        request.session['price'] = price        # store the price to session
        if price == "lowest":                   # when clicking the price lowest item on the selectbox
            products = Product.objects.filter(is_enable=True).order_by('price')
        elif price == "highest":                # when clicking the price highest item on the selectbox
            products = Product.objects.filter(is_enable=True).order_by('-price')
        else:                                   # when clicking Featured item on the selectbox
            products = Product.objects.filter(is_enable=True)

    return render(request, 'list.html', {'products': products, 'categories': categories, 'price': price})


#List
def list(request):
    categories = Category.objects.all
    home_flag = request.session.get('home_flag')
    categ_id = request.session.get('categ_id')  # get categ_id from session
    products = Product.objects.filter(category_id = categ_id)
    price = ""

    # price order
    if request.method == 'POST':
        price = request.POST.get("price", "")
        request.session['price'] = price        # store the price to session
        if price == "lowest":                   # when clicking the price lowest item on the selectbox
            if home_flag == 1:
                products = Product.objects.filter(is_enable=True).order_by('price')
            else:
                products = Product.objects.filter(is_enable=True, category_id=categ_id).order_by('price')
        elif price == "highest":                # when clicking the price highest item on the selectbox
            if home_flag == 1:
                products = Product.objects.filter(is_enable=True).order_by('-price')
            else:
                products = Product.objects.filter(is_enable=True, category_id=categ_id).order_by('-price')
        else:
            if home_flag == 1:                  # when clicking Featured item on the selectbox
                products = Product.objects.filter(is_enable=True)
            else:
                products = Product.objects.filter(is_enable=True, category_id=categ_id)

    return render(request, 'list.html', {'products': products, 'categories': categories, 'price': price})


# when clicking the category
def listbycateg(request, categ_name):
    categ = Category.objects.get(name=categ_name)
    request.session['home_flag'] = 0
    request.session['categ_id'] = categ.id       # Store a selected category to session.
    categories = Category.objects.all            # Get all categories from database.
    products = Product.objects.filter(category_id = categ.id)
    price = request.session.get('price')         # Get price order from session

    if price == "lowest":                        # lowest price
        products = Product.objects.filter(category_id = categ.id).order_by('price')
    elif price == "highest":                     # hightest price
        products = Product.objects.filter(category_id = categ.id).order_by('-price')

    # Rendering the list page.
    return render(request, 'list.html', {'products': products, 'categories': categories, 'cate_name': categ_name, 'price': price})



#Edit
def edit(request, id):
    if request.method == 'POST':               # When clicking the save button on <Edit form>
        product = Product.objects.get(pk=id)
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()                        # If the form is valid, save
            messages.success(request, ('Product has been saved!'))
            return redirect('home')            # After saving, redirect to list page.
        else:
            messages.success(request, ('You must input correct data.'))
    else:                                      # When clicking the edit button on list page
        product = Product.objects.get(pk=id)   # Get a specific item info from db
        form = ProductForm(instance=product)   # Set the data to product form
    return render(request, 'add-edit.html', {'form': form, 'action': 'edit'})  # render the add-edit.html


#Add
def add(request):
    if request.method == 'POST':               # When clicking the add button on <Add product> form
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():                    # If the form is valid, Add
            form.save()
            messages.success(request, ('Product has been created!'))
            return redirect('home')            # After saving, redirect to list page.
        else :
            messages.success(request, ('You must input correct data.'))
    else:
        form = ProductForm()                   # When clicking the Add button on Homepage, show a blank product form.
    return render(request, 'add-edit.html', { 'form': form }) # Rendering the add-edit.html


#Delete
def delete(request, id):
    product = Product.objects.get(pk=id)       # Get a specific product with id
    product.delete()                           # Delete
    messages.success(request, ('Product Has Been Deleted!'))
    return redirect('home')                    # After deleting, redirect to list page.


#About
def about(request):
    return render(request, 'about.html', {})   # Rendering the about.html


#Contact Us
def contactus(request):
    return render(request, 'contactus.html', {})   # Rendering the contactus.html

from django import forms
from .models import Category, Product

#Django provides a helper class that lets you create a Form class from a Django model.
#The generated Form class will have a form field for every model field specified, in the order specified in the fields attribute.


#Category Form
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields= ["name"]

#Product Form
class ProductForm(forms.ModelForm):
    image = forms.ImageField(required=False, widget=forms.FileInput(attrs={'class': 'addImageButton'}), label="Slika")
    class Meta:
        model = Product
        fields= ["name", "category", "price", "description", "image"]
        labels = {
            'name': 'Ime',
            'category': 'Kategorija',
            'price': 'Cijena',
            'description': 'Opis',
        }

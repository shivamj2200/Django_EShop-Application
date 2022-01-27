from itertools import product
from django.shortcuts import redirect, render
from polls.models.product import Product
from polls.models.category import Category
from django.views import View



class Index(View): 
    def post(self, request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        # print (product)
        cart = request.session.get('cart') 
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity-1
                        
                    
                else:
                    cart[product] = quantity+1
                
               
            else:
                
                cart[product] = 1
            
        else:
            cart = {}
            cart[product] = 1 
       
        request.session['cart'] = cart
        print(request.session['cart'])
        return redirect('homepage')
    
    def get(self, request):
        cart=request.session.get('cart')
        if not cart:
            request.session['cart'] = {}
        products = None
        print(products)
        categories = Category.get_all_categories()
        categoryID = request.GET.get('category')
        if categoryID:
            products = Product.get_all_products_by_categoryid(categoryID)
        else:
            products = Product.get_all_products();
        data = {}
        data['products'] = products
        data['categories']= categories
        print('you are : ' , request.session.get('email'))
        return render(request , 'index.html' , data)

  
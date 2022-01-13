from django.shortcuts import render
from . models import *
# Create your views here.
def index(request):


    # products = Product.objects.all()
    # # this method takes more time to process


    products = Product.objects.all().select_related('book','cupboard') 
    # this method takes less time to process 


    # products = Product.objects.all().prefetch_related('book','cupboard') 
    # # this method not better than the above one to process
    

    # book = Book.objects.all()
    # cupboard = Cupboard.objects.all()
    # products = cupboard.union(book)
    # #this method takes a much time to process

    context = {
      'products': products
    }
    return render(request, 'store.html', context=context)
from django.shortcuts import render,redirect
from .models import*
from .forms import*

# Create your views here.
def homepage(request):
    # return render(request,'book.html')
    books = Books.objects.all()
    return render(request,'books.html',{'books':books})

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = BookForm()
        return render(request,'add_book.html',{'form':form})
    
def delete_book(request,book_id):
    book = Books.objects.get(id=book_id)
    if book:
        book.delete()
    return redirect('homepage')

from django.shortcuts import render ,get_list_or_404,redirect
from .models import Books
from .forms import BookForms

def BookList(request):
    books = Books.objects.all()
    print(books)
    return render(request,'book_list.html',{'books':books})

def book_create(request):
    if request.method == 'POST':
        form = BookForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bookList')
    else:
        form = BookForms()
    return render(request, 'book_form.html', {'form': form})


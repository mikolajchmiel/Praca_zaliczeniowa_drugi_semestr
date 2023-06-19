from django.shortcuts import render, get_object_or_404
from .forms import BookForm
from django.shortcuts import render, get_object_or_404
from .forms import BookForm
from .models import Book

def book_detail_view(request, id):
    book = get_object_or_404(Book, id=id)
    form = BookForm(instance=book)
    return render(request, 'book_detail.html', {'form': form})






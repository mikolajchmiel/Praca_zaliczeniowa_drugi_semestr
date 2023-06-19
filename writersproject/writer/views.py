from django.shortcuts import render, get_object_or_404
from .forms import WriterForm
from .models import Writer


# Create your views here.

def writer_detail_view(request, id):
    writer = get_object_or_404(Writer, id=id)
    form = WriterForm(instance=writer)
    return render(request, 'Writer_detail.html', {'form': form})



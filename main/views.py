from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import MessageForm


def index(request):
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('success_page'))
        else:
            context = {'form': form}
            return render(request, 'index.html', context)
    else:
        form = MessageForm()
        context = {'form': form}
        return render(request, 'index.html', context)


def success_page(request):
    message = 'Сообщение успешно отправлено'
    return render(request, 'success_page.html', {"message": message})

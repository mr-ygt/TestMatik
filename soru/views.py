from django.shortcuts import render, HttpResponse, get_object_or_404, HttpResponseRedirect, redirect
from .models import Soru
from .forms import SoruForm
from django.contrib import messages
from django.utils.text import slugify
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q


# Create your views here.

def soru_index(request):
    soru_list = Soru.objects.all()
    query = request.GET.get('q')
    if query:
        soru_list = soru_list.filter(
            Q(konu__icontains=query) |
            Q(ders__icontains=query) |
            Q(sınıf__icontains=query)
        ).distinct()
    paginator = Paginator(soru_list, 5)  # Show 25 contacts per page

    page = request.GET.get('sayfa')
    try:
        sorular = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        sorular = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        sorular = paginator.page(paginator.num_pages)

    return render(request, 'soru/index.html', {'sorular': sorular})


def soru_detail(request, slug):
    soru = get_object_or_404(Soru, slug=slug)
    context = {
        'soru': soru,
    }
    return render(request, 'soru/detail.html', context)


def soru_create(request):
    form = SoruForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        soru = form.save(commit=False)
        soru.user = request.user
        soru.save()
        messages.success(request, 'afferin oldu')
        return HttpResponseRedirect(soru.get_absolute_url())
    context = {
        'form': form,
    }

    return render(request, 'soru/form.html', context)


def soru_update(request, slug):
    soru = get_object_or_404(Soru, slug=slug)
    form = SoruForm(request.POST or None, request.FILES or None, instance=soru)
    if form.is_valid():
        form.save()
        messages.success(request, 'afferin oldu', extra_tags='efferin')
        return HttpResponseRedirect(soru.get_absolute_url())
    context = {
        'form': form,
    }

    return render(request, 'soru/form.html', context)


def soru_delete(request, slug):
    soru = get_object_or_404(Soru, slug=slug)
    soru.delete()

    return redirect('soru:index')

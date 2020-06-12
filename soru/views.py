from django.shortcuts import render, HttpResponse, get_object_or_404, HttpResponseRedirect, redirect
from .models import Soru
from .forms import SoruForm
from django.contrib import messages
from django.utils.text import slugify
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.http import HttpResponse
from django.views.generic import View
from django.template.loader import get_template

from .utils import render_to_pdf

# Create your views here.

def soru_index(request):
    soru_list = Soru.objects.all()
    query = request.GET.get('q')
    if query:
        soru_list = soru_list.filter(
            Q(user__username__icontains=query)
        ).distinct()


    zorlukquery = request.GET.get('w')
    dersquery = request.GET.get('e')
    sinifquery = request.GET.get('r')
    konuquery = request.GET.get('t')
    if zorlukquery or dersquery or sinifquery or konuquery:
        soru_list = soru_list.filter(
            Q(zorluk__icontains=zorlukquery) &
            Q(ders__icontains=dersquery) &
            Q(sınıf__icontains=sinifquery) &
            Q(konu__icontains=konuquery)
        ).distinct()
    paginator = Paginator(soru_list, 99)  # Show 25 contacts per page

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

def soru_settest(request, slug):
    soru = get_object_or_404(Soru, slug=slug)
    soru.testid = 1
    soru.save()
    return redirect('soru:index')

def soru_testindex(request):
    soru_list = Soru.objects.filter(testid__contains=1)
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

    return render(request, 'testindex.html', {'sorular': sorular})



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


class GeneratePdf(View):
    def get(self, request, *args, **kwargs):
        soru_list = Soru.objects.filter(testid__contains=1)
        template = get_template('pdf.html')
        data = {
            'sorular': soru_list,
            'amount': 39.99,
            'customer_name': 'Cooper Mann',
            'order_id': 1233434,
        }
        html = template.render(data)
        pdf = render_to_pdf('pdf.html', data)
        if pdf:
            return HttpResponse(pdf, content_type='application/pdf')
        return HttpResponse("Not Found")
from lzma import is_check_supported
from django.shortcuts import render

from .models import Magazine


def publications(request):
    # TODO get request.GET params
    publications = Magazine.objects.filter(status='p')
    if vol := request.GET.get('vol'):
        publications = publications.filter(volume=vol)
    if iss := request.GET.get('iss'):
        publications = publications.filter(issue=iss)
    if year := request.GET.get('year'):
        publications = publications.filter(publication_date__year=year)

    return render(
        request,
        'magazine/publications.html',
        {
            'publications': publications,
            'volume': vol,
            'issue': iss,
            'publication_year': year,
        }
    )


def publication_detail(request, pk):
    publication = Magazine.objects.get(pk=pk)
    return render(
        request,
        'magazine/publication_detail.html',
        {'publication': publication}
    )


def reader(request, pk):
    publication = Magazine.objects.get(pk=pk)
    return render(
        request,
        'magazine/reader.html',
        {'publication': publication}
    )

from django.shortcuts import render
from django.core.exceptions import PermissionDenied

from .models import Magazine


def publications(request):
    # TODO get request.GET params
    publications = Magazine.objects.filter(status__in=['p', 'w'])
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
    if publication.status == 'w':
        raise PermissionDenied
    return render(
        request,
        'magazine/publication_detail.html',
        {'publication': publication}
    )


def reader(request, pk):
    publication = Magazine.objects.get(pk=pk)
    if publication.status == 'w':
        raise PermissionDenied
    return render(
        request,
        'magazine/reader.html',
        {'publication': publication}
    )

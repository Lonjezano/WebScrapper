
from django.shortcuts import render
from django.views.generic import MonthArchiveView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Contact, ScrappedData, ScrappedVacancy, ScrappedTender, ScrappedAdvert, ScrappedNew


def index(request):
    vacancy_list = ScrappedData.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(vacancy_list, 5)
    try:
        jobs = paginator.page(page)
    except PageNotAnInteger:
        jobs = paginator.page(1)
    except EmptyPage:
        jobs = paginator.page(paginator.num_pages)

    return render(request, 'vacancyapp/index.html', {'jobs': jobs})


def vacancy(request):
    vacancy_list = ScrappedVacancy.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(vacancy_list, 5)
    try:
        vacancies = paginator.page(page)
    except PageNotAnInteger:
        vacancies = paginator.page(1)
    except EmptyPage:
        vacancies = paginator.page(paginator.num_pages)
    return render(request, 'vacancyapp/vacancy.html', {'vacancies': vacancies})


def date(request, date):
    tenders = ScrappedTender.objects.filter(date__range=["2021-04-05", "2011-04-06"])
    return render(request, 'vacancyapp/tender_sorted.html', {'date': date, tenders: 'tenders'})


def news(request):
    news_list = ScrappedNew.objects.all().order_by('-scrapped_date')
    page = request.GET.get('page', 1)
    paginator = Paginator(news_list, 5)
    try:
        news = paginator.page(page)
    except PageNotAnInteger:
        news = paginator.page(1)
    except EmptyPage:
        news = paginator.page(paginator.num_pages)
    return render(request, 'vacancyapp/news.html', {'news': news})

def tender(request):
    tender_list = ScrappedTender.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(tender_list, 5)
    try:
        tenders = paginator.page(page)
    except PageNotAnInteger:
        tenders = paginator.page(1)
    except EmptyPage:
        tenders = paginator.page(paginator.num_pages)
    return render(request, 'vacancyapp/tender.html', {'tenders': tenders})


def advert(request):
    advert_list = ScrappedAdvert.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(advert_list, 10)
    try:
        adverts = paginator.page(page)
    except PageNotAnInteger:
        adverts = paginator.page(1)
    except EmptyPage:
        adverts = paginator.page(paginator.num_pages)
    return render(request, 'vacancyapp/advert.html', {'adverts': adverts})


def contact(request):
    if request.method == "POST":
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        c = Contact(email=email, subject=subject, message=message)
        c.save()

        return render(request, 'vacancyapp/contact.html')
    else:
        return render(request, 'vacancyapp/contact.html')

def search(request):
    if request.method == "POST":
        searched = request.POST['search']
        posts_list = ScrappedNew.objects.filter(title__contains=searched)
        page = request.GET.get('page', 1)
        paginator = Paginator(posts_list, 5)
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)
        return render(request, 'vacancyapp/search_result.html', {"searched": searched, "posts": posts})

    else:
        return render(request, 'vacancyapp/search_result.html')


class ArticleYearArchiveView(MonthArchiveView):
    queryset = ScrappedNew.objects.all()
    date_field = "scrapped_date"
    allow_future = True
    context_object_name = 'news'
    ordering = ['-scrapped_date']
    paginate_by = 4

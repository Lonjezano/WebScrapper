from django.contrib import admin
from .models import Student, Contact, VacancyList, ScrappedData, ScrappedVacancy, ScrappedTender, ScrappedAdvert, ScrappedNew

# Register your models here.

admin.site.register(Student)
admin.site.register(Contact)
admin.site.register(VacancyList)
admin.site.register(ScrappedData)
admin.site.register(ScrappedVacancy)
admin.site.register(ScrappedTender)
admin.site.register(ScrappedAdvert)
admin.site.register(ScrappedNew)


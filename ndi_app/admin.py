from django.contrib import admin
from .models import News, Design, Slider, Photos_for_Portfolio, Activity,\
    WorksInActivity, Number, MainSlide, DownloadFiles, ServicesOfExpertise
# Register your models here.


class PortfolioPhotoInLine(admin.TabularInline):
    model = Photos_for_Portfolio


class WorksInActivityInLine(admin.TabularInline):
    model = WorksInActivity


@admin.register(DownloadFiles)
class DownloadFilesAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


@admin.register(ServicesOfExpertise)
class AdminServicesOfExpertise(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


@admin.register(MainSlide)
class MainSlideAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


@admin.register(Number)
class NumberAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}
    list_display = ['name']
    search_fields = ['name']

    inlines = [WorksInActivityInLine]


@admin.register(WorksInActivity)
class WorksInActivityAdmin(admin.ModelAdmin):
    list_display = ['title', 'activity']
    search_fields = ['title']


@admin.register(Design)
class DesignAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

    inlines = [PortfolioPhotoInLine]


@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ['name', 'link']
    search_fields = ['name']


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created']
    list_filter = ['created']
    search_fields = ['title']


admin.site.register(Photos_for_Portfolio)

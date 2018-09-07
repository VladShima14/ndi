from django.db import models

# Create your models here.


class Slider(models.Model):
    name = models.CharField(max_length=50, db_index=True, verbose_name='Название слайда')
    text = models.CharField(max_length=500, blank=True, verbose_name='Текст слайда')
    image = models.ImageField(upload_to='images/slider/', verbose_name='Картинка слайдера')
    link = models.URLField()

    class Meta:
        ordering = ['name']
        verbose_name = 'Слайдер'
        verbose_name_plural = 'Слайды'

    def __str__(self):
        return self.name


class News(models.Model):
    title = models.CharField(max_length=200, db_index=True, verbose_name='Название новости')
    image = models.ImageField(upload_to='images/news/', verbose_name='Картинка новости')
    text = models.TextField(verbose_name='Текст для новости')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['id']
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return self.title


class Design(models.Model):
    name = models.CharField(max_length=200, db_index=True, verbose_name='Название пункта')
    text = models.TextField(max_length=500, verbose_name='Текст')

    class Meta:
        ordering = ['name']
        verbose_name = 'Вид Проектирования'
        verbose_name_plural = 'Виды Проектирования'

    def __str__(self):
        return self.name


class Photos_for_Portfolio(models.Model):
    design = models.ForeignKey(Design, related_name='design', verbose_name='Вид проектирования')
    name = models.CharField(max_length=50, db_index=True, verbose_name='Название подборки фоток')
    title = models.CharField(max_length=250, blank=True, verbose_name='Заголовок для фоток')
    images = models.ImageField(upload_to='images/portfolio/', verbose_name='фото для портфолио')

    class Meta:
        ordering = ['name']
        verbose_name = 'Фото Портфолио'
        verbose_name_plural = 'Фотки портфолио'

    def __str__(self):
        return self.name


class Number(models.Model):
    name = models.CharField(max_length=10, db_index=True, verbose_name='Номер')
    d_path = models.TextField()
    point_path = models.TextField()

    def __str__(self):
        return self.name


class Activity(models.Model):
    name = models.CharField(max_length=250, db_index=True, verbose_name='Название Деятельности')
    slug = models.SlugField(max_length=250, db_index=True)
    number = models.ForeignKey('Number', related_name="number", blank=True, verbose_name="Номер")

    def __str__(self):
        return self.name


class WorksInActivity(models.Model):
    activity = models.ForeignKey('Activity', related_name="activity", verbose_name="Деятельность")
    title = models.CharField(max_length=250, db_index=True, verbose_name="Название", blank=True, null=True)
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(upload_to='images/activity/', verbose_name='фото')

    def __str__(self):
        return self.title


class MainSlide(models.Model):
    name = models.CharField(max_length=250, db_index=True, verbose_name="Название слайда")
    image = models.ImageField(upload_to='images/mainslide/', verbose_name='фото')

    def __str__(self):
        return self.name


class DownloadFiles(models.Model):
    name = models.CharField(max_length=250, db_index=True, verbose_name="Название файла")
    file = models.FileField(verbose_name='Файл')
    activity = models.ForeignKey('Activity', related_name='download_file',
                                 blank=True, verbose_name='Файл для экспертизы', null=True)

    def __str__(self):
        return self.name


class ServicesOfExpertise(models.Model):
    name = models.CharField(max_length=500, db_index=True, verbose_name="Название вида экспертизы")
    activity = models.ForeignKey('Activity', related_name='service_of_activity',
                                 verbose_name='Услуга для экспертизы', null=True)

    def __str__(self):
        return self.name

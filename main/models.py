from django.db import models


class Message(models.Model):
    fio = models.CharField('ФИО', max_length=512)
    faculty = models.CharField("Институт", max_length=512)
    group = models.CharField('Группа', max_length=100)
    comment = models.TextField('Поздравление', max_length=500)
    media_link = models.CharField('Ссылка на файлы с поздравлением (по желанию)', max_length=2000, null=True, blank=True)

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'

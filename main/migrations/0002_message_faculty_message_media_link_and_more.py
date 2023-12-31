# Generated by Django 4.2.6 on 2023-11-08 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='faculty',
            field=models.CharField(default=1, max_length=512, verbose_name='Институт'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='message',
            name='media_link',
            field=models.CharField(blank=True, max_length=2000, null=True, verbose_name='Ссылка на файлы с поздравлением (по желанию)'),
        ),
        migrations.AlterField(
            model_name='message',
            name='comment',
            field=models.TextField(verbose_name='Поздравление'),
        ),
    ]

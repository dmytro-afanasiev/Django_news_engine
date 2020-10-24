# Generated by Django 3.1.1 on 2020-10-24 16:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=130, verbose_name='Автор')),
                ('title', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('description', models.TextField(help_text='Короткий фрагмент', verbose_name='Опис')),
                ('url', models.URLField(verbose_name='Посилання на ресурс')),
                ('url_to_image', models.URLField(verbose_name='Посилання на картинку')),
                ('published_at', models.DateTimeField(verbose_name='Дата публікації')),
                ('content', models.TextField(verbose_name='Контент')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='news', to='news.category')),
            ],
            options={
                'verbose_name': 'Новина',
                'verbose_name_plural': 'Новини',
                'ordering': ['-published_at'],
                'unique_together': {('title', 'published_at')},
            },
        ),
    ]

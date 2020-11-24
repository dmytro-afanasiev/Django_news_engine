# Generated by Django 3.1.1 on 2020-11-24 10:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth_system', '0008_auto_20201120_1556'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='Відгук')),
                ('published_at', models.DateTimeField(auto_now_add=True, verbose_name='Час, коли було отримано')),
                ('stars', models.IntegerField(verbose_name='Кількість зірок')),
                ('user_left', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Користувач, що залишив')),
            ],
            options={
                'verbose_name': 'Відгук',
                'verbose_name_plural': 'Відгуки',
            },
        ),
    ]
# Generated by Django 3.1.1 on 2020-10-12 15:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auth_system', '0002_user_categories'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='last_password_change',
            field=models.DateTimeField(default=django.utils.timezone.now, help_text='Дата і час, коли було останній раз змінено пароль, якщо не мінявся, то дата створення', verbose_name='Част останньої зміни паролю'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='send_news_to_email',
            field=models.BooleanField(default=False, help_text='Активуйте, якщо хочете отримувати новини на пошту', verbose_name='Надсилати новини на пошту'),
        ),
    ]

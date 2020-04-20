# Generated by Django 2.2.7 on 2020-02-13 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_title', models.CharField(max_length=200, verbose_name='Название поста')),
                ('post_text', models.TextField(verbose_name='Текст поста')),
                ('post_photo', models.ImageField(upload_to='', verbose_name='Главное изображение')),
                ('post_date', models.DateTimeField(auto_now=True, verbose_name='Дата публикации поста')),
                ('post_author', models.CharField(max_length=50, verbose_name='Автор')),
            ],
            options={
                'verbose_name': 'Пост',
                'verbose_name_plural': 'Посты',
            },
        ),
        migrations.AlterModelOptions(
            name='join_info',
            options={'verbose_name': 'Как зайти на сервер?', 'verbose_name_plural': 'Как зайти на сервер?'},
        ),
    ]

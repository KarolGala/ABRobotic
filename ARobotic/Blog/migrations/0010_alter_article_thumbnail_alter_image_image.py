# Generated by Django 4.1.7 on 2023-03-10 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0009_alter_article_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='thumbnail',
            field=models.ImageField(default=None, upload_to='Article'),
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(default=None, upload_to='Article'),
        ),
    ]

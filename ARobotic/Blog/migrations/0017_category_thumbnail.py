# Generated by Django 4.1.7 on 2023-03-28 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0016_tag_article_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='thumbnail',
            field=models.ImageField(default=None, upload_to='Category'),
        ),
    ]

# Generated by Django 4.1.7 on 2023-04-02 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0018_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='website',
            field=models.URLField(blank=True),
        ),
    ]

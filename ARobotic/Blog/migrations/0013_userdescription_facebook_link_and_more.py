# Generated by Django 4.1.7 on 2023-03-13 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0012_userdescription_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdescription',
            name='facebook_link',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='userdescription',
            name='instagram_link',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='userdescription',
            name='linkedin_link',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='userdescription',
            name='twitter_link',
            field=models.URLField(blank=True),
        ),
    ]
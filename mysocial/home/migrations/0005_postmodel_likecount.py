# Generated by Django 4.0.4 on 2022-05-15 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_comments_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='postmodel',
            name='likeCount',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]

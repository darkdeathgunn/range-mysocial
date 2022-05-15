# Generated by Django 4.0.4 on 2022-05-15 02:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0007_followmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='commentedPost',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.postmodel'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='commenter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
# Generated by Django 4.1.2 on 2022-11-18 14:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0011_auto_20221118_1420'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='tags_old',
        ),
        migrations.DeleteModel(
            name='ArticleTag',
        ),
    ]

# Generated by Django 3.2.8 on 2021-10-18 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newscomments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]

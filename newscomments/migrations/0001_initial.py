# Generated by Django 3.2.8 on 2021-10-18 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='ID', max_length=20)),
                ('content', models.TextField(help_text='comment')),
            ],
        ),
    ]

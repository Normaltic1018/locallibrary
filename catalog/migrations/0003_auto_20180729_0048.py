# Generated by Django 2.0.1 on 2018-07-29 00:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20180729_0008'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='language',
        ),
        migrations.DeleteModel(
            name='Language',
        ),
    ]

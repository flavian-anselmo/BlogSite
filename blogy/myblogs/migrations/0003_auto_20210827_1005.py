# Generated by Django 3.0.3 on 2021-08-27 10:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myblogs', '0002_auto_20210827_0909'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='catgoryName',
            new_name='categoryName',
        ),
    ]
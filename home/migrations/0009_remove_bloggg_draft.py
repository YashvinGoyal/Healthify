# Generated by Django 4.1 on 2023-06-25 12:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_alter_bloggg_draft'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bloggg',
            name='draft',
        ),
    ]
# Generated by Django 4.1 on 2023-06-20 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=10)),
                ('lname', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=20)),
                ('uname', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=20)),
                ('work', models.CharField(max_length=10)),
            ],
        ),
    ]
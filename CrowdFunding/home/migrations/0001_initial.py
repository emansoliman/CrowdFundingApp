# Generated by Django 3.1.7 on 2021-04-05 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=20)),
                ('Create_db', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

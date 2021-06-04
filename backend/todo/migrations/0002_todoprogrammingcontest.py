# Generated by Django 3.2.4 on 2021-06-04 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ToDoProgrammingContest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('platform', models.CharField(max_length=120)),
                ('staring_time', models.DateTimeField()),
                ('ending_time', models.DateTimeField()),
                ('description', models.CharField(max_length=120)),
                ('completed', models.BooleanField(default=False)),
            ],
        ),
    ]

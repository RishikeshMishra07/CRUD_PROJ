# Generated by Django 5.0.3 on 2024-03-20 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stuid', models.CharField(default='1', max_length=100)),
                ('stuname', models.CharField(max_length=200)),
                ('stuemail', models.EmailField(max_length=254)),
                ('stuage', models.IntegerField()),
            ],
        ),
    ]

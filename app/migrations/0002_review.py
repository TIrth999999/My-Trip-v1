# Generated by Django 5.0.1 on 2024-07-05 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='NULL', max_length=122)),
                ('city', models.CharField(default='NULL', max_length=122)),
                ('trip', models.CharField(default='NULL', max_length=10)),
                ('star', models.CharField(default='NULL', max_length=1000)),
                ('message', models.CharField(default='NULL', max_length=1000)),
            ],
        ),
    ]

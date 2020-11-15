# Generated by Django 3.1.2 on 2020-11-01 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('source_file', models.FileField(upload_to='uploads/')),
            ],
        ),
        migrations.CreateModel(
            name='Measure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modtime', models.DateField(auto_now=True)),
                ('content', models.TextField()),
                ('region', models.ManyToManyField(to='main.Region')),
            ],
        ),
    ]

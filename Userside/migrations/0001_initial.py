# Generated by Django 4.1.2 on 2023-01-07 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='reg_db',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(blank=True, max_length=25, null=True)),
                ('Email', models.EmailField(blank=True, max_length=100, null=True)),
                ('Password', models.TextField(blank=True, max_length=20, null=True)),
                ('C_Password', models.TextField(blank=True, max_length=20, null=True)),
            ],
        ),
    ]

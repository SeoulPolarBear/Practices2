# Generated by Django 3.2.16 on 2022-11-26 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fruit',
            fields=[
                ('f_no', models.IntegerField(primary_key=True, serialize=False)),
                ('f_name', models.CharField(max_length=10)),
                ('f_price', models.IntegerField()),
            ],
        ),
    ]
# Generated by Django 2.2.4 on 2020-07-13 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0006_сomplaint'),
    ]

    operations = [
        migrations.AlterField(
            model_name='сomplaint',
            name='text',
            field=models.TextField(verbose_name='Текст жалобы'),
        ),
    ]

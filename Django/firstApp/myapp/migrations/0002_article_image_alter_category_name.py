# Generated by Django 4.0.6 on 2022-07-16 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.ImageField(default='null', upload_to=''),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=110),
        ),
    ]

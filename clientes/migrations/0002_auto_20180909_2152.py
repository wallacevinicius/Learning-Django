# Generated by Django 2.1.1 on 2018-09-10 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='email',
            field=models.EmailField(default='a@a.com', max_length=254),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cliente',
            name='idade',
            field=models.IntegerField(),
        ),
    ]

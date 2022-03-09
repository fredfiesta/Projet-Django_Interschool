# Generated by Django 3.2.12 on 2022-03-09 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_interschool', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ['date']},
        ),
        migrations.RenameField(
            model_name='event',
            old_name='date_de_creation',
            new_name='date_creation',
        ),
        migrations.AddField(
            model_name='event',
            name='date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='event',
            name='lieu',
            field=models.CharField(blank=True, default='*pas de lieu déterminé', max_length=100),
        ),
        migrations.AlterField(
            model_name='event',
            name='titre',
            field=models.CharField(blank=True, default='*pas de titre déterminé', max_length=100),
        ),
    ]

# Generated by Django 4.1.2 on 2022-10-28 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_remove_onewire_onewire_addr'),
    ]

    operations = [
        migrations.AddField(
            model_name='onewire',
            name='onewire_channel',
            field=models.CharField(default='A', max_length=1, verbose_name='Канал'),
        ),
    ]

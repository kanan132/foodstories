# Generated by Django 3.1.2 on 2020-10-07 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0005_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='added_at',
            field=models.DateTimeField(auto_now_add=True, default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]

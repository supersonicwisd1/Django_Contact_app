# Generated by Django 4.0.3 on 2022-04-16 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_contact_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='gender',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=50),
        ),
    ]

# Generated by Django 4.2 on 2023-05-31 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='phone',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='student',
            name='age',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(max_length=50),
        ),
    ]
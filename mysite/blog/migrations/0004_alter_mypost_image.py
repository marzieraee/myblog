# Generated by Django 4.0.5 on 2022-06-08 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_mypost_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mypost',
            name='image',
            field=models.ImageField(default='media/defult.jpg', upload_to='media/'),
        ),
    ]

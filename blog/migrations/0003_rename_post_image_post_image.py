# Generated by Django 4.0.3 on 2022-04-13 10:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_post_post_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='post_image',
            new_name='image',
        ),
    ]

# Generated by Django 5.0.8 on 2024-09-02 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0009_alter_comment_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.CharField(max_length=100),
        ),
    ]

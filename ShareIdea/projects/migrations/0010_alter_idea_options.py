# Generated by Django 4.2.1 on 2023-06-04 18:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0009_alter_idea_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='idea',
            options={'ordering': ['-like', 'title', '-created']},
        ),
    ]

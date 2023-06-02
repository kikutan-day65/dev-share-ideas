# Generated by Django 4.2.1 on 2023-06-02 13:32

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_skill'),
        ('projects', '0006_alter_idea_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='idea',
            name='dislike',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('body', models.TextField(blank=True, null=True)),
                ('value', models.CharField(choices=[('like', 'like vote'), ('dislike', 'dislike vote')], max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('idea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.idea')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.profile')),
            ],
            options={
                'unique_together': {('owner', 'idea')},
            },
        ),
    ]

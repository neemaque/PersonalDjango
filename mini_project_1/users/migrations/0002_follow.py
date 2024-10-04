# Generated by Django 5.1.1 on 2024-09-30 15:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Follower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Follower', to='users.user')),
                ('Following', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Following', to='users.user')),
            ],
        ),
    ]

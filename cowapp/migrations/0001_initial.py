# Generated by Django 2.0.4 on 2018-04-21 03:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('number', models.TextField()),
                ('sex', models.TextField()),
                ('mother', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='children', to='cowapp.Cow')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cows', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]

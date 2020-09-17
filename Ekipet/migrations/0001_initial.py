# Generated by Django 3.0.5 on 2020-09-12 16:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Grupmoshat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fillim', models.IntegerField()),
                ('mbarim', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile', models.ImageField(default='default.jpg', upload_to='trainers_profile')),
                ('first', models.CharField(max_length=32)),
                ('last', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Ekipet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default.jpg', upload_to='team_pics')),
                ('description', models.TextField()),
                ('category', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='team', to='Ekipet.Grupmoshat')),
                ('trainers', models.ManyToManyField(related_name='team', to='Ekipet.Trainer')),
            ],
        ),
    ]

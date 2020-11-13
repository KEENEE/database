# Generated by Django 2.1.15 on 2020-11-13 10:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('ID', models.CharField(default='na', max_length=10)),
                ('PW', models.CharField(default='na', max_length=12)),
                ('birthdate', models.DateField(default=django.utils.timezone.now)),
                ('phone', models.CharField(default='01012343434', max_length=11)),
                ('address', models.CharField(default='na', max_length=100)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='na', max_length=6)),
                ('role', models.CharField(choices=[('A', 'Admin'), ('R', 'Rater'), ('S', 'Submitter')], default='na', max_length=10)),
            ],
        ),
    ]
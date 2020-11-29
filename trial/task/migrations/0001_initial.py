# Generated by Django 2.1.15 on 2020-11-29 03:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('my_admin', '0001_initial'),
        ('submitter', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplyTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('approved', models.IntegerField(default=0)),
                ('submitter', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='submitter.Submitter')),
            ],
            options={
                'db_table': 'apply_task',
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('task_id', models.AutoField(primary_key=True, serialize=False)),
                ('task_name', models.CharField(max_length=100, unique=True)),
                ('description', models.CharField(max_length=100)),
                ('mincycle', models.IntegerField()),
                ('admin', models.ForeignKey(db_column='admin', default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='my_admin.MyAdmin')),
            ],
            options={
                'db_table': 'task',
            },
        ),
        migrations.CreateModel(
            name='TaskDataTable',
            fields=[
                ('Name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('Scheme', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='applytask',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='task.Task'),
        ),
        migrations.AlterUniqueTogether(
            name='applytask',
            unique_together={('submitter', 'task')},
        ),
    ]

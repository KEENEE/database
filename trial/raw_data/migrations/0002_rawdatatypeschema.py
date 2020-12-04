# Generated by Django 2.1 on 2020-12-04 15:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('raw_data', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RawDataTypeSchema',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field_name', models.CharField(max_length=30)),
                ('field_type', models.CharField(choices=[('char', 'Char'), ('int', 'Int'), ('date', 'Date'), ('boolean', 'Boolean')], default='na', max_length=30)),
                ('null_value', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], default='na', max_length=10)),
                ('mapping_field', models.CharField(max_length=50)),
                ('type_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='raw_data.RawDataType')),
            ],
            options={
                'db_table': 'raw_data_type_schema',
            },
        ),
    ]

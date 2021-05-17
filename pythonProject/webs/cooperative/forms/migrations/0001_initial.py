# Generated by Django 3.2.1 on 2021-05-05 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AddWidget',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('widgetName', models.CharField(max_length=50)),
                ('widgetTitle', models.CharField(max_length=100)),
                ('uniqueCode', models.CharField(max_length=50)),
                ('status_id', models.IntegerField()),
                ('record_status', models.IntegerField()),
                ('created_by', models.IntegerField()),
                ('modified_by', models.IntegerField()),
                ('date_created', models.DateField()),
                ('time_created', models.TimeField()),
                ('date_modified', models.DateField()),
                ('time_modified', models.TimeField()),
            ],
            options={
                'db_table': 'user_widgets',
            },
        ),
    ]
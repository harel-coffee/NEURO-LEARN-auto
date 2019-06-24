# Generated by Django 2.1.7 on 2019-06-24 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0014_remove_data_demo_uploader'),
    ]

    operations = [
        migrations.CreateModel(
            name='Submissions_SA_Demo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_id', models.CharField(max_length=64, unique=True)),
                ('task_name', models.CharField(max_length=64)),
                ('task_type', models.CharField(max_length=64)),
                ('project_name', models.CharField(max_length=64)),
                ('test_var_data_x', models.CharField(max_length=1024)),
                ('group_var_data_y', models.CharField(max_length=1024)),
                ('note', models.CharField(max_length=64)),
                ('verbose', models.BooleanField()),
                ('task_status', models.CharField(max_length=64)),
                ('task_result', models.CharField(max_length=1024)),
            ],
        ),
        migrations.AlterField(
            model_name='data_demo',
            name='data_name',
            field=models.CharField(max_length=64, unique=True),
        ),
        migrations.AlterField(
            model_name='user_demo',
            name='user_id',
            field=models.CharField(max_length=64, unique=True),
        ),
    ]
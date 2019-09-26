# Generated by Django 2.2.5 on 2019-09-26 00:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='title')),
                ('partner', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, max_length=2000, null=True, verbose_name='description')),
                ('resolution', models.TextField(blank=True, max_length=2000, null=True, verbose_name='resolution')),
                ('deadline', models.DateField(blank=True, null=True, verbose_name='deadline')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_description', models.CharField(max_length=200, verbose_name='description')),
                ('is_done', models.BooleanField(default=False, verbose_name='done?')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taskapp.Task')),
            ],
            options={
                'verbose_name': 'Item',
                'verbose_name_plural': 'Check List',
            },
        ),
    ]

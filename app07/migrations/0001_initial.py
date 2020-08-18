# Generated by Django 3.1 on 2020-08-14 17:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Occupations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Occupation_Name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Info_Class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Phone', models.CharField(max_length=14)),
                ('SSC_Roll_No', models.IntegerField()),
                ('SSC_Board', models.CharField(max_length=20)),
                ('Email', models.EmailField(max_length=254)),
                ('Blood_Group', models.CharField(max_length=3)),
                ('Address', models.TextField(max_length=500)),
                ('Occupation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app07.occupations')),
            ],
        ),
    ]

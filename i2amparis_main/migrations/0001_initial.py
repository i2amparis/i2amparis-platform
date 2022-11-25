# Generated by Django 2.2.5 on 2019-11-15 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ModelsInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_name', models.TextField()),
                ('model_title', models.TextField(default='')),
                ('long_title', models.TextField(default='')),
                ('partener', models.TextField()),
                ('type_of_model', models.TextField()),
                ('time_horizon', models.IntegerField()),
                ('time_steps_in_solution', models.IntegerField(default=0)),
                ('long_description', models.TextField()),
                ('short_description', models.TextField(default='')),
                ('icon', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Socioecons',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.TextField()),
                ('subcategory', models.TextField(default='')),
                ('name', models.TextField()),
                ('state', models.TextField()),
                ('icon', models.TextField(default='')),
                ('model_name', models.ManyToManyField(to='i2amparis_main.ModelsInfo')),
            ],
        ),
        migrations.CreateModel(
            name='Sectors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.TextField()),
                ('subcategory', models.TextField(default='')),
                ('name', models.TextField()),
                ('icon', models.TextField(default='')),
                ('model_name', models.ManyToManyField(to='i2amparis_main.ModelsInfo')),
            ],
        ),
        migrations.CreateModel(
            name='Sdgs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('title', models.TextField(default='')),
                ('description', models.TextField()),
                ('icon', models.TextField(default='')),
                ('model_name', models.ManyToManyField(to='i2amparis_main.ModelsInfo')),
            ],
        ),
        migrations.CreateModel(
            name='Regions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region_name', models.TextField()),
                ('region_title', models.TextField(default='')),
                ('descr', models.TextField(default='')),
                ('model_name', models.ManyToManyField(to='i2amparis_main.ModelsInfo')),
            ],
        ),
        migrations.CreateModel(
            name='Policies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.TextField()),
                ('name', models.TextField()),
                ('state', models.TextField()),
                ('icon', models.TextField(default='')),
                ('model_name', models.ManyToManyField(to='i2amparis_main.ModelsInfo')),
            ],
        ),
        migrations.CreateModel(
            name='Mitigations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.TextField()),
                ('subcategory', models.TextField(default='')),
                ('name', models.TextField()),
                ('icon', models.TextField(default='')),
                ('model_name', models.ManyToManyField(to='i2amparis_main.ModelsInfo')),
            ],
        ),
        migrations.CreateModel(
            name='Emissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categories', models.TextField()),
                ('name', models.TextField()),
                ('state', models.TextField()),
                ('icon', models.TextField(default='')),
                ('title', models.TextField(default='')),
                ('model_name', models.ManyToManyField(to='i2amparis_main.ModelsInfo')),
            ],
        ),
        migrations.CreateModel(
            name='Countries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_name', models.TextField()),
                ('country_code', models.CharField(max_length=3)),
                ('region_name', models.ManyToManyField(to='i2amparis_main.Regions')),
            ],
        ),
        migrations.CreateModel(
            name='Adaptation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.TextField()),
                ('name', models.TextField()),
                ('icon', models.TextField(default='')),
                ('model_name', models.ManyToManyField(to='i2amparis_main.ModelsInfo')),
            ],
        ),
    ]
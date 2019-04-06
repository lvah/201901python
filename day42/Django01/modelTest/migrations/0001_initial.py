# Generated by Django 2.1.7 on 2019-03-31 08:23

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='组名')),
            ],
        ),
        migrations.CreateModel(
            name='GrouPersons',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_joined', models.DateField(default=datetime.datetime(2019, 3, 31, 8, 23, 49, 720204, tzinfo=utc))),
                ('join_reason', models.CharField(max_length=200)),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='modelTest.Group')),
            ],
        ),
        migrations.CreateModel(
            name='MyBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100, verbose_name='书籍名称')),
                ('logo', models.ImageField(upload_to='modelTest/', verbose_name='图书封面')),
                ('pubdate', models.DateField(db_column='出版日期', verbose_name='出版日期')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='姓名')),
            ],
        ),
        migrations.AddField(
            model_name='groupersons',
            name='person',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='modelTest.Person'),
        ),
        migrations.AddField(
            model_name='group',
            name='persons',
            field=models.ManyToManyField(through='modelTest.GrouPersons', to='modelTest.Person'),
        ),
    ]
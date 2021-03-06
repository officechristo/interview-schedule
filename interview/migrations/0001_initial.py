# Generated by Django 2.1.7 on 2019-10-14 11:27

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Interview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('pub_date', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Slot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date(2019, 10, 14))),
            ],
        ),
        migrations.CreateModel(
            name='SlotOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sc', models.CharField(choices=[('slot1', '9AM-10AM'), ('slot2', '10AM-11AM'), ('slot3', '11AM-12PM'), ('slot4', '12PM-1PM'), ('slot5', '1PM-2PM'), ('slot6', '2PM-3PM'), ('slot7', '3PM-4PM'), ('slot8', '4PM-5PM'), ('slot9', '5AM-6PM')], max_length=5)),
            ],
        ),
        migrations.AddField(
            model_name='slot',
            name='choices',
            field=models.ManyToManyField(to='interview.SlotOption'),
        ),
        migrations.AddField(
            model_name='slot',
            name='interview',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interview.Interview'),
        ),
        migrations.AddField(
            model_name='slot',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-09-27 20:40
from __future__ import unicode_literals

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
            name='Notice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(default=0, help_text='숫자만 입력하세요.', unique=True, verbose_name='작성번호')),
                ('text', models.CharField(default='', help_text='120자 이내로 입력하세요.', max_length=150, verbose_name='내용')),
                ('writer', models.CharField(default='', help_text='작성자를 입력하세요.', max_length=20, verbose_name='작성자')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fileName', models.FilePathField(path='tutor_excel/', verbose_name='강사시간표 파일명')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

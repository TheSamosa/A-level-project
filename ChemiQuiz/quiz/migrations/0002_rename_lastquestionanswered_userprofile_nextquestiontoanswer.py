# Generated by Django 4.0.2 on 2022-08-13 12:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='lastQuestionAnswered',
            new_name='NextQuestionToAnswer',
        ),
    ]

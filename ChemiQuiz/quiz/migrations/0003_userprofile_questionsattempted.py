# Generated by Django 4.0.2 on 2022-08-22 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_rename_lastquestionanswered_userprofile_nextquestiontoanswer'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='questionsAttempted',
            field=models.IntegerField(default=0),
        ),
    ]

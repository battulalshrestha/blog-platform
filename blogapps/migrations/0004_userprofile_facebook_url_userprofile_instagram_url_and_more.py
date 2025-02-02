# Generated by Django 5.1.1 on 2024-11-14 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapps', '0003_remove_userprofile_facebook_url_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='facebook_url',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='instagram_url',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='linkedin_url',
            field=models.CharField(blank=True, max_length=130, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='profilepic/'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='website_url',
            field=models.CharField(blank=True, max_length=1300, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='inquiry',
            field=models.CharField(default='no queries', max_length=100),
        ),
    ]

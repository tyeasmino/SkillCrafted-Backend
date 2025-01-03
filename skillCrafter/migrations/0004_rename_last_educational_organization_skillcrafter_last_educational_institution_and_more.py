# Generated by Django 5.1.2 on 2024-12-27 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skillCrafter', '0003_rename_passing_year_skillcrafter_last_passing_year_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='skillcrafter',
            old_name='last_educational_organization',
            new_name='last_educational_institution',
        ),
        migrations.AddField(
            model_name='skillcrafter',
            name='last_working_company',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='skillcrafter',
            name='last_working_projects_link_1',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='skillcrafter',
            name='last_working_projects_link_2',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='skillcrafter',
            name='last_working_years',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='skillcrafter',
            name='portfolio',
            field=models.URLField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='skillcrafter',
            name='github',
            field=models.URLField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='skillcrafter',
            name='linkedin',
            field=models.URLField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='skillcrafter',
            name='whatsapp',
            field=models.CharField(blank=True, max_length=11, null=True),
        ),
    ]

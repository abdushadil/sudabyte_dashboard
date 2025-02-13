# Generated by Django 4.2.11 on 2025-02-12 11:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_caseactivity'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='AdminUser',
        ),
        migrations.RemoveField(
            model_name='caseactivity',
            name='step',
        ),
        migrations.RemoveField(
            model_name='caseactivity',
            name='user',
        ),
        migrations.RemoveField(
            model_name='caseownership',
            name='case',
        ),
        migrations.RemoveField(
            model_name='caseownership',
            name='user',
        ),
        migrations.RemoveField(
            model_name='casestep',
            name='case',
        ),
        migrations.AlterModelTable(
            name='adminuser',
            table='admins',
        ),
        migrations.DeleteModel(
            name='Case',
        ),
        migrations.DeleteModel(
            name='CaseActivity',
        ),
        migrations.DeleteModel(
            name='CaseOwnership',
        ),
        migrations.DeleteModel(
            name='CaseStep',
        ),
    ]

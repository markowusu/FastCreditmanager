# Generated by Django 3.0.3 on 2020-09-17 00:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('creditApp', '0005_auto_20200916_1241'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction_table',
            old_name='trans_from',
            new_name='Transfer_from',
        ),
        migrations.RenameField(
            model_name='transaction_table',
            old_name='trans_to',
            new_name='Transfer_to',
        ),
        migrations.RenameField(
            model_name='transaction_table',
            old_name='amount_Transferd',
            new_name='credit',
        ),
    ]

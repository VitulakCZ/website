# Generated by Django 2.2.12 on 2023-01-14 05:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0061_installerdraft_credits'),
    ]

    operations = [
        migrations.AlterField(
            model_name='installerdraft',
            name='runner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='runners.Runner'),
        ),
    ]

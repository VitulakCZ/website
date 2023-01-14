# Generated by Django 2.2.12 on 2023-01-14 01:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('runners', '0012_runtime_enabled'),
        ('games', '0058_delete_gamemetadata'),
    ]

    operations = [
        migrations.CreateModel(
            name='InstallerDraft',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.CharField(max_length=32)),
                ('description', models.CharField(blank=True, max_length=512, null=True)),
                ('notes', models.TextField(blank=True)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('base_installer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='drafts', to='games.Installer')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='draft_installers', to='games.Game')),
                ('runner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='runners.Runner')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
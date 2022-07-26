# Generated by Django 4.0 on 2022-08-31 13:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Incident',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, editable=False, null=True)),
                ('updated', models.DateTimeField(blank=True, editable=False, null=True)),
                ('name', models.CharField(max_length=255)),
                ('hidden', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='auth.user')),
            ],
            options={
                'verbose_name': 'Incident',
                'verbose_name_plural': 'Incidents',
                'ordering': ['-created'],
                'get_latest_by': 'created',
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, editable=False, null=True)),
                ('updated', models.DateTimeField(blank=True, editable=False, null=True)),
                ('name', models.CharField(max_length=50)),
                ('type', models.CharField(choices=[('success', 'Success'), ('info', 'Information'), ('warning', 'Warning'), ('danger', 'Danger')], default='Information', max_length=20)),
                ('icon', models.CharField(default='fa-warning', help_text='Font Awesome icon name', max_length=255)),
            ],
            options={
                'verbose_name': 'Status',
                'verbose_name_plural': 'Statuses',
            },
        ),
        migrations.CreateModel(
            name='IncidentUpdate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, editable=False, null=True)),
                ('updated', models.DateTimeField(blank=True, editable=False, null=True)),
                ('description', models.TextField()),
                ('incident', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='status.incident')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='status.status')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='auth.user')),
            ],
            options={
                'verbose_name': 'Incident Update',
                'verbose_name_plural': 'Incident Updates',
                'ordering': ['created'],
                'get_latest_by': 'created',
            },
        ),
    ]

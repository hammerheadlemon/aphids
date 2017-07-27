# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-27 15:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address1', models.CharField(max_length=20)),
                ('address2', models.CharField(max_length=20)),
                ('address3', models.CharField(max_length=20)),
                ('address4', models.CharField(max_length=20)),
                ('postal_town', models.CharField(max_length=20)),
                ('postal_region', models.CharField(max_length=20)),
                ('county', models.CharField(max_length=20)),
                ('postcode', models.CharField(max_length=20)),
                ('since', models.DateField()),
                ('previous_address', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='passes.Address')),
            ],
        ),
        migrations.CreateModel(
            name='ApplicationStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=20)),
                ('urgency', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('sensitive', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Biometrics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='DiscType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disc_type', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Organisation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('companies_hse_reg', models.CharField(max_length=20)),
                ('hmrc_reg', models.CharField(max_length=20)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='passes.Address')),
            ],
        ),
        migrations.CreateModel(
            name='OrgType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('org_type', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Pass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False)),
                ('application_succeeded', models.BooleanField()),
                ('holder_staff_number', models.CharField(max_length=20)),
                ('proof_of_id_provided', models.BooleanField()),
                ('application_date', models.DateField()),
                ('activation_date', models.DateField()),
                ('expiry_date', models.DateField()),
                ('termination_date', models.DateField()),
                ('withdrawn_routine', models.BooleanField()),
                ('withdrawn_date', models.DateField(null=True)),
                ('withdrawn_denied', models.BooleanField()),
                ('withdrawn_denied_date', models.DateField(null=True)),
                ('withdrawn_denied_comments', models.TextField(null=True)),
                ('application_status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='passes.ApplicationStatus')),
            ],
        ),
        migrations.CreateModel(
            name='PassPrivilege',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('access_to_aircraft', models.BooleanField()),
                ('daytime_restrictions', models.CharField(max_length=20)),
                ('area_allowed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='privileges_allowed', to='passes.Area')),
                ('area_disallowed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='privileges_disallowed', to='passes.Area')),
            ],
        ),
        migrations.CreateModel(
            name='PassStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pass_status', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('middle_names', models.CharField(max_length=20)),
                ('surname', models.CharField(max_length=20)),
                ('dob', models.DateField()),
                ('place_of_birth', models.CharField(max_length=20)),
                ('nationality', models.CharField(max_length=20)),
                ('passport_no', models.CharField(max_length=20)),
                ('passport_image', models.BinaryField()),
                ('driving_license_no', models.CharField(max_length=20)),
                ('nat_ins', models.CharField(max_length=20)),
                ('employed_since', models.DateField()),
                ('vetting_start', models.DateField()),
                ('vetting_ref', models.CharField(max_length=20)),
                ('vetting_expiry', models.DateField()),
                ('vetting_terminated', models.BooleanField()),
                ('vetting_terminated_comment', models.TextField()),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='passes.Address')),
                ('biometrics', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='passes.Biometrics')),
                ('employer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='passes.Organisation')),
                ('line_manager', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='passes.Person')),
            ],
        ),
        migrations.CreateModel(
            name='ProofIdType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proof_id_type', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('managing_comp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sites_managed', to='passes.Organisation')),
                ('owning_comp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sites_owned', to='passes.Organisation')),
            ],
        ),
        migrations.CreateModel(
            name='SiteType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_type', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Telecoms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('landline', models.CharField(max_length=20)),
                ('mobile1', models.CharField(max_length=20)),
                ('mobile2', models.CharField(max_length=20)),
                ('email1', models.EmailField(max_length=254)),
                ('email2', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Vetting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(max_length=20)),
                ('issuing_authority', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='passes.Organisation')),
            ],
        ),
        migrations.AddField(
            model_name='site',
            name='site_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='passes.SiteType'),
        ),
        migrations.AddField(
            model_name='person',
            name='role',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='passes.Role'),
        ),
        migrations.AddField(
            model_name='person',
            name='telecoms',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='passes.Telecoms'),
        ),
        migrations.AddField(
            model_name='person',
            name='vetting_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='passes.Vetting'),
        ),
        migrations.AddField(
            model_name='pass',
            name='holder',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='passes', to='passes.Person'),
        ),
        migrations.AddField(
            model_name='pass',
            name='pass_issuer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='passes_issued', to='passes.Person'),
        ),
        migrations.AddField(
            model_name='pass',
            name='pass_privileges',
            field=models.ManyToManyField(to='passes.PassPrivilege'),
        ),
        migrations.AddField(
            model_name='pass',
            name='pass_status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='passes.PassStatus'),
        ),
        migrations.AddField(
            model_name='pass',
            name='proof_of_id_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='passes.ProofIdType'),
        ),
        migrations.AddField(
            model_name='pass',
            name='site',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='passes.Site'),
        ),
        migrations.AddField(
            model_name='pass',
            name='withdrawn_denied_disc_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='passes.DiscType'),
        ),
        migrations.AddField(
            model_name='organisation',
            name='org_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='passes.OrgType'),
        ),
        migrations.AddField(
            model_name='organisation',
            name='telecoms',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='passes.Telecoms'),
        ),
        migrations.AddField(
            model_name='area',
            name='site',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='passes.Site'),
        ),
    ]

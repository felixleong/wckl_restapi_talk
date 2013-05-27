# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'FundHouse'
        db.create_table(u'fundtracking_fundhouse', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'fundtracking', ['FundHouse'])

        # Adding model 'Fund'
        db.create_table(u'fundtracking_fund', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fund_house', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['fundtracking.FundHouse'])),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'fundtracking', ['Fund'])

        # Adding model 'Price'
        db.create_table(u'fundtracking_price', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fund', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['fundtracking.Fund'])),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('nav', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=4)),
        ))
        db.send_create_signal(u'fundtracking', ['Price'])

        # Adding model 'Annotation'
        db.create_table(u'fundtracking_annotation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('price', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['fundtracking.Price'])),
            ('time_added', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('time_modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('note', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'fundtracking', ['Annotation'])


    def backwards(self, orm):
        # Deleting model 'FundHouse'
        db.delete_table(u'fundtracking_fundhouse')

        # Deleting model 'Fund'
        db.delete_table(u'fundtracking_fund')

        # Deleting model 'Price'
        db.delete_table(u'fundtracking_price')

        # Deleting model 'Annotation'
        db.delete_table(u'fundtracking_annotation')


    models = {
        u'fundtracking.annotation': {
            'Meta': {'object_name': 'Annotation'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'note': ('django.db.models.fields.TextField', [], {}),
            'price': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['fundtracking.Price']"}),
            'time_added': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'time_modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'})
        },
        u'fundtracking.fund': {
            'Meta': {'object_name': 'Fund'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'fund_house': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['fundtracking.FundHouse']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'fundtracking.fundhouse': {
            'Meta': {'object_name': 'FundHouse'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'fundtracking.price': {
            'Meta': {'object_name': 'Price'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'fund': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['fundtracking.Fund']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nav': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '4'})
        }
    }

    complete_apps = ['fundtracking']
# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Lista'
        db.create_table('lista_lista', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('supermercado', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lista.Supermercado'])),
            ('produto', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lista.Produto'])),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('preco_unitario', self.gf('django.db.models.fields.DecimalField')(max_digits=12, decimal_places=2)),
            ('quantidade', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('criada_em', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('lista', ['Lista'])

    def backwards(self, orm):
        # Deleting model 'Lista'
        db.delete_table('lista_lista')

    models = {
        'lista.lista': {
            'Meta': {'object_name': 'Lista'},
            'criada_em': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'preco_unitario': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '2'}),
            'produto': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lista.Produto']"}),
            'quantidade': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'supermercado': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lista.Supermercado']"})
        },
        'lista.preco': {
            'Meta': {'ordering': "['supermercado', '-atualizacao']", 'unique_together': "(('supermercado', 'produto', 'valor'),)", 'object_name': 'Preco'},
            'atualizacao': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'produto': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lista.Produto']"}),
            'supermercado': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lista.Supermercado']"}),
            'valor': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '2'})
        },
        'lista.produto': {
            'Meta': {'object_name': 'Produto'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            'secoes': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['lista.Secao']", 'symmetrical': 'False'})
        },
        'lista.secao': {
            'Meta': {'object_name': 'Secao'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        },
        'lista.supermercado': {
            'Meta': {'ordering': "['nome']", 'object_name': 'Supermercado'},
            'ativo': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        }
    }

    complete_apps = ['lista']
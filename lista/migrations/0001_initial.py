# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
               # Adding model 'Precificacao'
        db.create_table('lista_precificacao', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('supermercado', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lista.Supermercado'])),
            ('produto', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lista.Produto'])),
            ('preco', self.gf('django.db.models.fields.DecimalField')(max_digits=12, decimal_places=2)),
            ('atualizacao', self.gf('django.db.models.fields.DateField')(auto_now=True, auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('lista', ['Precificacao'])

        # Adding unique constraint on 'Precificacao', fields ['supermercado', 'produto', 'preco']
        db.create_unique('lista_precificacao', ['supermercado_id', 'produto_id', 'preco'])

        # Adding model 'Cotacao'
        db.create_table('lista_cotacao', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('codigo', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('quantidade', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('supermercado', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lista.Supermercado'])),
            ('produto', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lista.Produto'])),
            ('preco', self.gf('django.db.models.fields.DecimalField')(max_digits=12, decimal_places=2)),
            ('atualizacao', self.gf('django.db.models.fields.DateField')(auto_now=True, auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('lista', ['Cotacao'])

    def backwards(self, orm):
        # Removing unique constraint on 'Precificacao', fields ['supermercado', 'produto', 'preco']
        db.delete_unique('lista_precificacao', ['supermercado_id', 'produto_id', 'preco'])

        # Deleting model 'Secao'
        db.delete_table('lista_secao')

        # Deleting model 'Produto'
        db.delete_table('lista_produto')

        # Removing M2M table for field secoes on 'Produto'
        db.delete_table('lista_produto_secoes')

        # Deleting model 'Supermercado'
        db.delete_table('lista_supermercado')

        # Deleting model 'Precificacao'
        db.delete_table('lista_precificacao')

        # Deleting model 'Cotacao'
        db.delete_table('lista_cotacao')

    models = {
        'lista.cotacao': {
            'Meta': {'ordering': "['atualizacao', 'produto']", 'object_name': 'Cotacao'},
            'atualizacao': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'codigo': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'preco': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '2'}),
            'produto': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lista.Produto']"}),
            'quantidade': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'supermercado': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lista.Supermercado']"})
        },
        'lista.precificacao': {
            'Meta': {'ordering': "['supermercado', '-atualizacao']", 'unique_together': "(('supermercado', 'produto', 'preco'),)", 'object_name': 'Precificacao'},
            'atualizacao': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'preco': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '2'}),
            'produto': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lista.Produto']"}),
            'supermercado': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lista.Supermercado']"})
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

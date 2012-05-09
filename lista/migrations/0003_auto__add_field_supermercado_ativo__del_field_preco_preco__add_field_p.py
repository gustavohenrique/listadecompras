# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing unique constraint on 'Preco', fields ['produto', 'preco', 'supermercado']
        db.delete_unique('lista_preco', ['produto_id', 'preco', 'supermercado_id'])

        # Adding field 'Supermercado.ativo'
        db.add_column('lista_supermercado', 'ativo',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)

        # Deleting field 'Preco.preco'
        db.delete_column('lista_preco', 'preco')

        # Adding field 'Preco.valor'
        db.add_column('lista_preco', 'valor',
                      self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=12, decimal_places=2),
                      keep_default=False)

        # Adding unique constraint on 'Preco', fields ['produto', 'supermercado', 'valor']
        db.create_unique('lista_preco', ['produto_id', 'supermercado_id', 'valor'])

    def backwards(self, orm):
        # Removing unique constraint on 'Preco', fields ['produto', 'supermercado', 'valor']
        db.delete_unique('lista_preco', ['produto_id', 'supermercado_id', 'valor'])

        # Deleting field 'Supermercado.ativo'
        db.delete_column('lista_supermercado', 'ativo')

        # Adding field 'Preco.preco'
        db.add_column('lista_preco', 'preco',
                      self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=12, decimal_places=2),
                      keep_default=False)

        # Deleting field 'Preco.valor'
        db.delete_column('lista_preco', 'valor')

        # Adding unique constraint on 'Preco', fields ['produto', 'preco', 'supermercado']
        db.create_unique('lista_preco', ['produto_id', 'preco', 'supermercado_id'])

    models = {
        'lista.preco': {
            'Meta': {'ordering': "['supermercado', '-atualizacao']", 'unique_together': "(('supermercado', 'produto', 'valor'),)", 'object_name': 'Preco'},
            'atualizacao': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'produto': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lista.Produto']"}),
            'supermercado': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lista.Supermercado']"}),
            'valor': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '12', 'decimal_places': '2'})
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
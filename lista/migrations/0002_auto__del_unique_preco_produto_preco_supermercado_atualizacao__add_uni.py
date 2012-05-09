# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing unique constraint on 'Preco', fields ['produto', 'preco', 'supermercado', 'atualizacao']
        db.delete_unique('lista_preco', ['produto_id', 'preco', 'supermercado_id', 'atualizacao'])

        # Adding unique constraint on 'Preco', fields ['produto', 'preco', 'supermercado']
        db.create_unique('lista_preco', ['produto_id', 'preco', 'supermercado_id'])

    def backwards(self, orm):
        # Removing unique constraint on 'Preco', fields ['produto', 'preco', 'supermercado']
        db.delete_unique('lista_preco', ['produto_id', 'preco', 'supermercado_id'])

        # Adding unique constraint on 'Preco', fields ['produto', 'preco', 'supermercado', 'atualizacao']
        db.create_unique('lista_preco', ['produto_id', 'preco', 'supermercado_id', 'atualizacao'])

    models = {
        'lista.preco': {
            'Meta': {'ordering': "['supermercado', '-atualizacao']", 'unique_together': "(('supermercado', 'produto', 'preco'),)", 'object_name': 'Preco'},
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
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        }
    }

    complete_apps = ['lista']
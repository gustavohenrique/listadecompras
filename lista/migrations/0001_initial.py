# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Secao'
        db.create_table('lista_secao', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
        ))
        db.send_create_signal('lista', ['Secao'])

        # Adding model 'Produto'
        db.create_table('lista_produto', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(unique=True, max_length=200)),
        ))
        db.send_create_signal('lista', ['Produto'])

        # Adding M2M table for field secoes on 'Produto'
        db.create_table('lista_produto_secoes', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('produto', models.ForeignKey(orm['lista.produto'], null=False)),
            ('secao', models.ForeignKey(orm['lista.secao'], null=False))
        ))
        db.create_unique('lista_produto_secoes', ['produto_id', 'secao_id'])

        # Adding model 'Supermercado'
        db.create_table('lista_supermercado', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
        ))
        db.send_create_signal('lista', ['Supermercado'])

        # Adding model 'Preco'
        db.create_table('lista_preco', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('supermercado', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lista.Supermercado'])),
            ('produto', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lista.Produto'])),
            ('preco', self.gf('django.db.models.fields.DecimalField')(max_digits=12, decimal_places=2)),
            ('atualizacao', self.gf('django.db.models.fields.DateField')(auto_now=True, auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('lista', ['Preco'])

        # Adding unique constraint on 'Preco', fields ['supermercado', 'produto', 'preco', 'atualizacao']
        db.create_unique('lista_preco', ['supermercado_id', 'produto_id', 'preco', 'atualizacao'])

    def backwards(self, orm):
        # Removing unique constraint on 'Preco', fields ['supermercado', 'produto', 'preco', 'atualizacao']
        db.delete_unique('lista_preco', ['supermercado_id', 'produto_id', 'preco', 'atualizacao'])

        # Deleting model 'Secao'
        db.delete_table('lista_secao')

        # Deleting model 'Produto'
        db.delete_table('lista_produto')

        # Removing M2M table for field secoes on 'Produto'
        db.delete_table('lista_produto_secoes')

        # Deleting model 'Supermercado'
        db.delete_table('lista_supermercado')

        # Deleting model 'Preco'
        db.delete_table('lista_preco')

    models = {
        'lista.preco': {
            'Meta': {'unique_together': "(('supermercado', 'produto', 'preco', 'atualizacao'),)", 'object_name': 'Preco'},
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
            'Meta': {'object_name': 'Supermercado'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        }
    }

    complete_apps = ['lista']
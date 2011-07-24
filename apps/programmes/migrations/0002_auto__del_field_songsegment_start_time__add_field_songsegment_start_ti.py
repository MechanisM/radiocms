# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'SongSegment.start_time'
        db.delete_column('programmes_songsegment', 'start_time')

        # Adding field 'SongSegment.start_time_minutes'
        db.add_column('programmes_songsegment', 'start_time_minutes', self.gf('django.db.models.fields.IntegerField')(default=0), keep_default=False)

        # Adding field 'SongSegment.start_time_seconds'
        db.add_column('programmes_songsegment', 'start_time_seconds', self.gf('django.db.models.fields.IntegerField')(default=0), keep_default=False)

        # Deleting field 'EventSegment.start_time'
        db.delete_column('programmes_eventsegment', 'start_time')

        # Adding field 'EventSegment.start_time_minutes'
        db.add_column('programmes_eventsegment', 'start_time_minutes', self.gf('django.db.models.fields.IntegerField')(default=0), keep_default=False)

        # Adding field 'EventSegment.start_time_seconds'
        db.add_column('programmes_eventsegment', 'start_time_seconds', self.gf('django.db.models.fields.IntegerField')(default=0), keep_default=False)


    def backwards(self, orm):
        
        # User chose to not deal with backwards NULL issues for 'SongSegment.start_time'
        raise RuntimeError("Cannot reverse this migration. 'SongSegment.start_time' and its values cannot be restored.")

        # Deleting field 'SongSegment.start_time_minutes'
        db.delete_column('programmes_songsegment', 'start_time_minutes')

        # Deleting field 'SongSegment.start_time_seconds'
        db.delete_column('programmes_songsegment', 'start_time_seconds')

        # User chose to not deal with backwards NULL issues for 'EventSegment.start_time'
        raise RuntimeError("Cannot reverse this migration. 'EventSegment.start_time' and its values cannot be restored.")

        # Deleting field 'EventSegment.start_time_minutes'
        db.delete_column('programmes_eventsegment', 'start_time_minutes')

        # Deleting field 'EventSegment.start_time_seconds'
        db.delete_column('programmes_eventsegment', 'start_time_seconds')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'music.artist': {
            'Meta': {'object_name': 'Artist'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'music.song': {
            'Meta': {'object_name': 'Song'},
            'artist': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['music.Artist']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'programmes.episode': {
            'Meta': {'object_name': 'Episode'},
            'episode': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'series': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'show': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'episodes'", 'to': "orm['programmes.Show']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'programmes.eventsegment': {
            'Meta': {'object_name': 'EventSegment'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'duration': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start_time_minutes': ('django.db.models.fields.IntegerField', [], {}),
            'start_time_seconds': ('django.db.models.fields.IntegerField', [], {})
        },
        'programmes.instance': {
            'Meta': {'object_name': 'Instance'},
            'episode': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'instances'", 'to': "orm['programmes.Episode']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tx_time': ('django.db.models.fields.DateTimeField', [], {})
        },
        'programmes.presenter': {
            'Meta': {'object_name': 'Presenter', '_ormbases': ['auth.User']},
            'preferred_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'user_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True', 'primary_key': 'True'})
        },
        'programmes.show': {
            'Meta': {'object_name': 'Show'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'presenters': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['programmes.Presenter']", 'symmetrical': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'programmes.songsegment': {
            'Meta': {'object_name': 'SongSegment'},
            'duration': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'song': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['music.Song']"}),
            'start_time_minutes': ('django.db.models.fields.IntegerField', [], {}),
            'start_time_seconds': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['programmes']

# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'ScheduleItem'
        db.create_table('programmes_scheduleitem', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('schedule', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['programmes.Schedule'])),
            ('show', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['programmes.Show'])),
            ('time', self.gf('django.db.models.fields.TimeField')()),
            ('is_monday', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_tuesday', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_wednesday', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_thursday', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_friday', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_saturday', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_sunday', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('programmes', ['ScheduleItem'])

        # Adding model 'Schedule'
        db.create_table('programmes_schedule', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('programmes', ['Schedule'])


    def backwards(self, orm):
        
        # Deleting model 'ScheduleItem'
        db.delete_table('programmes_scheduleitem')

        # Deleting model 'Schedule'
        db.delete_table('programmes_schedule')


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
            'description': ('django.db.models.fields.TextField', [], {'max_length': '1000', 'null': 'True', 'blank': 'True'}),
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
            'episode': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['programmes.Episode']"}),
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
        'programmes.schedule': {
            'Meta': {'object_name': 'Schedule'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'programmes.scheduleitem': {
            'Meta': {'object_name': 'ScheduleItem'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_friday': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_monday': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_saturday': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_sunday': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_thursday': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_tuesday': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_wednesday': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'schedule': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['programmes.Schedule']"}),
            'show': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['programmes.Show']"}),
            'time': ('django.db.models.fields.TimeField', [], {})
        },
        'programmes.show': {
            'Meta': {'object_name': 'Show'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'presenters': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['programmes.Presenter']", 'symmetrical': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'programmes.songsegment': {
            'Meta': {'ordering': "('start_time_minutes', 'start_time_seconds')", 'object_name': 'SongSegment'},
            'duration': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'episode': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['programmes.Episode']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'song': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['music.Song']"}),
            'start_time_minutes': ('django.db.models.fields.IntegerField', [], {}),
            'start_time_seconds': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['programmes']

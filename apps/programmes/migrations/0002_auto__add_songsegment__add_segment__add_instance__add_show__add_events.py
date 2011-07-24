# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'SongSegment'
        db.create_table('programmes_songsegment', (
            ('segment_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['programmes.Segment'], unique=True, primary_key=True)),
            ('song', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['music.Song'])),
        ))
        db.send_create_signal('programmes', ['SongSegment'])

        # Adding model 'Segment'
        db.create_table('programmes_segment', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('start_time', self.gf('django.db.models.fields.TimeField')()),
            ('duration', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('programmes', ['Segment'])

        # Adding model 'Instance'
        db.create_table('programmes_instance', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('episode', self.gf('django.db.models.fields.related.ForeignKey')(related_name='instances', to=orm['programmes.Episode'])),
        ))
        db.send_create_signal('programmes', ['Instance'])

        # Adding model 'Show'
        db.create_table('programmes_show', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('programmes', ['Show'])

        # Adding M2M table for field presenters on 'Show'
        db.create_table('programmes_show_presenters', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('show', models.ForeignKey(orm['programmes.show'], null=False)),
            ('presenter', models.ForeignKey(orm['programmes.presenter'], null=False))
        ))
        db.create_unique('programmes_show_presenters', ['show_id', 'presenter_id'])

        # Adding model 'EventSegment'
        db.create_table('programmes_eventsegment', (
            ('segment_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['programmes.Segment'], unique=True, primary_key=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('programmes', ['EventSegment'])

        # Adding model 'Presenter'
        db.create_table('programmes_presenter', (
            ('user_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True, primary_key=True)),
            ('preferred_name', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal('programmes', ['Presenter'])

        # Adding model 'Episode'
        db.create_table('programmes_episode', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('show', self.gf('django.db.models.fields.related.ForeignKey')(related_name='episodes', to=orm['programmes.Show'])),
        ))
        db.send_create_signal('programmes', ['Episode'])


    def backwards(self, orm):
        
        # Deleting model 'SongSegment'
        db.delete_table('programmes_songsegment')

        # Deleting model 'Segment'
        db.delete_table('programmes_segment')

        # Deleting model 'Instance'
        db.delete_table('programmes_instance')

        # Deleting model 'Show'
        db.delete_table('programmes_show')

        # Removing M2M table for field presenters on 'Show'
        db.delete_table('programmes_show_presenters')

        # Deleting model 'EventSegment'
        db.delete_table('programmes_eventsegment')

        # Deleting model 'Presenter'
        db.delete_table('programmes_presenter')

        # Deleting model 'Episode'
        db.delete_table('programmes_episode')


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
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'show': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'episodes'", 'to': "orm['programmes.Show']"})
        },
        'programmes.eventsegment': {
            'Meta': {'object_name': 'EventSegment', '_ormbases': ['programmes.Segment']},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'segment_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['programmes.Segment']", 'unique': 'True', 'primary_key': 'True'})
        },
        'programmes.instance': {
            'Meta': {'object_name': 'Instance'},
            'episode': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'instances'", 'to': "orm['programmes.Episode']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'programmes.presenter': {
            'Meta': {'object_name': 'Presenter', '_ormbases': ['auth.User']},
            'preferred_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'user_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True', 'primary_key': 'True'})
        },
        'programmes.segment': {
            'Meta': {'object_name': 'Segment'},
            'duration': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start_time': ('django.db.models.fields.TimeField', [], {})
        },
        'programmes.show': {
            'Meta': {'object_name': 'Show'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'presenters': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['programmes.Presenter']", 'symmetrical': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'programmes.songsegment': {
            'Meta': {'object_name': 'SongSegment', '_ormbases': ['programmes.Segment']},
            'segment_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['programmes.Segment']", 'unique': 'True', 'primary_key': 'True'}),
            'song': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['music.Song']"})
        }
    }

    complete_apps = ['programmes']

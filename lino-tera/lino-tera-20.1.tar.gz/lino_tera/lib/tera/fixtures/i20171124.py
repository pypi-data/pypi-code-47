# no longer used. content copied to spzloader2

from lino.api import dd, rt
from lino_xl.lib.tim2lino.spzloader import TimLoader

List = rt.models.lists.List
Member = rt.models.lists.Member
Topic = rt.models.topics.Topic
Interest = rt.models.topics.Interest
Partner = rt.models.contacts.Partner
Note = rt.models.notes.Note
Course = rt.models.courses.Course

class TimLoader(TimLoader):
    
    def objects(self):

        Topic.objects.all().delete()
        Interest.objects.all().delete()
        Note.objects.all().delete()

        yield self.load_dbf('PRB')
        yield self.load_dbf('PPR')
        yield self.load_dbf('MSG')


    def load_prb(self, row, **kw):
        kw = dict(
            id=row.idprb.strip(),
            name=row.name1.strip(),
            ref=row.ref.strip() or None)
        if Topic.objects.filter(pk=kw['id']).exists():
            return
        if Topic.objects.filter(ref=kw['ref']).exists():
            return
        yield Topic(**kw)
        
    def load_ppr(self, row, **kw):
        idprb = row.idprb.strip()
        if not idprb:
            return
        if not Topic.objects.filter(id=idprb).exists():
            return
        idpar = row.idpar.strip()
        try:
            prj = Course.objects.get(ref=idpar)
        except Course.DoesNotExist:
            dd.logger.warning(
                "Cannot import MSG %s : no course ref %s", row, idpar)
            return
        # idpar = self.par_pk(row.idpar.strip())
        # if idpar is None:
        #     return
        # try:
        #     par = Partner.objects.get(id=idpar)
        # except Partner.DoesNotExist:
        #     return
        yield Interest(owner=prj, topic_id=idprb)
        
    def load_msg(self, row, **kw):
        idpar = row.idpar.strip()
        try:
            prj = Course.objects.get(ref=idpar)
        except Course.DoesNotExist:
            dd.logger.warning(
                "Cannot import MSG %s : no course ref %s", row, idpar)
            return
        mt, new = rt.models.notes.NoteType.objects.get_or_create(
            name=row.type.strip())
            
        # idpar = self.par_pk(row.idpar.strip())
        # if idpar is None:
        #     return
        if row.date is None:
            return
        # try:
        #     prj = Course.objects.get(partner__id=idpar)
        # except Course.DoesNotExist:
        #     prj = None
        # except Course.MultipleObjectsReturned:
        #     prj = None
        yield Note(
            project=prj,
            type=mt,
            user=self.get_user(row.idusr),
            date=row.date,
            time=row.time.strip(),
            subject=row.titre.strip(),
            body=self.dbfmemo(row.texte))
        

from django.conf import settings

def objects():
    tim = TimLoader(settings.SITE.legacy_data_path)
    for obj in tim.objects():
        yield obj

    # tim.finalize()

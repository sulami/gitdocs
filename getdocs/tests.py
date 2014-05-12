from django.test import TestCase
from getdocs.functions import get_docs
from processor.models import Docs, Version
from datetime import date, timedelta

class GetDocsTestCase(TestCase):
    def setUp(self):
        self.docs = Docs(owner='sulami', name='Test')
        self.docs.save()
        self.verm = Version(name='master', content='# Test')
        self.verm.save()
        self.ver1 = Version(name='0.1', content='# Not master')
        self.ver1.save()
        self.ver2 = Version(name='0.2', content='# Not really master')
        self.ver2.save()
        self.docs.versions.add(self.verm)
        self.docs.versions.add(self.ver1)
        self.docs.versions.add(self.ver2)

    def tearDown(self):
        for doc in Docs.objects.all():
            doc.delete()
        for ver in Version.objects.all():
            ver.delete()

    def test_get_existing_docs(self):
        docs = get_docs('sulami', 'Test')
        self.assertIsNotNone(docs)

    def Dtest_get_docs_from_gh(self):
        docs = get_docs('sulami', 'dotfiles')
        self.assertIsNotNone(docs)

    def Dtest_get_not_existing_docs(self):
        notdocs = get_docs('sulami', 'foobar')
        self.assertIsNone(notdocs)

    def Dtest_save_docs_fetched_from_github(self):
        try: docs = Docs.objects.get(owner='sulami', name='dotfiles')
        except: docs = None
        self.assertIsNone(docs)
        get_docs('sulami', 'dotfiles')
        try: docs = Docs.objects.get(owner='sulami', name='dotfiles')
        except: docs = None
        self.assertIsNotNone(docs)
        vers = []
        for v in docs.versions.all():
            vers.append(v.name)
        self.assertIn('master', vers)
        master = docs.versions.get(name='master')
        self.assertIn('These are my dotfiles', master.content)

    def test_old_docs_get_refreshed(self):
        self.docs.time = date.today() + timedelta(days=-8)
        self.docs.save()
        get_docs(self.docs.owner, self.docs.name)
        self.assertEqual(self.docs.time, date.today())
        self.docs.time = date.today()
        self.docs.save()


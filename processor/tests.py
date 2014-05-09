from django.test import TestCase
from processor.functions import process_docs
from processor.models import Docs, Version

class ProcessDocsTestCase(TestCase):
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

    def tearDown(delf):
        for doc in Docs.objects.all():
            doc.delete()
        for ver in Version.objects.all():
            ver.delete()

    def test_readme_gets_processed(self):
        docs = process_docs(self.verm.content)
        self.assertEqual(docs, '<h1>Test</h1>')

    def test_docs_model_holds_data(self):
        docs = Docs.objects.get(pk=1)
        self.assertEqual(docs.owner, 'sulami')
        self.assertEqual(docs.name, 'Test')
        self.assertIn(self.verm, docs.versions.all())

    def test_version_model_holds_data(self):
        ver = Version.objects.get(pk=1)
        self.assertEqual(ver.name, 'master')
        self.assertEqual(ver.content, '# Test')

    def test_docs_returns_latest_first(self):
        tmp = Version()
        tmp.name = '0.1'
        tmp.content = '# Not master'
        tmp.save()
        self.docs.versions.add(tmp)
        ver = self.docs.get_latest_version()
        self.assertEqual(ver, self.verm)

    def test_docs_returns_latest_first_without_master(self):
        self.docs.versions.remove(self.verm) # Get rid of master
        self.docs.versions.add(self.ver2)
        self.docs.versions.add(self.ver1)
        latest = self.docs.get_latest_version()
        self.assertEqual(latest, self.ver2)
        self.docs.versions.add(self.verm) # Readd master

    def test_docs_return_ordered_list_of_versions(self):
        versions = self.docs.get_versions()
        tmp = Version(name='1.0', content='')
        tmp.save()
        self.docs.versions.add(tmp)
        self.assertEqual(versions[0].name, '0.1')
        self.assertEqual(versions[1].name, '0.2')
        self.assertEqual(versions[2].name, '1.0')
        self.assertEqual(versions[3].name, 'master')
        self.docs.versions.remove(tmp)

    def test_docs_returns_nothing_when_nothing_there(self):
        docs = Docs(owner='foo', name='bar')
        docs.save()
        latest = docs.get_latest_version()
        self.assertIsNone(latest)
        alls = docs.get_versions()
        self.assertTrue(alls.count() == 0)
        docs.delete()


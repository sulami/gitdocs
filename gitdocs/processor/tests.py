from django.test import TestCase
from processor.functions import process_docs
from processor.models import Docs, Version

class ProcessDocsTestCase(TestCase):
    def setUp(self):
        self.docs = Docs()
        self.docs.owner = 'sulami'
        self.docs.name = 'Test'
        self.docs.save()
        self.ver = Version()
        self.ver.name = 'master'
        self.ver.content = '# Test'
        self.ver.save()
        self.docs.versions.add(self.ver)

    def test_readme_gets_processed(self):
        docs = process_docs('# Test')
        self.assertEqual(docs, '<h1>Test</h1>')

    def test_docs_model(self):
        self.assertIsNotNone(Docs.objects.get(pk=1))

    def test_docs_model_holds_data(self):
        docs = Docs.objects.get(pk=1)
        self.assertEqual(docs.owner, 'sulami')
        self.assertEqual(docs.name, 'Test')
        self.assertIn(self.ver, docs.versions.all())

    def test_version_model_holds_data(self):
        ver = Version.objects.get(pk=1)
        self.assertEqual(ver.name, 'master')
        self.assertEqual(ver.content, '# Test')


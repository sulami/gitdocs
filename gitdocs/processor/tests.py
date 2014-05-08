from django.test import TestCase
from processor.functions import process_docs
from processor.models import Docs, Version

class ProcessDocsTestCase(TestCase):
    def test_readme_gets_processed(self):
        docs = process_docs('# Test')
        self.assertEqual(docs, '<h1>Test</h1>')

    def test_docs_model(self):
        docs = Docs()
        self.assertIsNotNone(docs)

    def test_docs_model_holds_data(self):
        tmp = Docs()
        tmp.owner = 'sulami'
        tmp.name = 'Test'
        tmp.save()
        docs = Docs.objects.get(pk=1)
        self.assertEqual(docs.owner, 'sulami')
        self.assertEqual(docs.name, 'Test')

    def test_version_model_holds_data(self):
        tmp = Version()
        tmp.name = '0.1'
        tmp.content = '# Test'
        tmp.save()
        ver = Version.objects.get(pk=1)
        self.assertEqual(ver.name, '0.1')
        self.assertEqual(ver.content, '# Test')


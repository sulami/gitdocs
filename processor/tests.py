from django.test import TestCase
from processor.functions import process_docs
from processor.models import Docs

class ProcessDocsTestCase(TestCase):
    def test_readme_gets_processed(self):
        docs = process_docs('# Test')
        self.assertEqual(docs, '<h1>Test</h1>')

    def test_docs_model(self):
        docs = Docs()
        self.assertIsNotNone(docs)


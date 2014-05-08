from django.test import TestCase
from processor.functions import process_docs

class ProcessDocs(TestCase):
    def test_readme_gets_processed(self):
        docs = process_docs('# Test')
        self.assertEqual(docs, '<h1>Test</h1>')


from unittest import TestCase

import camel_case

class testCamelCase(TestCase):
    def test_camelCase_sentence(self):

        self.assertEqual('helloWorld', camel_case.camelcase('Hello World'))
    
    def test_camelCase_blank(self):
        self.assertEqual('', camel_case.camelcase('') )

    def test_camelCase_oneWord(self):
        self.assertEqual('hello', camel_case.camelcase('Hello'))

    def test_camelCase_nonAlpha(self):
        self.assertEqual('hello!1', camel_case.camelcase('Hello!1'))
    
    def test_camelCase_emoji(self):
        self.assertEqual('😁', camel_case.camelcase('😁'))

    def test_camelCase_newLines(self):
        self.assertEqual('helloWorld', camel_case.camelcase('Hello\n\t  World'))
    
    def test_camelCase_whiteSpace(self):
        self.assertEqual('hello', camel_case.camelcase('       Hello      '))
    
    def test_camelCase_oneWord(self):
        self.assertEqual('helloWorld', camel_case.camelcase('Hello  World'))


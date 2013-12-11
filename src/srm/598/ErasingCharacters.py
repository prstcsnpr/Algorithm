import unittest

class ErasingCharacters(object):
    def simulate(self, s):
        while True:
            result = s
            for i in range(len(s) - 1):
                if s[i] == s[i + 1]:
                    result = s[0:i] + s[i+2:]
            if result == s:
                return result
            else:
                s = result

class ErasingCharactersTestCase(unittest.TestCase):
    def setUp(self):
        self.ec = ErasingCharacters()
    def test_0(self):
        self.assertEqual(self.ec.simulate('cieeilll'), 'cl')
    def test_1(self):
        self.assertEqual(self.ec.simulate('topcoder'), 'topcoder')
    def test_2(self):
        self.assertEqual(self.ec.simulate('abcdefghijklmnopqrstuvwxyyxwvutsrqponmlkjihgfedcba'), '')
    def test_3(self):
        self.assertEqual(self.ec.simulate('bacaabaccbaaccabbcabbacabcbba'), 'bacbaca')
    def test_4(self):
        self.assertEqual(self.ec.simulate('eel'), 'l')
        
if __name__ == '__main__':
    unittest.main()
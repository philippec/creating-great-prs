import random
try:
    import unittest2 as unittest
except ImportError:
    import unittest
import emoji
import re
import os


class BookTest(unittest.TestCase):
    
    def setUp(self):
        with open('Book/Chapters/01.md', 'r') as file:
            self.chapter01 = file.read().replace('\n', '')
        with open('Book/Chapters/02.md', 'r') as file:
            self.chapter02 = file.read().replace('\n', '')

    def stem(self, word):
        for suffix in ['s']:
            if word.endswith(suffix):
                return word[:-len(suffix)]
            return word

    def test_characters(self):
        allPeopleRaw = re.findall(r'👤(\w+)', self.chapter01)
        allPeople = set([person.lower() for person in allPeopleRaw])
        knownPeopleRaw = os.listdir('Book/Characters')
        knownPeople = [os.path.splitext(person)[0].lower() for person in knownPeopleRaw]
        for onePerson in allPeople:
            if not (onePerson in knownPeople):
                self.fail('{} not found in {}'.format(onePerson, knownPeople))

    def test_places(self):
        allPlacesRaw = re.findall(r'📍(\w+)', self.chapter01)
        allPlaces = set([place.lower() for place in allPlacesRaw])
        knownPlacesRaw = os.listdir('Book/Places')
        knownPlaces = [os.path.splitext(place)[0].lower() for place in knownPlacesRaw]
        for onePlace in allPlaces:
            if not (onePlace in knownPlaces):
                if not (self.stem(onePlace) in knownPlaces):
                    self.fail('{} not found in {}'.format(onePlace, knownPlaces))

    def test_tech(self):
        allTechRaw = re.findall(r'🔧(\w+)', self.chapter01)
        allTech = set([tech.lower() for tech in allTechRaw])
        knownTechRaw = os.listdir('Book/Tech')
        knownTech = [os.path.splitext(tech)[0].lower() for tech in knownTechRaw]
        for oneTech in allTech:
            if not (oneTech in knownTech):
                if not (self.stem(oneTech) in knownTech):
                    self.fail('{} not found in {}'.format(oneTech, knownTech))

    def test_characters_chapter_02(self):
        allPeopleRaw = re.findall(r'👤(\w+)', self.chapter02)
        allPeople = set([person.lower() for person in allPeopleRaw])
        knownPeopleRaw = os.listdir('Book/Characters')
        knownPeople = [os.path.splitext(person)[0].lower() for person in knownPeopleRaw]
        for onePerson in allPeople:
            if not (onePerson in knownPeople):
                self.fail('{} not found in {}'.format(onePerson, knownPeople))

    def test_places_chapter_02(self):
        allPlacesRaw = re.findall(r'📍(\w+)', self.chapter02)
        allPlaces = set([place.lower() for place in allPlacesRaw])
        knownPlacesRaw = os.listdir('Book/Places')
        knownPlaces = [os.path.splitext(place)[0].lower() for place in knownPlacesRaw]
        for onePlace in allPlaces:
            if not (onePlace in knownPlaces):
                if not (self.stem(onePlace) in knownPlaces):
                    self.fail('{} not found in {}'.format(onePlace, knownPlaces))

    def test_tech_chapter_02(self):
        allTechRaw = re.findall(r'🔧(\w+)', self.chapter02)
        allTech = set([tech.lower() for tech in allTechRaw])
        knownTechRaw = os.listdir('Book/Tech')
        knownTech = [os.path.splitext(tech)[0].lower() for tech in knownTechRaw]
        for oneTech in allTech:
            if not (oneTech in knownTech):
                if not (self.stem(oneTech) in knownTech):
                    self.fail('{} not found in {}'.format(oneTech, knownTech))

if __name__ == '__main__':
    import xmlrunner
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'))

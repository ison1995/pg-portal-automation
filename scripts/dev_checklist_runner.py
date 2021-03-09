import unittest
import HTMLTestRunner
from selenium import webdriver
from checklists.dev_release_checklist import devReleaseChecklist

class devChecklistRunner(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		cls.browser = webdriver.Chrome()
		cls.dev_checklist_steps = devReleaseChecklist(cls.browser)
		cls.lib = cls.dev_checklist_steps.lib
		cls.lib.urlSetup()

	def test1_GoogleSignIn(self):
		self.dev_checklist_steps.step_GoogleSignIn()
		
		# Assertion Check
		stack_url = "https://stackoverflow.com/#"
		current_url = self.browser.current_url
		self.assertEqual(stack_url, current_url)

	def test2_PortalSignIn(self):
		self.dev_checklist_steps.step_PortalSignIn()
		
		# Assertion Check
		portal_url = self.lib.URL + "write"
		current_url = self.browser.current_url
		self.assertEqual(portal_url, current_url)

#	def test3_StoryCreate(self):
#		self.dev_checklist_steps.step_StoryCreate()
		# TODO: Assert Statement 

#	def test4_CharacterCreate(self):
#		self.dev_checklist_steps.step_CharacterCreate()
		# TODO: Assert Statement 

#	def test5_CharacterCustomize(self):
#		self.dev_checklist_steps.step_CharacterCustomize()
		# TODO: Assert Statement 

#	def test6_OutfitsCreate(self):
#		self.dev_checklist_steps.step_OutfitsCreate()
		# TODO: Assert Statement 

#	def test7_ChaptersCreate(self):
#		self.dev_checklist_steps.step_ChaptersCreate()
		# TODO: Assert Statement 

#	def test8_ChaptersCreate(self):
#		self.dev_checklist_steps.step_ShareGmail()
		# TODO: Assert Statement 

#	def test9_ChaptersCreate(self):
#		self.dev_checklist_steps.step_StoryPublish()
		# TODO: Assert Statement 

	@classmethod
	def tearDownClass(cls):
		cls.browser.quit()

if __name__ == '__main__':
	filepath = "/Users/isaacson/Downloads/Repos/pg-portal-automation/reports/report.html"
	fp = open(filepath, 'wb')
	unittest.main(testRunner=HTMLTestRunner.HTMLTestRunner(stream=fp))
	fp.close()

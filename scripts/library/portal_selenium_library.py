# Automation for Portal QA Checklist
import time
import unittest
import calendar
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

global browser
browser = webdriver.Chrome()


class DevChecklist(unittest.TestCase):

	def setUp(self):
		# Setup instead of using init since we are using unittest
		self.url = ""
		self.user_input_version = ""

	def urlSetup(self):
		# Asks user for which version of Portal to use 
		user_input_version = input("Which version do you want to sign into? Type in 'dev' for main dev: ")

		if user_input_version == "dev":
			url = "https://pg-story-dev.appspot.com/"
		else :
			url = "http://version"+user_input_version+"-dot-pg-story-dev.appspot.com/"

		# Assigns Variabless
		self.url = url
		self.user_input_version = user_input_version

	def googleSignIn(self, user, pw):

		# Navigates to stackoverflow and presses the login button
		browser.get("https://stackoverflow.com/")
		button_stack_login_locator = '//a[@href="'+"https://stackoverflow.com/users/login?ssrc=head&returnurl=https%3a%2f%2fstackoverflow.com%2f"+'"]'
		WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.XPATH, button_stack_login_locator)))
		button_stack_login = browser.find_element_by_xpath(button_stack_login_locator)
		time.sleep(1)
		button_stack_login.click()

		# Chooses to login via Google
		WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.CLASS_NAME, "s-btn__google")))
		button_stack_google = browser.find_element_by_class_name("s-btn__google")
		button_stack_google.click()

		# Enters Username 
		WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='identifierId']")))
		time.sleep(2)
		ActionChains(browser).send_keys(user).perform()
		time.sleep(2) # Simulates real person waiting
		ActionChains(browser).send_keys(Keys.RETURN).perform()

		# Enters Password
		time.sleep(2)
		ActionChains(browser).send_keys(pw).perform()
		time.sleep(2) # Simulates real person waiting
		ActionChains(browser).send_keys(Keys.RETURN).perform()
		time.sleep(2)

	def portalSignIn(self, url): 

		# Navigates to Episode Portal 
		browser.get(url)

		# Click "Create Story" button to scroll down
		WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.LINK_TEXT, "Create a Story")))
		button_createstory = browser.find_element_by_link_text("Create a Story")
		button_createstory.click()
		time.sleep(1) # Pauses for scroll to finish

		# Click Google Sign-in button
		WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.CLASS_NAME, "c-btn--g-plus")))
		button_googlesignin = browser.find_element_by_class_name("c-btn--g-plus")
		button_googlesignin.click() 
		time.sleep(1) # Pauses to fool Google's anti-bot
		
		# Uncheck Google Allow Check Box
		#checkbox_google_allow_locator = "input[id='persist_checkbox']"
		#checkbox_google_allow = browser.find_element_by_css_selector(checkbox_google_allow_locator)
		#checkbox_google_allow.click()
		#time.sleep(1) 

		# Press Google Allow Submit
		#button_google_allow = browser.find_element_by_name("submit_true") 
		#button_google_allow.click()

	def portalNewWriterTOS(self, url):

		# Checks the TOS checkbox
		checkbox_TOS_locator = "input[id='checkbox-tos']"
		WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, checkbox_TOS_locator)))
		checkbox_TOS = browser.find_element_by_css_selector(checkbox_TOS_locator)
		checkbox_TOS.click()
		time.sleep(1) # Wait to activate "Stat Writing!" button

		# Presses TOS Submit button
		button_submit_TOS_locator = "input[id='submit-tos']"
		WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, button_submit_TOS_locator)))
		button_submit_TOS = browser.find_element_by_css_selector(button_submit_TOS_locator)
		button_submit_TOS.click() 
		time.sleep(1)

	def createNewStory(self, url, version_number):
		# Redirect to Home Page
		browser.get(url)
		time.sleep(1)

		# Close New Onboarding Flow Popup
		WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.CLASS_NAME, "shepherd-cancel-icon")))
		button_close_onboarding = browser.find_element_by_class_name("shepherd-cancel-icon")
		button_close_onboarding.click()

		# Create New Story Button Click
		WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.LINK_TEXT, "New Story")))
		button_new_story = browser.find_element_by_link_text("New Story")
		button_new_story.click() # Click on "Create New Story" button

		# Input the Story Name and Submit
		WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.ID, "new_story_name")))
		input_new_story = browser.find_element_by_id("new_story_name")
		input_new_story.clear()
		input_new_story.send_keys(version_number) # Adds the version# as the name
		button_new_story_submit = browser.find_element_by_id("new-story-submit")
		button_new_story_submit.click() # Submits the story name

		# Wait until "Characters" button is loaded on Story Home Page and get current url
		WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.LINK_TEXT, "Characters")))
		story_url = browser.current_url
		return story_url

	def test_characterCreate(self, story_id_url, character_model, character_name, first_flag):
		# Go to Story Page
		browser.get(story_id_url)

		if first_flag == True:
			# Select Character Style and Formats
			WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.LINK_TEXT, "Characters")))
			button_characters = browser.find_element_by_link_text("Characters")
			button_characters.click()
			WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.LINK_TEXT, "Use Episode Limelight")))
			button_limelight = browser.find_element_by_link_text("Use Episode Limelight")
			button_limelight.click()
			WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.LINK_TEXT, "Use Episode Cinematic")))
			button_cinematic = browser.find_element_by_link_text("Use Episode Cinematic")
			button_cinematic.click()

		elif first_flag == False:
			# Just press "Characters" button
			WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.LINK_TEXT, "Characters")))
			button_characters = browser.find_element_by_link_text("Characters")
			button_characters.click()
			WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.LINK_TEXT, "New Character")))
			button_new_character = browser.find_element_by_link_text("New Character")
			button_new_character.click()

		# Creates Character
		WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.NAME, "actor")))
		time.sleep(1)
		actor_locator = browser.find_element_by_name("actor")
		actor = Select(actor_locator)
		actor.select_by_visible_text(character_model)
		time.sleep(1)
		input_character_name = browser.find_element_by_name("name")
		input_character_name.click()
		ActionChains(browser).send_keys(character_name + Keys.RETURN).perform()

		# Wait for next page to load
		WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.LINK_TEXT, "New Character")))

		# Hard Assert if character has been created with character_name
		display_name_selector = "//input[@value='" + character_name + "']"
		display_name = browser.find_element_by_xpath(display_name_selector)
		self.assertIsNotNone(display_name)

	def customizeCharacter(self, story_id_url, character_name, body, body_color, brow, brow_color, hair, hair_color, 
							eyes, eyes_color, face, nose, lips, lips_color):
		# Go to Story Page
		browser.get(story_id_url)

		# Press the Characters button
		WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.LINK_TEXT, "Characters")))
		button_characters = browser.find_element_by_link_text("Characters")
		button_characters.click()

		# Choose which Character to customize
		WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.LINK_TEXT, character_name)))
		button_character_toCustomize = browser.find_element_by_link_text(character_name)
		button_character_toCustomize.click()

		# Define Customize Helper Function
		def customizeCharacterHelper(part_toCustomize, part_toSelect, color_toSelect, color_flag):
			# Select Which Object to Customize
			button_toCustomize_xpath_selector = "//*[contains(text(), '" + part_toCustomize + "')]"
			WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.XPATH, button_toCustomize_xpath_selector)))
			button_toCustomize = browser.find_element_by_xpath(button_toCustomize_xpath_selector)
			button_toCustomize.click()

			# Choose Customizable Object
			part_xpath_selector = "//p[text()='" + part_toSelect + "']"
			button_part_toChoose = browser.find_element_by_xpath(part_xpath_selector)
			button_part_toChoose.click()

			# Choose Color
			if color_flag == True:
				body_color_id = "color-cell-" + color_toSelect
				button_bodyColor_toChoose = browser.find_element_by_id(body_color_id)
				button_bodyColor_toChoose.click()

			# Save Changes and Wait for save to finish
			save_changes_button = browser.find_element_by_id("save-button")
			save_changes_button.click()
			WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.ID, "save-button")))

		# Customize
		customizeCharacterHelper("Body", body, body_color, True)
		customizeCharacterHelper("Brow", brow, brow_color, True)
		customizeCharacterHelper("Hair", hair, hair_color, True)
		customizeCharacterHelper("Eyes", eyes, eyes_color, True)
		customizeCharacterHelper("Face", face, "", False)
		customizeCharacterHelper("Nose", nose, "", False)
		customizeCharacterHelper("Lips", lips, lips_color, True)

	#def outfitCreate(character_name, body_type, outfit_name):
	# Click Outfit Button on Story Page
	#	WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='outfit-button']")))
	#	button_outfits = browser.find_element_by_id("outfit-button")
	#	button_outfits.click()

		# Search for Character's Default Outfit
	#	WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.XPATH, "//*[@class='asset-left-panel-search-bar'")))
	#	outfit_search_input = find_element_by_class_name("asset-left-panel-search-bar")
	#	outfit_search_input.click()

	#def customizeOutfit():

	#def createEpisode(text):

	#def shareGmail():

	#def publishStory():

if __name__ == '__main__':
	unittest.main()





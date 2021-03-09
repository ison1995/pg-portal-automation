# Automation for Portal QA Checklist
import time
import pyperclip
import calendar
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

class DevLibrary():
	def __init__(self, browser):
		self.URL = ""
		self.user_input_version = ""
		self.STORY = ""
		self.browser = browser 

	def urlSetup(self):
		# Asks user for which version of Portal to use 
		user_input_version = input("Which version do you want to sign into? Type in 'dev' for main dev: ")

		if user_input_version == "dev":
			URL = "https://pg-story-dev.appspot.com/"
		else:
			URL = "http://version"+user_input_version+"-dot-pg-story-dev.appspot.com/"

		# Assigns Variabless
		self.URL = URL
		self.user_input_version = user_input_version

	def closeWindow(self):
		self.browser.close()

	def closeDriver(self):
		self.browser.quit()

	def googleSignIn(self, user, pw):

		# Navigates to stackoverflow and presses the login button
		self.browser.get("https://stackoverflow.com/")
		button_stack_login_locator = '//a[@href="'+"https://stackoverflow.com/users/login?ssrc=head&returnurl=https%3a%2f%2fstackoverflow.com%2f"+'"]'
		WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, button_stack_login_locator)))
		button_stack_login = self.browser.find_element_by_xpath(button_stack_login_locator)
		time.sleep(1)
		button_stack_login.click()

		# Chooses to login via Google
		WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.CLASS_NAME, "s-btn__google")))
		button_stack_google = self.browser.find_element_by_class_name("s-btn__google")
		button_stack_google.click()

		# Enters Username 
		WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='identifierId']")))
		time.sleep(2)
		ActionChains(self.browser).send_keys(user).perform()
		time.sleep(2) # Simulates real person waiting
		ActionChains(self.browser).send_keys(Keys.RETURN).perform()

		# Enters Password
		google_password_input_xpath_locater = "//input[@name='password']"
		WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, google_password_input_xpath_locater)))
		google_password_input = self.browser.find_element_by_xpath(google_password_input_xpath_locater)
		google_password_input.send_keys(pw)
		time.sleep(2) # Simulates real person waiting
		ActionChains(self.browser).send_keys(Keys.RETURN).perform()
		time.sleep(2)

	def portalSignIn(self, url): 

		# Navigates to Episode Portal 
		self.browser.get(url)

		# Click "Create Story" button to scroll down
		WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.LINK_TEXT, "Create a Story")))
		button_createstory = self.browser.find_element_by_link_text("Create a Story")
		button_createstory.click()
		time.sleep(1) # Pauses for scroll to finish

		# Click Google Sign-in button
		WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.CLASS_NAME, "c-btn--g-plus")))
		button_googlesignin = self.browser.find_element_by_class_name("c-btn--g-plus")
		button_googlesignin.click() 
		time.sleep(1) # Pauses to fool Google's anti-bot
		
		# Uncheck Google Allow Check Box
		#checkbox_google_allow_locator = "input[id='persist_checkbox']"
		#checkbox_google_allow = self.browser.find_element_by_css_selector(checkbox_google_allow_locator)
		#checkbox_google_allow.click()
		#time.sleep(1) 

		# Press Google Allow Submit
		#button_google_allow = self.browser.find_element_by_name("submit_true") 
		#button_google_allow.click()

	def portalNewWriterTOS(self, url):
		try:
			# Checks the TOS checkbox
			checkbox_TOS_locator = "input[id='checkbox-tos']"
			WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, checkbox_TOS_locator)))
			checkbox_TOS = self.browser.find_element_by_css_selector(checkbox_TOS_locator)
			checkbox_TOS.click()
			time.sleep(1) # Wait to activate "Stat Writing!" button

			# Presses TOS Submit button
			button_submit_TOS_locator = "input[id='submit-tos']"
			WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, button_submit_TOS_locator)))
			button_submit_TOS = self.browser.find_element_by_css_selector(button_submit_TOS_locator)
			button_submit_TOS.click() 
			time.sleep(1)
		except: 
			print("TOS not found, continuing")

	def createNewStory(self, url, version_number):
		# Redirect to Home Page
		self.browser.get(url)
		time.sleep(1)

		# Close New Onboarding Flow Popup
		try:
			WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable((By.CLASS_NAME, "shepherd-cancel-icon")))
			button_close_onboarding = self.browser.find_element_by_class_name("shepherd-cancel-icon")
			button_close_onboarding.click()
		except:
			print("Onboarding Flow not found, continuing")

		# Create New Story Button Click
		WebDriverWait(self.browser, 30).until(EC.presence_of_element_located((By.LINK_TEXT, "New Story")))
		button_new_story = self.browser.find_element_by_link_text("New Story")
		button_new_story.click() # Click on "Create New Story" button

		# Input the Story Name and Submit
		WebDriverWait(self.browser, 30).until(EC.presence_of_element_located((By.ID, "new_story_name")))
		input_new_story = self.browser.find_element_by_id("new_story_name")
		input_new_story.clear()
		input_new_story.send_keys(version_number) # Adds the version# as the name
		button_new_story_submit = self.browser.find_element_by_id("new-story-submit")
		button_new_story_submit.click() # Submits the story name

		# Wait until "Characters" button is loaded on Story Home Page and get current url
		WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.LINK_TEXT, "Characters")))
		story_url = self.browser.current_url
		self.STORY = story_url

	def characterCreate(self, story_id_url, character_model, character_name, first_flag):
		# Go to Story Page
		self.browser.get(story_id_url)

		if first_flag == True:
			# Select Character Style and Formats
			WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.LINK_TEXT, "Characters")))
			button_characters = self.browser.find_element_by_link_text("Characters")
			button_characters.click()
			WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.LINK_TEXT, "Use Episode Limelight")))
			button_limelight = self.browser.find_element_by_link_text("Use Episode Limelight")
			button_limelight.click()
			WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.LINK_TEXT, "Use Episode Cinematic")))
			button_cinematic = self.browser.find_element_by_link_text("Use Episode Cinematic")
			button_cinematic.click()

		elif first_flag == False:
			# Just press "Characters" button
			WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.LINK_TEXT, "Characters")))
			button_characters = self.browser.find_element_by_link_text("Characters")
			button_characters.click()
			WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.LINK_TEXT, "New Character")))
			button_new_character = self.browser.find_element_by_link_text("New Character")
			button_new_character.click()

		# Creates Character
		WebDriverWait(self.browser, 30).until(EC.presence_of_element_located((By.NAME, "actor")))
		time.sleep(1)
		actor_locator = self.browser.find_element_by_name("actor")
		actor = Select(actor_locator)
		actor.select_by_visible_text(character_model)
		time.sleep(1)
		input_character_name = self.browser.find_element_by_name("name")
		input_character_name.click()
		ActionChains(self.browser).send_keys(character_name + Keys.RETURN).perform()

		# Wait for next page to load
		WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.LINK_TEXT, "New Character")))

		# Hard Assert if character has been created with character_name
		#display_name_selector = "//input[@value='" + character_name + "']"
		#display_name = self.browser.find_element_by_xpath(display_name_selector)

	def customizeCharacter(self, story_id_url, character_name, body, body_color, brow, brow_color, hair, hair_color, 
							eyes, eyes_color, face, nose, lips, lips_color):
		# Go to Story Page
		self.browser.get(story_id_url)

		# Press the Characters button
		WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.LINK_TEXT, "Characters")))
		button_characters = self.browser.find_element_by_link_text("Characters")
		button_characters.click()

		# Choose which Character to customize
		WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.LINK_TEXT, character_name)))
		button_character_toCustomize = self.browser.find_element_by_link_text(character_name)
		button_character_toCustomize.click()

		# Define Customize Helper Function
		def customizeCharacterHelper(part_toCustomize, part_toSelect, color_toSelect, color_flag):
			# Select Which Object to Customize
			button_toCustomize_xpath_selector = "//*[contains(text(), '" + part_toCustomize + "')]"
			WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, button_toCustomize_xpath_selector)))
			button_toCustomize = self.browser.find_element_by_xpath(button_toCustomize_xpath_selector)
			button_toCustomize.click()

			# Choose Customizable Object
			part_xpath_selector = "//p[text()='" + part_toSelect + "']"
			button_part_toChoose = self.browser.find_element_by_xpath(part_xpath_selector)
			button_part_toChoose.click()

			# Choose Color
			if color_flag == True:
				body_color_id = "color-cell-" + color_toSelect
				button_bodyColor_toChoose = self.browser.find_element_by_id(body_color_id)
				button_bodyColor_toChoose.click()

			# Save Changes and Wait for save to finish
			save_changes_button = self.browser.find_element_by_id("save-button")
			save_changes_button.click()
			WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.ID, "save-button")))

		# Customize
		customizeCharacterHelper("Body", body, body_color, True)
		customizeCharacterHelper("Brow", brow, brow_color, True)
		customizeCharacterHelper("Hair", hair, hair_color, True)
		customizeCharacterHelper("Eyes", eyes, eyes_color, True)
		customizeCharacterHelper("Face", face, "", False)
		customizeCharacterHelper("Nose", nose, "", False)
		customizeCharacterHelper("Lips", lips, lips_color, True)

	def removeFromExistingOutfit(self, story_id_url, outfit_name, asset_toRemove):
		# Go to Story Page
		self.browser.get(story_id_url)

		# Click Outfit Button on Story Page
		WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='outfit-button']")))
		button_outfits = self.browser.find_element_by_id("outfit-button")
		button_outfits.click()

		# Find Outfit and Click
		WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.ID, "outfits-list")))
		outfit_toCustomize_button = self.browser.find_element_by_link_text(outfit_name)
		outfit_toCustomize_button.click()

		# Find Asset and Remove 
		WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.ID, "outfits-list")))
		asset_toRemove_xpath_locater = "//div[contains(text(), '"+asset_toRemove+"')]/../img"
		asset_toRemove_button = self.browser.find_element_by_xpath(asset_toRemove_xpath_locater)
		asset_toRemove_button.click()

		# Save Outfit
		WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.ID, "outfit-save-button")))
		outfit_saveButton = self.browser.find_element_by_id("outfit-save-button")
		outfit_saveButton.click()

	def addToExistingOutfit(self, story_id_url, outfit_name, asset_toAdd):
		# Go to Story Page
		self.browser.get(story_id_url)

		# Click Outfit Button on Story Page
		WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='outfit-button']")))
		button_outfits = self.browser.find_element_by_id("outfit-button")
		button_outfits.click()

		# Find Outfit and Click
		WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.ID, "outfits-list")))
		outfit_toCustomize_button = self.browser.find_element_by_link_text(outfit_name)
		outfit_toCustomize_button.click()

		# Search Asset
		WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.ID, "outfit-search-box")))
		outfit_searchbox_xpath = "//*[@id='outfit-search-box']/input"
		outfit_searchbox = self.browser.find_element_by_xpath(outfit_searchbox_xpath)
		outfit_searchbox.send_keys(asset_toAdd)
		
		# Hover and Click Asset
		WebDriverWait(self.browser, 30).until(EC.presence_of_element_located((By.CLASS_NAME, "btn-toolbar")))
		outfit_before_hover = self.browser.find_element_by_xpath("//div[contains(text(), '"+asset_toAdd+"')]")
		ActionChains(self.browser).move_to_element(outfit_before_hover).perform()
		outfit_toAdd = self.browser.find_element_by_class_name("overlay-image")
		outfit_toAdd.click()

		# Save Outfit
		WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.ID, "outfit-save-button")))
		outfit_saveButton = self.browser.find_element_by_id("outfit-save-button")
		outfit_saveButton.click()
		
	def createNewOutfit(self, story_id_url, outfit_name, body_type, asset_toAdd):
		# Go to Story Page
		self.browser.get(story_id_url)

		# Click Outfit Button on Story Page
		WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='outfit-button']")))
		button_outfits = self.browser.find_element_by_id("outfit-button")
		button_outfits.click()	

		# Create New Outfit
		WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.ID, "new-outfit-button")))
		new_outfit_button = self.browser.find_element_by_id("new-outfit-button")
		new_outfit_button.click()

		# Name Outfit
		WebDriverWait(self.browser, 30).until(EC.presence_of_element_located((By.CLASS_NAME, "col-sm-9")))
		outfit_name_input_locater = "input[id='displayName']"
		outfit_name_input = self.browser.find_element_by_css_selector(outfit_name_input_locater)
		outfit_name_input.send_keys(outfit_name)

		# Choose Body Type from Dropdown
		WebDriverWait(self.browser, 30).until(EC.presence_of_element_located((By.ID, "categorized-body-type-dropdown")))
		body_type_dropdown = self.browser.find_element_by_id("categorized-body-type-dropdown")
		body_type_dropdown.click()
		body_type_toClick_xpath_locater = "//a[contains(text(), '"+body_type+"')]"
		body_type_toClick = self.browser.find_element_by_xpath(body_type_toClick_xpath_locater)
		body_type_toClick.click()

		# Search Initial Outfit
		WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.ID, "outfit-search-box")))
		outfit_searchbox_xpath = "//*[@id='outfit-search-box']/input"
		outfit_searchbox = self.browser.find_element_by_xpath(outfit_searchbox_xpath)
		outfit_searchbox.send_keys(asset_toAdd)
		
		# Hover and Click Asset
		WebDriverWait(self.browser, 30).until(EC.presence_of_element_located((By.CLASS_NAME, "btn-toolbar")))
		outfit_before_hover = self.browser.find_element_by_xpath("//div[contains(text(), '"+asset_toAdd+"')]")
		ActionChains(self.browser).move_to_element(outfit_before_hover).perform()
		outfit_toAdd = self.browser.find_element_by_class_name("overlay-image")
		outfit_toAdd.click()
		time.sleep(5)	

		# Save Outfit
		WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.ID, "outfit-save-button")))
		outfit_saveButton = self.browser.find_element_by_id("outfit-save-button")
		outfit_saveButton.click()

		# Wait for Webpage to finish saving
		WebDriverWait(self.browser, 30).until(EC.presence_of_element_located((By.LINK_TEXT, outfit_name)))

	def createEpisode(self, story_id_url, textfile_abs_path):
		# Go to Story Page
		self.browser.get(story_id_url)

		# Check for the Survey Pop Up
		try:
			survey_close_button_xpath_locater = "//div[@class='smcx-modal-close']"
			WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable((By.XPATH, survey_close_button_xpath_locater)))
			survey_close_button = self.browser.find_element_by_xpath(survey_close_button_xpath_locater)
			survey_close_button.click()
		except:
			print("Survey not found. Continuing.")

		# Create a new Episode 
		new_episodeButton = self.browser.find_element_by_id("episode-button")
		new_episodeButton.click()

		# Copy Contents of Text File
		with open(textfile_abs_path) as file:
			data = file.read()
			pyperclip.copy(data)

		# Define Story Editor
		story_editor_xpath_locater = "//*[contains(@class, 'ace_layer ace_text-layer')]/div"
		WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.ID, "savebtn")))
		story_editor = self.browser.find_element_by_xpath(story_editor_xpath_locater)

		# Clicks into Story Editor
		ActionChains(self.browser) \
			.move_to_element(story_editor) \
			.click(story_editor) \
			.perform()

		# Pastes Content into Story Editor (MAC ONLY)
		ActionChains(self.browser) \
			.key_down(Keys.COMMAND) \
			.send_keys("a") \
			.send_keys("v") \
			.perform()

		# Save Episode
		chapter_preview_button_xpath_locater = "//a[contains(text(), 'Save And Preview')]"
		WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, chapter_preview_button_xpath_locater)))
		
		ActionChains(self.browser) \
		.key_down(Keys.COMMAND) \
		.send_keys("s") \
		.perform()

		# Wait for Save to Finish
		savedNotification_xpath_locater = "//span[contains(text(), 'Chapter saved.')]"
		WebDriverWait(self.browser, 30).until(EC.presence_of_element_located((By.XPATH, savedNotification_xpath_locater)))

	def closeSurvey(self):
		try:
			WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.CLASS_NAME, "smcx-modal-close")))
			survey_close_button = self.browser.find_element_by_class_name("smxc-modal-close")
			survey_close_button.click()
		except:
			print("Survey not found. Continuing.")

	def shareGmail(self, story_id_url, email_toShare):
		# Go to Story Page
		self.browser.get(story_id_url)

		# Click on the Gmail Icon
		gmail_shareButton_xpath_locater = "//a[@class='at-icon-wrapper at-share-btn at-svc-gmail']"
		WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, gmail_shareButton_xpath_locater)))
		gmail_shareButton = self.browser.find_element_by_xpath(gmail_shareButton_xpath_locater)
		gmail_shareButton.click()
		time.sleep(1)

		# Insert Email into recipients 
		self.browser.switch_to_window(self.browser.window_handles[1])
		gmail_recipient_input_xpath_locater = "//textarea[@id=':o6']"
		WebDriverWait(self.browser, 30).until(EC.presence_of_element_located((By.XPATH, gmail_recipient_input_xpath_locater)))
		gmail_recipient_input = self.browser.find_element_by_xpath(gmail_recipient_input_xpath_locater)
		gmail_recipient_input.send_keys(email_toShare)

		# Press the Send button
		gmail_sendButton_xpath_locater = "//div[@id=':oy']"
		gmail_sendButton = self.browser.find_element_by_xpath(gmail_sendButton_xpath_locater)
		gmail_sendButton.click()

		# Refocus on Main Tab
		self.browser.switch_to_window(self.browser.window_handles[0])

	def publishStory(self, story_id_url, author_name, story_description, num_episodes):
		# Go to Story Page
		self.browser.get(story_id_url)

		# Click on Publish Button 
		WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.ID, "submit-button")))
		publish_button = self.browser.find_element_by_id("submit-button")
		publish_button.click()
		
		# Input Author Name
		author_name_xpath_locater = "//div[contains(text(), 'Author Name')]/following-sibling::input"
		WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, author_name_xpath_locater)))
		time.sleep(1)
		author_name_input = self.browser.find_element_by_xpath(author_name_xpath_locater)
		author_name_input.send_keys(author_name)

		# Input Description
		story_description_input_xpath_locater = "//textarea[@placeholder='Write a brief description of your story']"
		WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, story_description_input_xpath_locater)))
		story_description_input = self.browser.find_element_by_xpath(story_description_input_xpath_locater)
		story_description_input.send_keys(story_description)

		# Check the TOS Publishing Box
		TOS_publishing_box = self.browser.find_element_by_id("publishing-agree-tos")
		TOS_publishing_box.click()

		# Publish
		final_publish_button_xpath_locater = "//button[@ng-click='publishStory()']"
		WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, final_publish_button_xpath_locater)))
		final_publish_button = self.browser.find_element_by_xpath(final_publish_button_xpath_locater)
		final_publish_button.click()

	def waitUser(self):
		user_permission = input("Ready to proceed? y/n ")
		result = False

		if user_permission == "y":
			result = True
		else:
			result = False

		return result

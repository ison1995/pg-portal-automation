from checklists.library.portal_selenium_library import DevLibrary

class devReleaseChecklist():
	def __init__(self, browser):
		self.lib = DevLibrary(browser)
		self.text_file = "/Users/isaacson/Downloads/Repos/pg-portal-automation/scripts/checklists/library/files/episode_sample_text.txt"
		# TODO: When the library fragments, this section and relevant functions need to be updated to 
		# handle the persistent variables here instead of the library. The library of functions should 
		# NOT hold any persistent variables like STORY or URL

	def step_GoogleSignIn(self):
		self.lib.googleSignIn("episodeisaacqa@gmail.com", "Tapfarm1")

	def step_PortalSignIn(self):
		self.lib.portalSignIn(self.lib.URL)
		self.lib.portalNewWriterTOS(self.lib.URL)

	def step_StoryCreate(self):
		self.lib.createNewStory(self.lib.URL, self.lib.user_input_version)

	def step_CharacterCreate(self): # Testing Character Creation
		self.lib.characterCreate(self.lib.STORY, "PEARL", "FEMALE", True)
		self.lib.characterCreate(self.lib.STORY, "CHARLIE", "MALE", False)
		self.lib.characterCreate(self.lib.STORY, "RENEE", "FEMALEPLUS", False)

	def step_CharacterCustomize(self): # Testing Character Customization
		self.lib.customizeCharacter(self.lib.STORY, "FEMALE", "Female Generic Body", "Ash01", "Arched Short", 
							"greenMint", "Beach Wave Hair", "BluePastel", "Deepset Downturned", 
							"violet", "Diamond Long", "Defined Natural", "Full Heart Pouty", 
							"pinkDeepGloss")
		self.lib.customizeCharacter(self.lib.STORY, "MALE", "Male Generic Body", "BeigeNeutral2", "Arched Medium", 
							"BlondeHoney", "Conservative Cut", "BrownMedium", "Deepset Heavy Lid",
							"hazel", "Chiseled Angular", "Button Wide", "Full Heart Natural",
							"brownNeutral")
		self.lib.customizeCharacter(self.lib.STORY, "FEMALEPLUS", "Female Plus Skin", "BeigeGold", "Arched Thick Styled",
							"WhiteWarm", "Layered Wavy Bob", "BlondeAsh", "Deepset Almond", 
							"red", "Heart Defined", "Grecian Soft", "Full Wide",
							"orangeBloodMatte")

	def step_OutfitsCreate(self): # Testing Outfit Creation
		self.lib.createNewOutfit(self.lib.STORY, "FEMALE_Outfit", "Generic Female", 
						"Turtleneck Sweater And High Waisted Pants Cotton White")
		self.lib.createNewOutfit(self.lib.STORY, "MALE_Outfit", "Generic Male", 
						"One Piece Suit Jacket Cotton Blue Purple")
		self.lib.createNewOutfit(self.lib.STORY, "FEMALEPLUS_Outfit", "Plus Female", 
						"Button Up Denim Dress T Shirt Layered Denim Blue White")

	def step_ChaptersCreate(self): # Testing Chapter Creation
		self.lib.createEpisode(self.lib.STORY, self.text_file)
		self.lib.createEpisode(self.lib.STORY, self.text_file)
		self.lib.createEpisode(self.lib.STORY, self.text_file)

	def step_ShareGmail(self): # Testing Gmail Sharing 
		self.lib.shareGmail(self.lib.STORY, "pocketgemstestiap@gmail.com")

	def step_StoryPublish(self): # Testing Story Publishing 
		permission = False
		while permission == False:
			permission = self.lib.waitUser()
			if permission == True:
				break
		self.lib.publishStory(self.lib.STORY, "TEST_AUTHOR", "TEST_DESCRIPTION", 3)



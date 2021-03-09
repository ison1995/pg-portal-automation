from selenium_library.portal_selenium_library import DevLibrary

# Dev Checklist 

# Setup
dev_test_run = DevLibrary()
dev_test_run.urlSetup()

# Sign In
dev_test_run.googleSignIn("episodeisaacqa@gmail.com", "Tapfarm1")
dev_test_run.portalSignIn(dev_test_run.url)
dev_test_run.portalNewWriterTOS(dev_test_run.url)

# Story Create -- Creates the story URL to use for the rest of the testing run
STORY = dev_test_run.createNewStory(dev_test_run.url, dev_test_run.user_input_version)

# Character Create -- Creates the test characters
dev_test_run.characterCreate(STORY, "PEARL", "FEMALE", True)
dev_test_run.characterCreate(STORY, "CHARLIE", "MALE", False)
dev_test_run.characterCreate(STORY, "RENEE", "FEMALEPLUS", False)

# Character Customization -- Customizes each character 
dev_test_run.customizeCharacter(STORY, "FEMALE", "Female Generic Body", "Ash01", "Arched Short", 
							"greenMint", "Beach Wave Hair", "BluePastel", "Deepset Downturned", 
							"violet", "Diamond Long", "Defined Natural", "Full Heart Pouty", 
							"pinkDeepGloss")
dev_test_run.customizeCharacter(STORY, "MALE", "Male Generic Body", "BeigeNeutral2", "Arched Medium", 
							"BlondeHoney", "Conservative Cut", "BrownMedium", "Deepset Heavy Lid",
							"hazel", "Chiseled Angular", "Button Wide", "Full Heart Natural",
							"brownNeutral")
dev_test_run.customizeCharacter(STORY, "FEMALEPLUS", "Female Plus Skin", "BeigeGold", "Arched Thick Styled",
							"WhiteWarm", "Layered Wavy Bob", "BlondeAsh", "Deepset Almond", 
							"red", "Heart Defined", "Grecian Soft", "Full Wide",
							"orangeBloodMatte")

# Outfit Create -- Creates new outfits for each character to change into
dev_test_run.createNewOutfit(STORY, "FEMALE_Outfit", "Generic Female", "Turtleneck Sweater And High Waisted Pants Cotton White")
dev_test_run.createNewOutfit(STORY, "MALE_Outfit", "Generic Male", "One Piece Suit Jacket Cotton Blue Purple")
dev_test_run.createNewOutfit(STORY, "FEMALEPLUS_Outfit", "Plus Female", "Button Up Denim Dress T Shirt Layered Denim Blue White")

# Chapter Creation
dev_test_run.createEpisode(STORY, "/Users/isaacson/Downloads/Repos/pg-portal-automation/scripts/library/episode_sample_text.txt")
dev_test_run.createEpisode(STORY, "/Users/isaacson/Downloads/Repos/pg-portal-automation/scripts/library/episode_sample_text.txt")
dev_test_run.createEpisode(STORY, "/Users/isaacson/Downloads/Repos/pg-portal-automation/scripts/library/episode_sample_text.txt")

# Story Sharing
dev_test_run.shareGmail(STORY, "pocketgemstestiap@gmail.com")

# Story Publishing
permission = False
while permission == False:
	permission = dev_test_run.waitUser()
	if permission == True:
		break
dev_test_run.publishStory(STORY, "TEST_AUTHOR", "TEST_DESCRIPTION", 3)



# ----------------------------------#
#	TESTING PURPOSES
# ----------------------------------# 

# Setup (TEST)
#STORY = "https://pg-story-dev.appspot.com/write/story/dev_bK"

#test_run.urlSetup()
#test_run.googleSignIn("episodeisaacqa@gmail.com", "Tapfarm1")
#test_run.portalSignIn(test_run.url)

# Story Customization (TEST) DONE
#test_run.customizeCharacter(STORY, "FEMALE", "Female Athletic Body", "Ash01", "Arched Short", "greenMint", 
#	"Beach Wave Hair", "BluePastel", "Deepset Downturned", "violet", "Diamond Long", "Defined Natural", "Full Heart Pouty", "pinkDeepGloss")

# Outfit Customization (TEST) DONE
#test_run.removeFromExistingOutfit(STORY, "FEMALE_default", "Rippedleggingssimple Grey Black")
#test_run.addToExistingOutfit(STORY, "FEMALE_default", "Rippedleggingssimple Grey Black")
#test_run.createNewOutfit(STORY, "OUTFIT_NAME", "Plus Female", "Leg Hair Light")

# Copy and Paste Text Into Story Editor (TEST) DONE
#test_run.createEpisode(STORY, "/Users/isaacson/Downloads/Repos/pg-portal-automation/scripts/library/episode_sample_text.txt")

# Share Story via Gmail (TEST) DONE
#test_run.shareGmail(STORY, "pocketgemstestiap@gmail.com")

# Publish Story (TEST) IN PROGRESS
#test_run.publishStory(STORY, "TEST", "TEST", 3)







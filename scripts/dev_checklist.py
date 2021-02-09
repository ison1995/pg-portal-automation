from library.portal_selenium_library import DevChecklist

# Dev Checklist 

# Setup
test_run = DevChecklist()
#test_run.urlSetup()

# Sign In
#test_run.googleSignIn("episodeisaacqa@gmail.com", "Tapfarm1")
#test_run.portalSignIn(test_run.url)
#test_run.portalNewWriterTOS(test_run.url)

# Story Setup
#STORY = test_run.createNewStory(test_run.url, test_run.user_input_version)
#test_run.test_characterCreate(STORY, "PEARL", "FEMALE", True)
#test_run.test_characterCreate(STORY, "CHARLIE", "MALE", False)
#test_run.test_characterCreate(STORY, "RENEE", "FEMALEPLUS", False)


# ----------------------------------#
#	TESTING PURPOSES
# ----------------------------------# 

# Setup (TEST)
STORY = "https://pg-story-dev.appspot.com/write/story/dev_bK"

# Sign In (TEST)
test_run.urlSetup()
test_run.googleSignIn("episodeisaacqa@gmail.com", "Tapfarm1")
test_run.portalSignIn(test_run.url)

# Story Customization (TEST) DONE
#test_run.customizeCharacter(STORY, "FEMALE", "Female Athletic Body", "Ash01", "Arched Short", "greenMint", 
#	"Beach Wave Hair", "BluePastel", "Deepset Downturned", "violet", "Diamond Long", "Defined Natural", "Full Heart Pouty", "pinkDeepGloss")

# Outfit Customization (TEST) DONE
#test_run.removeFromExistingOutfit(STORY, "FEMALE_default", "Rippedleggingssimple Grey Black")
#test_run.addToExistingOutfit(STORY, "FEMALE_default", "Rippedleggingssimple Grey Black")
#test_run.createNewOutfit(STORY, "OUTFIT_NAME", "Plus Female", "Leg Hair Light")

# Copy and Paste Text Into Story Editor (TEST) IN PROGRESS
test_run.createEpisode(STORY, "/Users/isaacson/Downloads/Repos/pg-portal-automation/scripts/library/episode_sample_text.txt")
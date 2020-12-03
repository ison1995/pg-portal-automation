from library.portal_selenium_library import EpisodePortalAutomation

# Dev Checklist 

# Setup
test_run = EpisodePortalAutomation()
test_run.urlSetup()

# Sign In
test_run.googleSignIn("episodeisaacqa@gmail.com", "Tapfarm1")
test_run.portalSignIn(test_run.url)
test_run.portalNewWriterTOS(test_run.url)

# Story Setup
STORY = test_run.createNewStory(test_run.url, test_run.user_input_version)
FEMALE_CHAR = test_run.test_characterCreate(STORY, "PEARL", "FEMALE", True)
MALE_CHAR = test_run.test_characterCreate(STORY, "CHARLIE", "MALE", False)
FEMALEPLUS_CHAR = test_run.test_characterCreate(STORY, "RENEE", "FEMALEPLUS", False)

# Story Customization
#customizeCharacter(FEMALE_CHAR, TESTBODY", "TESTBROW", "TESTHAIR", "TESTEYES", "TESTFACE", "TESTNOSE", "TESTLIPS")
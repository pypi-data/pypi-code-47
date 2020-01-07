from tv2test.display import Region

def constant(f):
    def fset(self, value):
        raise TypeError
    def fget(self):
        return f()
    return property(fget, fset)


class ConstTestCaseFailReason():
    @constant
    def BELL_LOGO_NOT_FOUND():
        return "Bell logo launch timeout"    
    @constant
    def YOUTUBE_LAUNCH_TIMEOUT():
        return "Youtube launch timeout"
    @constant
    def BELL_APP_LAUNCHER_TIMEOUT():
        return "Bell app launcher launch timeout"
    @constant
    def WEATHER_NETWORK_LANUCH_TIMEOUT():
        return "Weather network launch timeout"
    @constant
    def VOD_LAUNCH_FROM_MENU_TIMEOUT():
        return "VOD launch from the menu, timout"
    @constant
    def VOD_LAUNCH_TIMEOUT():
        return "VOD launch timout"
    @constant
    def VOD_EMPTY_TEXT():
        return "text not found"
    @constant
    def POSTER_DETECTION_FAIL():
        return "poster not detected"
    @constant
    def MY_FIBE_ICON_TIMEOUT():
        return "My fibe icon launch timeout"
    @constant
    def TC_DEFAULT_PAGE_TEXT_LOAD_TIMEOUT():
        return "Verification of \"Continue enjoying\" and \"My list\" failed"
    @constant
    def ASSET_MATCHED_FAILED():
        return "Asset match failed"
    @constant
    def MOTION_DETECTION_FAILED():
        return "Motion detection failed"
    @constant
    def SEASONS_TITLES_MATCH_FAILED():
        return "Matching of season's title failed"
    @constant
    def SEASONS_MATCH_FAILED():
        return "Seasons match failed"
    @constant
    def TEXT_NOT_FOUND():
        return "Text \"%s\" not found"
    @constant
    def ASSET_TITLES_MATCH_FAILED():
        return "Asset titles match failed"
    @constant
    def CATEGORY_MATCH_FAILED():
        return "Categories match failed"
    @constant
    def CATEGORY_MATCH_FAILED():
        return "Categories match failed"
    @constant
    def NETFLIX_LAUNCH_TIMEOUT():
        return "Netflix launch timeout"
    @constant
    def MOVIE_OR_SEASON_NOT_FOUND():
        return "Movie or Season not found"
    @constant
    def VERIFICATION_TIME_OUT():
        return "verification time out"
    @constant
    def TIME_NOT_FOUND():
        return "Time not found"
    @constant
    def FORWARD_COMMAND_FAIL():
        return "Foward voice command failed"
    @constant
    def RECORING_NOT_LOADED():
        return "Recording screen didn't load"
    @constant
    def NO_RECORING_FOUND():
        return "There were no recordings"
    @constant
    def PLAY_BTN_NOT_FOUND():
        return "Play button not found"
    @constant
    def CURRENT_CHANNEL_NOT_DETECTED():
        return "Failed to detect current channel"
    @constant
    def CHANNEL_NOT_DETECTED():
        return "Failed to detect channel"
    @constant
    def CHANNEL_DOWN_COMMAND_FAILED():
        return "Channel down voice commmand failed"
    @constant
    def VOICE_COMMAND_FAILED():
        return "Voice commmand failed"
    @constant
    def TIME_NOT_DETECTED():
        return "Failed to detect time of the video"
    @constant   
    def TUNE_TO_CHANNEL_FAIL():
        return "Failed to tune the channel"
    
    def text_not_found(self,text):
        return self.TEXT_NOT_FOUND % text


class ConstDeviceNames():
    @constant
    def MEDIA_FIRST():
        return "mediafirst"

    @constant
    def MEDIA_ROOM():
        return "mediaroom"


class ConstElk():
    @constant
    def IDX_BELL_TEST_CASES():
        return "bell_test_cases"
    @constant
    def DOC_TEST_DETAILS():
        return "tc_details"


class ConstantPosterRegions():
    @constant
    def movie_poster_region():
        movie_regions = Region(84, 242, 492, 300)
        return movie_regions

    @constant
    def series_poster_region():
        series_regions = Region(82, 706,492,300)
        return series_regions


class ConstTCType():
    @constant
    def BELL_TEST_CASE():
        return "BELL_TEST_CASE"
    @constant
    def BELL_VOICE_TEST_CASE():
        return "BELL_VOICE_TEST_CASE"
    @constant
    def BELL_VOD_TEST_CASE():
        return "BELL_VOD_TEST_CASE"

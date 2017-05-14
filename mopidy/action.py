class mopidy(object):

    def __init__(self, say, keyword):
        self.say = say
        self.keyword = keyword


    def get_playlist(self, playlist_name):

        return playlists[playlist_name]

    def run(self, voice_command):

        artist = voice_command.replace(self.keyword, '', 1)

        if (voice_command == "playlist stop") or (voice_command == "playlist off"):
            subprocess.call("mpc stop", shell=True)


        if self.keyword == "playlist":
            subprocess.call(["mpc clear && mpc load" + artist + "&& mpc shuffle && mpc play"], shell=True)

        if self.keyword == "skip":
            subprocess.call("mopidy-next")

        if self.keyword == "pause":
            subprocess.call("mopidy-pause")


        if self.keyword == "resume":
            subprocess.call("mopidy-resume")


        if self.keyword == "play":
            subprocess.call("mopidy-play")

        if self.keyword == "stop":
            subprocess.call("mpc stop")
            
            
            
# =========================================
# Makers! Add your own voice commands here.
# =========================================

    actor.add_keyword(_('music playlist'), mopidy(say, _('playlist')))
    actor.add_keyword(_('music skip'), mopidy(say, _('skip')))
    actor.add_keyword(_('music pause'), mopidy(say, _('pause')))
    actor.add_keyword(_('music play'), mopidy(say, _('play')))
    actor.add_keyword(_('music stop'), mopidy(say, _('stop')))
    actor.add_keyword(_('music resume'), mopidy(say, _('resume')))

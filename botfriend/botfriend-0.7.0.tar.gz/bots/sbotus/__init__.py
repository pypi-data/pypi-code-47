from .argument import Argument
from botfriend.bot import TextGeneratorBot
from nose.tools import set_trace

class SBOTUS(TextGeneratorBot):
    
    def generate_text(self):
        bot_state = self.model.json_state
        if not bot_state:
            argument_state = Argument.STARTING_STATE
            last_speaker = None
        else:
            argument_state = bot_state['argument_state']
            last_speaker = bot_state['last_speaker']

        toot = None
        argument = Argument(argument_state, last_speaker)
        while not toot or len(toot) < 100:
            lines, new_state, new_last_speaker = self.make_lines(argument)

            toot = "\n\n".join(lines)
            # Reset state in case we have to try again.
            argument.state = argument_state or argument.STARTING_STATE
            argument.last_speaker = last_speaker
        if argument.state == argument.ENDING_STATE:
            new_state = None
        self.model.json_state = dict(argument_state=new_state,
                                     last_speaker=new_last_speaker)
        return toot

    def make_lines(self, argument):
        lines = []
        as_string = ""
        previous_state = argument.state
        while len(as_string) < 500 and len(lines) < 2:
            previous_state = argument.state
            previous_last_speaker = argument.last_speaker

            # Try 5 times to add a random line that fits.
            found_match = False
            for i in range(5):
                speaker, utterance = argument.random_line()
                name = speaker['last_name']
                if not name:
                    name = "Unknown"
                if name.endswith(','):
                    name = name[:-1]
                line = "%s: %s" % (name, utterance['text'])
                as_string = "\n\n".join(lines + [line])
                if len(as_string) >= 500:
                    continue
                found_match = True
                break
            if found_match:
                # This is good.
                lines.append(line)
                # Move to the next state.
                argument.transition(speaker, utterance)
                if argument.finished:
                    # All done;
                    break
            if len(as_string) >= 400 and len(as_string) < 500:
                # Good enough; don't try again.
                break
        return lines, previous_state, previous_last_speaker

Bot = SBOTUS

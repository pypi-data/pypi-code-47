# Hello!
# Welcome to Threeza. You should have received an email like this:

def welcome_message(email_alias,private_key,public_key):
    return """<html> <p>You're in !</p>
<h2>Welcome to the Intech Supercollider Challenge</h2>
<p>Brought to you by <a href="https://www.intechinvestments.com/">Intech Investments</a> using the Algorithmia Marketplace, this game
pits your mathematical talent against the complex structure of stock movements. It requires you to deploy an algorithm that generates 10,000 samples
from the joint distribution of minutely price changes, every minute of the day. </p>
<h3>Start playing immediately</h3>
<p>You can immediately start participating by&nbsp;<a href="https://algorithmia.com/developers/algorithm-development/your-first-algo#create-your-first-algorithm">creating your first algorithm</a> in the Algorithmia marketplace and replacing any existing code with:&nbsp;</p>
<pre><span style="background-color: #ffffff;">from threeza import Futurithmia
Futurithmia.subscribe('intech_supercollider')

def apply(input):
    return Futurithmia.examples.samplers.empirical_sampler(input)</span><br />    </pre>
<p>Make sure to add "threeza" to the list of Algorithm dependencies (see&nbsp;<a href="https://algorithmia.com/developers/faqs/can-i-use-external-libraries">FAQ: dependencies</a>&nbsp;in the Algorithmia help). Then:&nbsp;</p>
<p>&nbsp; &nbsp; &nbsp; <span style="background-color: #99ccff; color: #ffffff;">Save</span>&nbsp;</p>
<p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;<span style="color: #ffffff;"><span style="background-color: #339966;">Build</span>&nbsp; &nbsp; &nbsp;</span></p>
<p><span style="color: #ffffff;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;<span style="background-color: #333399;">Publish</span></span>&nbsp;</p>
<p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; and start earning credits.</p>
<h3>Your alias</h3>
<p>Your communications alias is EMAIL_ALIAS. You can include this in the description of any challenge related Algorithmia you publish to let us know you wish to receive alerts and performance monitoring. Remove it when you don't.</p>
<h3>Your keys</h3>
<p><em>You may not need to know this</em> but your private key ending in <b>PRIVATE_KEY</b> has already been saved to your Algorithmia <a href="https://algorithmia.com/data/hosted/">data collection</a>. Never supply it to anyone. Your public key, already waved to the crowd, is <b>PUBLIC_KEY</b> </p>
<h3>Enjoy</h3>
<p>Thanks for helping with this experiment in collective probabilistic modeling of high dimensional joint distributions. See <a href="www.3za.org">www.3za.org</a> for more about this and other challenges.</p>

</html>""".replace("EMAIL_ALIAS",email_alias).replace("PRIVATE_KEY",private_key[-4:]).replace("PUBLIC_KEY",public_key)

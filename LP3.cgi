#! /usr/bin/env python3
print('Content-type: text/html\n')

import cgi

form = cgi.FieldStorage()   #parses form data
word = form.getfirst('word','None')
guess = form.getfirst('guess','None')
elven_trans_dict = {'lapse':'baby','wilin':'bird','parma':'book','yanta':'bridge','liikuma':'candle','meoi':'cat','lanne':'cloth','yulma':'cup','huo':'dog','fenume':'dragon','hen':'eye','taal':'foot','quaare':'hand','silmo':'moon','amon':'mountain','olva':'plant','malle':'road','lunte':'ship','alda':'tree','ramba':'wall'}
word_guess = elven_trans_dict.get(word,'incorrect')

if word_guess == guess:
    correct_or_not = "That's correct!"
else:
  correct_or_not = "Sorry, the correct answer was " + elven_trans_dict[word] + "."
    
img = "lp3img/" + word_guess +".jpg"   
    
html = """
<!doctype html>
<html>
<head><meta charset="utf-8">
<title>Elven Translation</title></head>
    <body>
        <p><img src="{0}"></p>
	<p><h2>{1}</h2></p>
	<br>
	<p>{2}</p>
    </body>
</html>"""

if word_guess != "That's correct!":
    next="""<form method="post" action="LP3_again.cgi">
    <p>Select a word to translate:
            <select name="word">
			<option>lapse</option>
			<option>wilin</option>
			<option>parma</option>
			<option>yanta</option>
			<option>liikuma</option>
			<option>meoi</option>
			<option>lanne</option>
			<option>yulma</option>
			<option>huo</option>
			<option>fenume</option>
			<option>hen</option>
			<option>taal</option>
			<option>quaare</option>
			<option>silmo</option>
			<option>amon</option>
			<option>olva</option>
			<option>malle</option>
			<option>lunte</option>
			<option>alda</option>
			<option>ramba</option>
		</select>
	</p>
        <br>
        <p>Enter your translation:
            <input type="text" name="guess">
        </p>
        <br>
            <button type="submit">Submit</button>
        </form>"""
else:
    next="""<form method="post" action="LP3_again.cgi">
    <p>Select a word to translate:
            <select name="word">
			<option>lapse</option>
			<option>wilin</option>
			<option>parma</option>
			<option>yanta</option>
			<option>liikuma</option>
			<option>meoi</option>
			<option>lanne</option>
			<option>yulma</option>
			<option>huo</option>
			<option>fenume</option>
			<option>hen</option>
			<option>taal</option>
			<option>quaare</option>
			<option>silmo</option>
			<option>amon</option>
			<option>olva</option>
			<option>malle</option>
			<option>lunte</option>
			<option>alda</option>
			<option>ramba</option>
		</select>
	</p>
        <br>
        <p>Enter your translation:
            <input type="text" name="guess">
        </p>
        <br>
            <button type="submit">Submit</button>
        </form>"""

print(html.format(img,correct_or_not,next))

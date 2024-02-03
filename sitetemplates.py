from flask import render_template

import resultifier
def home():
	return render_template('./template.html', current_score=int(resultifier.get_currentScore()))
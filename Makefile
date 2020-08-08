#countries = ["sk", "ro", "sl", "hr", "bg"]

sk1.csv : sk1.py
	python3 sk1.py
sk2.csv: sk2.py
	python3 sk2.py
ro1.csv : ro1.py
	python3 ro1.py
ro2.csv : ro2.py
	python3 sk1.py
sl1.csv : sl1.py
	python3 sk1.py
sl2.csv : sl2.py
	python3 sk1.py
hr1.csv : hr1.py
	python3 sk1.py
hr2.csv : hr2.py
	python3 sk1.py
bg1.csv : bg1.py
	python3 sk1.py
bg2.csv : bg2.py
	python3 sk1.py
opencorp_sample.csv : concat.sh sk1.csv sk2.csv ro1.csv ro2.csv sl1.csv sl2.csv hr1.csv hr2.csv bg1.csv bg2.csv
	sh concat.sh
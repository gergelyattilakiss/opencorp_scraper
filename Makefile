#countries = ["sk", "ro", "sl", "hr", "bg"]
opencorp_sample.csv : sk1.csv sk2.csv ro1.csv ro2.csv si1.csv si2.csv hr1.csv hr2.csv pl1.csv pl2.csv
	cat *.csv > where.csv
	sed -i 1i"name,country,city" where.csv
sk1.csv : sk1.py
	python3 sk1.py
sk2.csv: sk2.py
	python3 sk2.py
ro1.csv : ro1.py
	python3 ro1.py
ro2.csv : ro2.py
	python3 ro2.py
si1.csv : sl1.py
	python3 sl1.py
si2.csv : sl2.py
	python3 sl2.py
hr1.csv : hr1.py
	python3 hr1.py
hr2.csv : hr2.py
	python3 hr2.py
pl1.csv : pl1.py
	python3 pl1.py
pl2.csv : pl2.py
	python3 pl2.py
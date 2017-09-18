.ONESHELL:
build:
	cd app
	yarn build
	cp build/static/js/main*.js ../enchant/server/static/js/main.js
	cp build/static/css/main*.css ../enchant/server/static/css/main.css
	cd ..

run: build
	python run.py


clean:
	find . | grep -E "(__pycache__|\.pyc|\.pyo$$)" | xargs rm -rf
run:
	export FLASK_APP=cmd/main/main.py && \
	flask run


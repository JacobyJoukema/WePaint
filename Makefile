install:
	python3 -m pip install uvicorn fastapi

server:
	uvicorn server:app --reload
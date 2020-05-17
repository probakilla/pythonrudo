INTERP = python3
MAIN = src/main.py
TEST_MAIN = src/test_main.py

all: run

run:
	$(INTERP) $(MAIN)

test:
	$(INTERP) $(TEST_MAIN)

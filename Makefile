help:
	@echo
	@echo "Please use 'make <user>' where <user> is a valid username."

clean:
	@echo "Cleaning..."
	@rm -rf build/
	@echo "Done."

run:
	@echo "Running for ${user}...\n"
	@python freqtweets/freqtweets.py ${user}
	@echo "Done."

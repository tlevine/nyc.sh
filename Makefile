.PHONY: index.html test

index.html:
	rm -f index.html
	cat partials/head | tr -d '\n' >> index.html
	cat nyc.sh                     >> index.html
	cat partials/foot | tr -d '\n' >> index.html

test:
	urchin test

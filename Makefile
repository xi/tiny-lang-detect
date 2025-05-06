.PHONY: all
all: data/wili data/profiles

data/wili:
	@mkdir -p $@
	wget https://zenodo.org/records/841984/files/wili-2018.zip?download=1 -O /tmp/wili.zip
	unzip /tmp/wili.zip '*_test.txt' -d $@
	@rm /tmp/wili.zip

data/profiles:
	@mkdir -p $@
	wget https://github.com/DoodleBears/langdetect/archive/refs/heads/master.zip -O /tmp/langdetect.zip
	unzip -j /tmp/langdetect.zip 'langdetect-master/langdetect/profiles/*' -d $@
	@rm /tmp/langdetect.zip

.PHONY: clean
clean:
	rm -rf data

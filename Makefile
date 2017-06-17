BASEDIR=$(CURDIR)
OUTPUTDIR=$(BASEDIR)/public

FTP_HOST=ftp.fundor333.com
FTP_USER=fundor333.com
FTP_TARGET_DIR=/

SSH_HOST=localhost
SSH_PORT=22
SSH_USER=root
SSH_TARGET_DIR=/var/www

S3_BUCKET=my_s3_bucket

DROPBOX_DIR=~/Dropbox/Host/

DEBUG ?= 0
ifeq ($(DEBUG), 1)
	PELICANOPTS += -D
endif

RELATIVE ?= 0
ifeq ($(RELATIVE), 1)
	PELICANOPTS += --relative-urls
endif

help:
	@echo 'Makefile for a Hugo Web site                                           '
	@echo '                                                                          '
	@echo 'Usage:                                                                    '
	@echo '   make clean                          remove the generated files         '
	@echo '   make publish                        generate using production settings '
	@echo '   make dropbox_upload                 upload the web site via Dropbox    '
	@echo '   make dev                            start a local dev server           '
	@echo '                                                                          '
	@echo 'Set the DEBUG variable to 1 to enable debugging, e.g. make DEBUG=1 html   '
	@echo 'Set the RELATIVE variable to 1 to enable relative urls                    '
	@echo '                                                                          '

clean:
	[ ! -d $(OUTPUTDIR) ] || rm -rf $(OUTPUTDIR)

publish: clean
	hugo

dropbox_upload: publish
	cp -r $(OUTPUTDIR)/* $(DROPBOX_DIR)

ftp_upload: publish
	lftp ftp://$(FTP_USER)@$(FTP_HOST) -e "mirror -R $(OUTPUTDIR) $(FTP_TARGET_DIR) ; quit"


dev:
	hugo server --watch --buildDrafts

.PHONY: help
help: ## Show this help
	@egrep -h '\s##\s' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

develop: ## Run the site localy
	hugo server --disableFastRender 

developfuture: ## Run the site localy with all the future article
	hugo server --disableFastRender --buildFuture 

developall: ## Run the site localy with all the article, future or drafts
	hugo server --disableFastRender --buildFuture --buildDrafts

clean: ## Clean the directory of the project of chache e meta file
	hugo --gc

.PHONY: new
new: ## Make new object for the blog
	python make-post.py

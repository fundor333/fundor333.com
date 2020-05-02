develop:
	hugo server --disableFastRender 

developfuture:
	hugo server --disableFastRender --buildFuture 

developall:
	hugo server --disableFastRender --buildFuture --buildDrafts

clean-resorce:
	hugo --gc

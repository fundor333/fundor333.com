develop:
	hugo server --disableFastRender & sass --watch themes/f333/static/css/style.scss:themes/f333/static/css/style.css --style compressed

developfuture:
	hugo server --disableFastRender --buildFuture & sass --watch themes/f333/static/css/style.scss:themes/f333/static/css/style.css --style compressed

developall:
	hugo server --disableFastRender --buildFuture --buildDrafts & sass --watch themes/f333/static/css/style.scss:themes/f333/static/css/style.css --style compressed

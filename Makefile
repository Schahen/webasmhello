
setup:
	rustup target add wasm32-unknown-unknown --toolchain nightly 
	cargo +nightly build --target wasm32-unknown-unknown
	npm install

build:
	cargo +nightly build --target wasm32-unknown-unknown
	wasm-bindgen target/wasm32-unknown-unknown/debug/webasmhello.wasm --out-dir target/bindgen
	node node_modules/webpack/bin/webpack.js app.js --output-path target/dist
	cp index.html target/dist/index.html


const rust = import("./target/bindgen/webasmhello");
rust.then(m => m.greet("LALALALALA!"));

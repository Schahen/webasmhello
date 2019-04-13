import kotlinx.interop.wasm.dom.*
import kotlinx.wasm.jsinterop.*

fun main(args: Array<String>) {
    alert("Hello!!!!")
}


@SymbolName("alert")
external public fun alert(msg: String)



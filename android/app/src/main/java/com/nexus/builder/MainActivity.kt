package com.nexus.builder

import android.app.Activity
import android.os.Bundle
import android.webkit.JavascriptInterface
import android.webkit.WebView
import android.webkit.WebViewClient
import org.json.JSONArray
import org.json.JSONObject
import java.io.File
import java.util.UUID

class MainActivity : Activity() {
    private lateinit var web: WebView

    override fun onCreate(state: Bundle?) {
        super.onCreate(state)
        web = WebView(this)
        web.settings.javaScriptEnabled = true
        web.settings.domStorageEnabled = true
        web.settings.allowFileAccess = true
        web.webViewClient = WebViewClient()
        web.addJavascriptInterface(NexusBridge(), "NexusNative")
        web.loadUrl("file:///android_asset/index.html")
        setContentView(web)
    }

    inner class NexusBridge {
        private fun projectsRoot() = File(filesDir, "projects").apply { mkdirs() }

        @JavascriptInterface
        fun systemInfo(): String {
            val rt = Runtime.getRuntime()
            return JSONObject()
                .put("android", android.os.Build.VERSION.RELEASE)
                .put("device", android.os.Build.MODEL)
                .put("cores", rt.availableProcessors())
                .put("maxMemoryMb", rt.maxMemory() / 1048576)
                .put("abi", android.os.Build.SUPPORTED_ABIS.firstOrNull() ?: "unknown")
                .toString()
        }

        @JavascriptInterface
        fun createProject(name: String, type: String): String {
            val safe = name.replace(Regex("[^A-Za-z0-9 _-]"), "").trim().ifBlank { "Projeto" }
            val dir = File(projectsRoot(), safe + "-" + UUID.randomUUID().toString().take(5)).apply { mkdirs() }
            File(dir, "project.json").writeText(JSONObject().put("name", safe).put("type", type).toString(2))
            when (type) {
                "game" -> File(dir, "index.html").writeText("<!doctype html><meta name='viewport' content='width=device-width'><body style='background:#07101f;color:white;font-family:sans-serif'><h1>$safe</h1><canvas id='c' width='320' height='480'></canvas><script>const c=document.querySelector('#c'),g=c.getContext('2d');let x=10;setInterval(()=>{g.fillStyle='#07101f';g.fillRect(0,0,320,480);g.fillStyle='#80aaff';g.fillRect(x,220,24,24);x=(x+3)%296},16)</"+"script>")
                "web" -> File(dir, "index.html").writeText("<!doctype html><meta name='viewport' content='width=device-width'><title>$safe</title><style>body{background:#081020;color:#eef;font-family:sans-serif;padding:30px}</style><h1>$safe</h1><p>Projeto criado pela Nexus.</p>")
                else -> File(dir, "README.txt").writeText("$safe\nProjeto criado pela Nexus.")
            }
            return JSONObject().put("ok", true).put("name", safe).put("path", dir.absolutePath).toString()
        }

        @JavascriptInterface
        fun listProjects(): String = JSONArray(projectsRoot().listFiles()?.filter { it.isDirectory }?.map { it.name } ?: emptyList<String>()).toString()

        @JavascriptInterface
        fun saveMemory(text: String): String {
            File(filesDir, "nexus-memory.txt").appendText(text.trim() + "\n")
            return "OK"
        }
    }

    @Deprecated("Deprecated in Java")
    override fun onBackPressed() {
        if (::web.isInitialized && web.canGoBack()) web.goBack() else super.onBackPressed()
    }
}
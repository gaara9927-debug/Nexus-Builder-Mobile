package com.nexus.builder
import android.app.Activity
import android.os.Bundle
import android.webkit.WebView
import android.webkit.WebViewClient
class MainActivity:Activity(){
 override fun onCreate(b:Bundle?){super.onCreate(b)
  val w=WebView(this); w.settings.javaScriptEnabled=true; w.settings.allowFileAccess=true
  w.webViewClient=WebViewClient(); w.loadUrl("file:///android_asset/index.html"); setContentView(w)
 }
 override fun onBackPressed(){val w=findViewById<WebView>(android.R.id.content).rootView as? WebView;if(w?.canGoBack()==true)w.goBack() else super.onBackPressed()}
}

# Local AI
Nexus does not bundle a multi-gigabyte model. A GGUF file is selected/downloaded by the user after hardware checks. LocalAIRuntime verifies the file hash, then uses llama.cpp through llama-cpp-python when that runtime is available. Missing runtime/model is BLOCKED, never reported as PASS. Android packaging needs a native llama.cpp/JNI integration and remains a separate release gate.

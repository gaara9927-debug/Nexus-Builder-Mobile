# Nexus architecture
Nexus separates language/model runtime from deterministic tools. Tool calls pass through validation, permission policy and workspace isolation. Secrets stay outside projects. Local API binds to loopback by default. Optional hardware/provider capabilities remain BLOCKED until actually configured and tested.

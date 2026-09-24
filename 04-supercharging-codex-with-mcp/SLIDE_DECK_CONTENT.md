# Slide Deck Content: Supercharging OpenAI Codex with Model Context Protocol (MCP)

> **Template Note:** Use the official Pluralsight Audition PowerPoint Template (`.pptx`). 
> **Pacing Rule:** Slide/visual changes every 20–30 seconds. All bullets animated to appear on-click.

---

### Slide 1: Title Slide
* **Layout:** `Title Slide`
* **Title:** Supercharging OpenAI Codex with MCP
* **Subtitle:** Connecting AI Agents to Live Development Context via Model Context Protocol
* **Author:** [Your Name]
* **Credentials/Handle:** AI Systems Architect | @YourHandle
* **Duration:** 0:00 – 0:25 (25 seconds)

---

### Slide 2: Overview / WIIFM
* **Layout:** `Overview/Summary`
* **Header:** What's In It For You?
* **Subheader:** Beyond the Code-Only Sandbox
* **Bullets (Animate On Click):**
  1. *The Blind Spot:* An AI model trapped in a code sandbox cannot see database tables, running services, or live schemas.
  2. *The MCP Breakthrough:* Model Context Protocol (MCP) standardizes how AI agents query external tools and environments securely.
  3. *Today's Goal:* Configure an MCP server in OpenAI Codex to diagnose and resolve an otherwise invisible database schema mismatch.
* **Duration:** 0:25 – 1:10 (45 seconds)

---

### Slide 3: The Runtime Context Gap
* **Layout:** `Two Text Chunking`
* **Header:** The Problem: The Runtime Blind Spot
* **Left Column:**
  * **What the Code Shows**
  * `User(username="alex", email="alex@work.com")`
  * Looks 100% syntactically valid in the Python file.
* **Right Column:**
  * **What the Live Database Demands**
  * Migration added `tenant_id NOT NULL`.
  * Runtime crashes with `IntegrityError`.
  * AI cannot see the live DB table schema without MCP.
* **Duration:** 1:10 – 1:40 (30 seconds)

---

### Slide 4: What is Model Context Protocol (MCP)?
* **Layout:** `Three Text Chunking`
* **Header:** The Open Standard for AI Connectivity
* **Column 1:**
  * **1. Resources**
  * Read-only data streams (e.g. database schemas, server logs, API documentation).
* **Column 2:**
  * **2. Tools**
  * Executable functions that the AI can call (e.g. `inspect_table`, `run_query`).
* **Column 3:**
  * **3. Prompts**
  * Standardized templates exposed by the server to guide the model.
* **Duration:** 1:40 – 2:10 (30 seconds)

---

### Slide 5: Configuring MCP in OpenAI Codex
* **Layout:** `Code Notes Dark`
* **Header:** Declarative MCP Configuration
* **Code / Text Box:**
  ```json
  {
    "mcpServers": {
      "sqlite-dev": {
        "command": "python",
        "args": ["mcp_server.py"],
        "env": { "DB_PATH": "database.sqlite" }
      }
    }
  }
  ```
* **Duration:** 2:10 – 2:45 (35 seconds)

---

### Slide 6: Important Statement
* **Layout:** `Important Statement` (Solid teal accent background)
* **Statement:** "An AI that only sees source code is guessing. An AI with MCP is verifying."
* **Supporting Note:** 
  * Granting Codex read-only tool access bridges the gap between static text and real-world system state.
* **Duration:** 2:45 – 3:30 (45 seconds)

---

### Slide 7: Demo Transition Slide
* **Layout:** `Demo (Optional)`
* **Title:** Hands-On Demo
* **Subtitle:** Solving a Hidden Schema Mismatch with Codex & MCP
* **Duration:** 3:30 – 3:45 (15 seconds)

---

### [LIVE DEMO SCREENCAST: 3:45 – 6:45 (3 minutes)]
* **Environment:** VS Code with Codex panel. Terminal at 125% zoom, post-production callouts.

---

### Slide 8: Summary & Key Takeaways
* **Layout:** `Overview/Summary`
* **Header:** Summary: Practical Takeaways
* **Bullets (Animate On Click):**
  1. *Bridge the Context Gap:* Connect Codex to real-time resources using the open Model Context Protocol.
  2. *Configure Safely:* Use declarative JSON configurations with principle of least privilege (read-only introspection).
  3. *Empower Autonomous Debugging:* Let Codex inspect live schemas directly rather than copying and pasting error logs.
* **Duration:** 6:45 – 7:15 (30 seconds)

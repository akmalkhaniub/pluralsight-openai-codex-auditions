# Timed Narration Script: Supercharging OpenAI Codex with Model Context Protocol (MCP)

* **Target Video Length:** 7 minutes 15 seconds
* **Audio Track Standard:** High-fidelity studio voice recording, 48kHz / 24-bit, separate audio channel, zero clicks/background noise.
* **Screen Resolution:** 1920x1080 at 125% IDE scale.

---

### [0:00 - 0:25] Slide 1: Title Slide
* **Visual:** Slide 1 displayed.
* **Speaker Tone:** Tech-forward, engaging, confident.
* **Narration:**
> "Hello everyone, and welcome! My name is [Your Name]. In this session, we’re learning how to **Supercharge OpenAI Codex with the Model Context Protocol**, or MCP."
> 
> *[1-second pause]*
> 
> "OpenAI Codex is exceptional at writing and editing code. But in production software development, code doesn't exist in a vacuum—it depends on live databases, environment variables, and external services."

---

### [0:25 - 1:10] Slide 2: Overview / WIIFM
* **Visual:** Slide 2 displayed. Click bullets in sync.
* **Speaker Tone:** Inspiring, problem-focused.
* **Narration:**
> *[Click Bullet 1]*  
> "When an AI is trapped inside a code-only sandbox, it's essentially flying blind. If an error is caused by a live database schema change or an external infrastructure mismatch, the AI can only hallucinate guesses.  
> 
> *[Click Bullet 2]*  
> That is where the Model Context Protocol comes in. MCP is an open standard that allows AI agents to securely connect to external tools, databases, and APIs.  
> 
> *[Click Bullet 3]*  
> By the end of this audition, you’ll know how to configure MCP inside OpenAI Codex so your AI can query live system schemas and solve complex runtime bugs autonomously."

---

### [1:10 - 1:40] Slide 3: The Runtime Context Gap
* **Visual:** Slide 3 displayed. Animate columns.
* **Speaker Tone:** Analytical, relatable.
* **Narration:**
> "Let’s look at a realistic scenario. Elena is on-call. A user registration endpoint in Python is throwing a 500 error: `IntegrityError: NOT NULL constraint failed: users.tenant_id`.  
> 
> Elena looks at the Python model code. In the code, the `User` class only defines `username` and `email`. Everything looks syntactically clean!  
> 
> What happened? A database migration recently ran on the live database adding a non-null `tenant_id` column. If Elena prompts an AI with just the Python code, the AI cannot see the database table and guesses incorrectly."

---

### [1:40 - 2:10] Slide 4: What is Model Context Protocol (MCP)?
* **Visual:** Slide 4 displayed. Animate 3 columns.
* **Speaker Tone:** Educational, structured.
* **Narration:**
> "The Model Context Protocol solves this by exposing three standardized primitives to the AI:  
> 
> First: **Resources**—read-only access to files, logs, and documentation.  
> Second: **Tools**—callable functions that allow Codex to take action or inspect environments, like running an `inspect_table` query.  
> And Third: **Prompts**—pre-configured workflows defined by the tool authors.  
> 
> MCP gives Codex safe, controlled eyes into the outside world."

---

### [2:10 - 2:45] Slide 5: Configuring MCP in OpenAI Codex
* **Visual:** Slide 5 displayed with code note styling.
* **Speaker Tone:** Practical, instructional.
* **Narration:**
> "Configuring MCP in Codex is remarkably straightforward.  
> 
> Inside your project or user configuration, we define an `mcpServers` block.  
> Here, we configure `sqlite-dev`. We specify the execution command, point to our local Python MCP server script, and pass the path to our SQLite database file.  
> 
> Once reloaded, Codex automatically registers the tools exposed by this server."

---

### [2:45 - 3:30] Slide 6: Important Statement
* **Visual:** Slide 6 displayed (Teal accent).
* **Speaker Tone:** Emphatic, definitive.
* **Narration:**
> "Consider this rule of thumb:  
> 
> *[1-second pause]*  
> 
> *'An AI that only sees source code is guessing. An AI with MCP is verifying.'*  
> 
> Giving your agent read-only introspection transforms it from a glorified code completer into an active debugging partner.  
> 
> Let's see this in action live."

---

### [3:30 - 3:45] Slide 7: Demo Transition
* **Visual:** Slide 7 displayed.
* **Narration:**
> "Let's switch to VS Code and watch OpenAI Codex leverage an MCP server to fix our database mismatch."

---

### [3:45 - 6:45] LIVE DEMO SCREENCAST (3:00)

#### Segment 1: The Failing Application [3:45 - 4:20]
* **Screen:** VS Code showing `app.py`. Terminal runs `python app.py`.
* **Action:** Terminal throws `sqlite3.IntegrityError: NOT NULL constraint failed: users.tenant_id`.
* **Visual Cue:** `[CALLOUT BOX: Highlight IntegrityError in terminal]` *(Hand off mouse)*.
* **Narration:**
> "Here is our application in `app.py`. When we run it in the terminal, it immediately crashes with: `IntegrityError: NOT NULL constraint failed: users.tenant_id`.  
> But if we look at our Python file on lines 8 through 15, the `User` class only defines `id`, `username`, and `email`. The code has no idea what `tenant_id` is."

#### Segment 2: Inspecting the MCP Server Configuration [4:20 - 4:55]
* **Screen:** Open `codex_mcp_config.json`.
* **Visual Cue:** `[CALLOUT BOX: Highlight mcpServers -> sqlite-dev]`
* **Narration:**
> "Instead of manually opening a database client to inspect the schema, let's look at our Codex MCP configuration.  
> 
> We have connected `sqlite-dev`, which provides an `inspect_table_schema` tool directly to Codex. Let's make sure our MCP server is active in the Codex panel."

#### Segment 3: Prompting Codex to Investigate via MCP [4:55 - 5:50]
* **Screen:** Open Codex panel and enter prompt: *"Investigate why app.py fails with IntegrityError on the users table. Use the sqlite-dev MCP tool to inspect the live schema."*
* **Visual Cue:** `[CALLOUT BOX: Highlight Codex invoking tool: sqlite-dev.inspect_table_schema("users")]`
* **Narration:**
> "Now we prompt Codex:  
> *'Investigate why app.py fails with IntegrityError on the users table. Use the sqlite-dev MCP tool to inspect the live schema.'*  
> 
> Look at the tool invocation indicator: Codex calls `sqlite-dev.inspect_table_schema` for table `users`.  
> The MCP server returns the live column definitions: and right there on column 4 is `tenant_id VARCHAR NOT NULL`!"

#### Segment 4: Applying the Fix and Verifying [5:50 - 6:45]
* **Screen:** Codex applies the fix to `app.py` adding `tenant_id` to the entity and insert query. Run `python app.py` in terminal $\rightarrow$ Success!
* **Visual Cue:** `[CALLOUT BOX: Highlight updated User class with tenant_id, then terminal success message]`
* **Narration:**
> "Because Codex saw the live schema via MCP, it didn't have to guess.  
> It immediately updates `app.py`: adding `tenant_id` to the `User` dataclass and providing a default organization tenant ID in the insert query.  
> 
> Let's re-run `python app.py` in the terminal:  
> *'User created successfully with ID: 101, Tenant: org_corp_default'*.  
> 
> The bug is solved, verified, and closed."

---

### [6:45 - 7:15] Slide 8: Summary & Key Takeaways
* **Visual:** Slide 8 displayed. Click bullets in sync.
* **Speaker Tone:** Enthusiastic, summarizing.
* **Narration:**
> *[Click Bullet 1]*  
> "To wrap up: bridge the context gap by connecting OpenAI Codex to real runtime systems using MCP.  
> 
> *[Click Bullet 2]*  
> Use declarative JSON configurations to grant targeted, read-only tools like schema inspection.  
> 
> *[Click Bullet 3]*  
> Empower your AI to verify facts against reality, eliminating hallucinations and debugging faster than ever before.  
> 
> Thank you so much for watching!"

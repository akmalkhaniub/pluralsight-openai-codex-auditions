# Video Audition Outline - Pluralsight

| Audition Information | |
| :--- | :--- |
| **Title** | Supercharging OpenAI Codex with Model Context Protocol (MCP) |
| **Author Name** | [Your Name] |
| **Level** | Advanced |
| **Additional Notes** | Focuses on configuring Model Context Protocol (MCP) servers in OpenAI Codex to grant the agent live, read-only introspection of database schemas and external development tools. |

| Course Planning | |
| :--- | :--- |
| **Learner Prerequisites** | Understanding of database schemas and foreign keys, basic client-server protocols, and familiarity with configuring developer tools via JSON. |
| **Storyline** | Elena is debugging an urgent production bug: a user creation endpoint is crashing with a cryptic database foreign key constraint error. Looking strictly at the source code, OpenAI Codex cannot figure out why the insertion fails because it cannot see the live database schema. Elena configures an MCP (Model Context Protocol) database server inside Codex, enabling the agent to autonomously inspect live schema metadata, discover a missing non-null `tenant_id` column, and resolve the bug accurately. |
| **Description** | In this audition you’ll learn to connect OpenAI Codex to external development environments using the Model Context Protocol (MCP). When you’re finished with this audition, you’ll have the skills and knowledge of Codex MCP configuration needed to give your AI agent direct access to live schemas, linters, and external documentation. |

| Course Organization | |
| :---: | :--- | :--- |
| **1** | **Audition Overview**<br>• Title slide & introduction.<br>• WIIFM: Why AI agents trapped in code-only sandboxes hallucinate and how MCP gives them real-world environment awareness.<br>• Preview: Codex autonomously inspecting a live database schema via MCP to fix an invisible database bug. | **70 seconds (1:10)** |
| **2** | **Conceptual Foundation: How MCP Empowers Codex**<br>• *Slide 1:* The Context Gap (Why static code inspection fails when runtime schemas diverge).<br>• *Slide 2:* What is Model Context Protocol? (The open standard for AI tools and resources).<br>• *Slide 3:* Configuring MCP in Codex: Declarative JSON setup (`mcpServers`) and security permissions. | **2:20 minutes** |
| **3** | **Demo: Fixing a Live Database Schema Bug via MCP**<br>• *Step 1:* Run the failing app: `sqlite3.IntegrityError: NOT NULL constraint failed: users.tenant_id`. Show that the Python model code is missing this field.<br>• *Step 2:* Open `codex_mcp_config.json` and show the database MCP server connection.<br>• *Step 3:* Prompt Codex: *"Investigate why user insertion is failing using the SQLite MCP schema tool."*<br>• *Step 4:* Callout overlays show Codex invoking `db.inspect_schema("users")`, discovering the newly migrated `tenant_id` column, and updating the ORM model to pass `tenant_id`. | **3:00 minutes** |
| **4** | **Conclusion**<br>• Summary: Transitioning Codex from a passive text editor into an environment-aware engineer.<br>• Next Steps: Exploring ecosystem MCP servers (GitHub, PostgreSQL, AWS). | **0:45 seconds** |
| **Total Duration** | | **~7:15 minutes** |

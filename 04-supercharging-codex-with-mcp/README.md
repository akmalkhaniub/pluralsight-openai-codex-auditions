# Topic 4: Supercharging OpenAI Codex with Model Context Protocol (MCP)

## Package Contents
* `AUDITION_OUTLINE.md`: The official filled-out Pluralsight Video Audition Outline form.
* `SLIDE_DECK_CONTENT.md`: Slide-by-slide layout matching the Pluralsight PowerPoint template with on-click animation cues.
* `TIMED_NARRATION_SCRIPT.md`: Word-for-word spoken transcript with second-by-second timestamps and visual callout instructions.
* `demo-code/`: The MCP server, failing app, SQLite database setup, and configuration files.

## How to Record Your Audition
1. **Prepare Slides:** Copy `SLIDE_DECK_CONTENT.md` into the Pluralsight PowerPoint template. Set bullets to appear one at a time.
2. **Setup the Demo Screencast:**
   * Step 1: Open terminal in `demo-code/` and run `python setup_db.py`.
   * Step 2: Run `python app.py` and show the red `sqlite3.IntegrityError: NOT NULL constraint failed: users.tenant_id`. Show that the Python code has no `tenant_id`.
   * Step 3: Open `codex_mcp_config.json` and explain the `sqlite-dev` connection using callout boxes (no mouse circling).
   * Step 4: Open the Codex prompt panel and paste the prompt from `codex_prompts.txt`.
   * Step 5: Watch Codex invoke the MCP `inspect_table_schema` tool, diagnose the missing `tenant_id`, and patch `app.py`.
   * Step 6: Re-run `python app.py` in the terminal to verify clean execution.
3. **Target Time:** 7 minutes 15 seconds.

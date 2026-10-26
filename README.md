# AI Project & CV Reviewer

An AI agent that reviews **code projects** (ZIP / single file) and **technical CVs** (PDF / text) and then lets you chat about the results.

> Team graduation project from the Digital Egypt Pioneers Initiative (DEPI, program period Nov 2025 – Jul 2026), built by [Ahmed Abdelaziz](https://github.com/ahmedabdelazizahmed) and [morefaat69](https://github.com/morefaat69). This repository holds the version cleaned and documented in Oct 2026 (folder structure, docs, file-handling safety fix). The live demo backend runs on a teammate's Hugging Face Space, using his Groq API key.

## How it works
- **Backend:** Flask API + a LangChain **ReAct agent** with conversation memory.
- **LLM:** Llama 3.3 70B (`llama-3.3-70b-versatile`) served by **Groq** through its OpenAI-compatible endpoint.
- **Tools the agent can call:** `code_structure_analyzer`, `bug_detector`, `best_practices_checker`, `code_improver`, `cv_analyzer` (rule-based keyword/ATS scoring), `web_search` (DuckDuckGo).
- **Frontend:** static HTML/JS (upload → results + chat → history stored in the browser).
- **Safety:** per-IP rate limit (20 requests/hour), file size limit (15 MB), content truncation (7,000 chars), and `.env*` files inside uploaded ZIPs are never read.

## Endpoints
| Method | Path | What it does |
|---|---|---|
| POST | `/AI` | Upload a file, get the first analysis + `session_id` |
| POST | `/chat` | Follow-up question inside a session |
| DELETE | `/session/<id>` | Delete a session |
| GET | `/session/<id>/history` | Get chat history |
| GET | `/health` | Status, model, tools |

Details: `docs/API_Documentation.txt`.

## Run locally
```bash
pip install -r requirements.txt
cp .env.example .env      # then put your own GROQ_API_KEY inside
python app.py             # http://localhost:7860/health
```
Open `frontend/page1.html` and set `API_BASE` in `frontend/js/api.js` to `http://localhost:7860` while testing.

## Deploy your own copy (optional): Render
1. Push this repo to GitHub.
2. On render.com: **New → Web Service**, connect the repo, runtime **Docker**, plan **Free**.
3. Add the environment variable `GROQ_API_KEY` (and optionally `FLASK_SECRET_KEY`) in the service settings. Never commit keys.
4. After the first deploy, open `https://<your-service>.onrender.com/health`.
5. Put that URL in `API_BASE` inside `frontend/js/api.js`, then publish the `frontend/` folder (for example with GitHub Pages).

Note: on the free plan the server sleeps after about 15 minutes without traffic, so the first request after a pause can take about a minute.

## Known limitations (honest list)
- Sessions are kept in memory, so they reset when the server restarts.
- `cv_analyzer` is keyword-based, not an LLM judgment (planned improvement).
- Free-tier LLM limits apply.

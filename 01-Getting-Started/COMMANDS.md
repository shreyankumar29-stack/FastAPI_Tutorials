# FastAPI Tutorial Commands

Commands used while learning FastAPI through the **Corey Schafer FastAPI tutorial series**.

> **Note:** Corey Schafer uses `uv` in the tutorial. This course uses **Python `venv` + `pip`** instead.

---

# 1. Create Project Directory

```powershell
mkdir FastAPI_Tutorials
cd FastAPI_Tutorials
```

---

# 2. Create a Tutorial Directory

```powershell
mkdir 01-Getting-Started
cd 01-Getting-Started
```

---

# 3. Create Virtual Environment

```powershell
python -m venv .venv
```

If the virtual environment is located in the parent project directory, activate it from the tutorial directory with:

```powershell
..\.venv\Scripts\activate
```

If `.venv` is inside the current directory:

```powershell
.venv\Scripts\activate
```

---

# 4. Check Python Version

```powershell
python --version
```

---

# 5. Check Python Location

```powershell
python -c "import sys; print(sys.executable)"
```

This is useful for confirming that Python from `.venv` is being used.

---

# 6. Install FastAPI

```powershell
pip install "fastapi[standard]"
```

This installs FastAPI along with the standard dependencies needed for development.

---

# 7. Check FastAPI Installation

```powershell
pip show fastapi
```

---

# 8. Check Installed Packages

```powershell
pip list
```

---

# 9. Run FastAPI Development Server

From the directory containing `main.py`:

```powershell
fastapi dev main.py
```

---

# 10. Stop the Server

Press:

```text
CTRL + C
```

---

# 11. Local Application

Default development URL:

```text
http://127.0.0.1:8000
```

---

# 12. Swagger Documentation

Open:

```text
http://127.0.0.1:8000/docs
```

---

# 13. ReDoc Documentation

Open:

```text
http://127.0.0.1:8000/redoc
```

---

# 14. Verify FastAPI from Python

```powershell
python -c "import fastapi; print(fastapi.__version__)"
```

---

# 15. Useful Virtual Environment Commands

### Activate

```powershell
.venv\Scripts\activate
```

### Deactivate

```powershell
deactivate
```

---

# 16. Git Commands

Check repository status:

```powershell
git status
```

Add files:

```powershell
git add .
```

Commit:

```powershell
git commit -m "Complete FastAPI video 1"
```

Push:

```powershell
git push origin main
```

---

# 17. Corey's `uv` Commands vs My Commands

| Corey Schafer        | This Course                       |
| -------------------- | --------------------------------- |
| `uv init`            | `python -m venv .venv`            |
| `uv add fastapi`     | `pip install "fastapi[standard]"` |
| `uv run fastapi dev` | `fastapi dev main.py`             |

The tools are different, but the FastAPI concepts being learned are the same.

---

# 18. Video 1 Command Summary

```powershell
python -m venv .venv
.venv\Scripts\activate
pip install "fastapi[standard]"
pip show fastapi
fastapi dev main.py
```



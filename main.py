import os
import pathlib
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title="Python App")

_ROOT = pathlib.Path(__file__).parent

@app.get("/", response_class=HTMLResponse)
def read_root():
    html_file = _ROOT / "index.html"
    if html_file.exists():
        return HTMLResponse(content=html_file.read_text(encoding='utf-8'))
    return HTMLResponse(content="<h1>Python App is running</h1>")

@app.get("/api/info")
def api_info():
    db_status = 'disabled'
    if os.getenv('DATABASE_URL'):
        db_status = 'configured'
    return {
        'app': 'python',
        'status': 'running',
        'db': db_status
    }

if __name__ == '__main__':
    import uvicorn
    port = int(os.getenv('PORT', 8000))
    host = os.getenv('HOST', '0.0.0.0')
    uvicorn.run('main:app', host=host, port=port, reload=False)

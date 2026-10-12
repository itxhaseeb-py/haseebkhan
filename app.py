from fastapi import FastAPI , Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pathlib import Path

app = FastAPI()
templates = Jinja2Templates(directory="templates")

BASE_DIR = Path(__file__).resolve().parent

app.mount(
    "/static",
    StaticFiles(directory=BASE_DIR / "static"),
    name="static"
)




@app.get("/")
def home(request : Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={}
    )



@app.get("/about")
def home(request : Request):
    return templates.TemplateResponse(
        request=request,
        name="about.html",
        context={}
    )




@app.get("/Skills")
def skills(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="Skills.html",
        context={}
    )






@app.get("/projects")
def skills(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="projects.html",
        context={}
    )



@app.get("/contact")
def contact(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="contact.html",
        context={}
    )
from fastapi import FastAPI, Depends
from .schemas import CreateJobRequest
from sqlalchemy.orm import Session
from .database import get_db
from .models import Job


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/check")
def read_check():
    return {"Hello": "Check world"}

@app.post("/job")
def create_job(details: CreateJobRequest, db: Session = Depends(get_db)):
	to_create = Job(
		title=details.title,
		description=details.description
	)
	db.add(to_create)
	db.commit()

	return {
		"success": True,
		"created_id": to_create.id
	}

@app.get("/job")
def get_all_jobs(db: Session = Depends(get_db)):
	all = db.query(Job).all()
	return {"data": all}

@app.get("/job/{id}")
def get_job_by_id(id: int, db: Session = Depends(get_db)):
	return db.query(Job).filter(Job.id == id).first()

@app.delete("/job/{id}")
def delete_job_by_id(id: int, db: Session = Depends(get_db)):
	job = db.query(Job).filter(Job.id == id).first()
	success = bool(job)
	if success:
		db.delete(job)
		db.commit()
	return {"success": success}

@app.put("/job/{id}")
def update_job(id: int, details: CreateJobRequest, db: Session = Depends(get_db)):
	job = db.query(Job).filter(Job.id == id).first()
	is_found = bool(job)
	if is_found:
		job.title = details.title
		job.description = details.description
		db.add(job)
		db.commit()
	return {"success": is_found}
	


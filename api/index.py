# from fastapi import FastAPI
# from pydantic import BaseModel
# from typing import List

# app = FastAPI(title="Candidate-Job Matcher API")

# # Candidate model
# class Candidate(BaseModel):
#     name: str
#     skills: List[str]
#     education: str
#     experience: int  # in years

# # Job model
# class Job(BaseModel):
#     title: str
#     skills: List[str]
#     education: str
#     experience: int  # required experience in years

# # Request model
# class MatchRequest(BaseModel):
#     candidate: Candidate
#     jobs: List[Job]

# # Function to calculate score based on skills, experience & education
# def calculate_score(candidate: Candidate, job: Job):
#     # Skills match (50 points)
#     skill_match = len(set(candidate.skills) & set(job.skills)) / len(job.skills) * 50
    
#     # Experience match (30 points)
#     if job.experience == 0:
#         exp_match = 30  # agar job experience 0 hai, full points
#     else:
#         exp_match = min(candidate.experience / job.experience, 1) * 30
    
#     # Education match (20 points)
#     edu_match = 20 if candidate.education.lower() == job.education.lower() else 0
    
#     # Total score
#     total_score = skill_match + exp_match + edu_match
#     return total_score

# # API endpoint
# @app.post("/recommend_jobs_per_job/")
# def recommend_jobs_per_job(data: MatchRequest):
#     results = []

#     for job in data.jobs:
#         score = calculate_score(data.candidate, job)
#         results.append({
#             "job_title": job.title,
#             "candidate": data.candidate.dict(),
#             "score": round(score, 2)
#         })

#     # Sort jobs by score descending
#     results.sort(key=lambda x: x["score"], reverse=True)
#     return {"recommendations": results}



from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "FastAPI deployed on Vercel 🚀"}

@app.get("/health")
def health():
    return {"status": "OK"}

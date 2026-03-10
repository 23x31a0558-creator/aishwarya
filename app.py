from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# Importing the project data from the existing code.py file
try:
    from code import project_data
except ImportError:
    project_data = {}
    print("Warning: Could not import project_data from code.py")

app = FastAPI(
    title="Construction Project Management API",
    description="API for accessing construction project details including schedule, resources, and costs.",
    version="1.0.0"
)

# Enable CORS for frontend integration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.get("/")
def read_root():
    return {
        "message": "Welcome to the Construction Project Management API",
        "endpoints": [
            "/api/overview",
            "/api/wbs",
            "/api/schedule",
            "/api/resources",
            "/api/materials",
            "/api/costs",
            "/api/risks",
            "/api/optimization",
            "/api/all"
        ]
    }

@app.get("/api/overview", tags=["Project Information"])
def get_project_overview():
    """Get the general overview of the construction project."""
    if "project_overview" not in project_data:
        raise HTTPException(status_code=404, detail="Overview not found")
    return {"project_overview": project_data["project_overview"]}

@app.get("/api/wbs", tags=["Project Information"])
def get_work_breakdown_structure():
    """Get the Work Breakdown Structure (WBS) phases and tasks."""
    if "wbs" not in project_data:
        raise HTTPException(status_code=404, detail="WBS not found")
    return {"wbs": project_data["wbs"]}

@app.get("/api/schedule", tags=["Planning"])
def get_schedule():
    """Get the project schedule including task durations and dependencies."""
    if "schedule" not in project_data:
        raise HTTPException(status_code=404, detail="Schedule not found")
    return {"schedule": project_data["schedule"]}

@app.get("/api/resources", tags=["Planning"])
def get_resources():
    """Get the labor and equipment resources required for tasks."""
    if "resources" not in project_data:
        raise HTTPException(status_code=404, detail="Resources not found")
    return {"resources": project_data["resources"]}

@app.get("/api/materials", tags=["Logistics"])
def get_materials():
    """Get the estimated materials required for the project."""
    if "materials" not in project_data:
        raise HTTPException(status_code=404, detail="Materials not found")
    return {"materials": project_data["materials"]}

@app.get("/api/costs", tags=["Financials"])
def get_cost_estimation():
    """Get the estimated costs for materials, labor, and equipment."""
    if "cost_estimation" not in project_data:
        raise HTTPException(status_code=404, detail="Cost estimation not found")
    return {"cost_estimation": project_data["cost_estimation"]}

@app.get("/api/risks", tags=["Risk Management"])
def get_risks():
    """Get the identified project risks and their mitigations."""
    if "risks" not in project_data:
        raise HTTPException(status_code=404, detail="Risks not found")
    return {"risks": project_data["risks"]}

@app.get("/api/optimization", tags=["Planning"])
def get_optimization_strategies():
    """Get project optimization strategies."""
    if "optimization" not in project_data:
        raise HTTPException(status_code=404, detail="Optimization strategies not found")
    return {"optimization": project_data["optimization"]}

@app.get("/api/all", tags=["Complete Data"])
def get_all_data():
    """Get all project data in a single payload."""
    return project_data

if __name__ == "__main__":
    import uvicorn
    # Run the API on localhost at port 8000
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)

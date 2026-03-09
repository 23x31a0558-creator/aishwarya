project_data = {
    "project_overview": "Construction of a 5-story residential apartment building with a total floor area of 20,000 sq ft. The project includes site preparation, foundation, structural framework, masonry, electrical and plumbing installations, and interior finishes.",
    "wbs": [
        {
            "phase": "Site Preparation & Substructure",
            "tasks": [
                "Site preparation",
                "Excavation",
                "Foundation work"
            ]
        },
        {
            "phase": "Superstructure",
            "tasks": [
                "Structural framework",
                "Brickwork",
                "Roofing"
            ]
        },
        {
            "phase": "Systems & Interior",
            "tasks": [
                "Electrical installation",
                "Plumbing",
                "Plastering",
                "Flooring",
                "Painting"
            ]
        },
        {
            "phase": "Closing",
            "tasks": [
                "Final inspection"
            ]
        }
    ],
    "schedule": [
        {
            "task": "Site preparation",
            "duration_days": "14",
            "depends_on": "None"
        },
        {
            "task": "Excavation",
            "duration_days": "21",
            "depends_on": "Site preparation"
        },
        {
            "task": "Foundation work",
            "duration_days": "30",
            "depends_on": "Excavation"
        },
        {
            "task": "Structural framework",
            "duration_days": "60",
            "depends_on": "Foundation work"
        },
        {
            "task": "Brickwork",
            "duration_days": "45",
            "depends_on": "Structural framework"
        },
        {
            "task": "Roofing",
            "duration_days": "20",
            "depends_on": "Structural framework"
        },
        {
            "task": "Electrical installation",
            "duration_days": "35",
            "depends_on": "Structural framework"
        },
        {
            "task": "Plumbing",
            "duration_days": "35",
            "depends_on": "Structural framework"
        },
        {
            "task": "Plastering",
            "duration_days": "30",
            "depends_on": "Brickwork, Electrical installation, Plumbing"
        },
        {
            "task": "Flooring",
            "duration_days": "25",
            "depends_on": "Plastering"
        },
        {
            "task": "Painting",
            "duration_days": "20",
            "depends_on": "Plastering"
        },
        {
            "task": "Final inspection",
            "duration_days": "10",
            "depends_on": "Flooring, Painting, Roofing"
        }
    ],
    "resources": [
        {
            "task": "Excavation",
            "labor": [
                "Equipment Operators",
                "General Laborers"
            ],
            "equipment": [
                "Excavators",
                "Dump Trucks"
            ]
        },
        {
            "task": "Foundation work",
            "labor": [
                "Concrete Finishers",
                "Ironworkers"
            ],
            "equipment": [
                "Concrete Mixers",
                "Concrete Pumps",
                "Vibrators"
            ]
        },
        {
            "task": "Structural framework",
            "labor": [
                "Ironworkers",
                "Crane Operators",
                "Carpenters"
            ],
            "equipment": [
                "Tower Crane",
                "Welding Machines"
            ]
        },
        {
            "task": "Brickwork",
            "labor": [
                "Masons",
                "Laborers"
            ],
            "equipment": [
                "Mortar Mixers",
                "Scaffolding"
            ]
        },
        {
            "task": "Electrical installation",
            "labor": [
                "Electricians",
                "Apprentices"
            ],
            "equipment": [
                "Hand Tools",
                "Lifts"
            ]
        },
        {
            "task": "Plumbing",
            "labor": [
                "Plumbers",
                "Pipefitters"
            ],
            "equipment": [
                "Welding Gear",
                "Hand Tools"
            ]
        }
    ],
    "materials": [
        {
            "material": "Cement",
            "estimated_quantity": "5000 bags"
        },
        {
            "material": "Steel",
            "estimated_quantity": "150 tons"
        },
        {
            "material": "Sand",
            "estimated_quantity": "800 cubic yards"
        },
        {
            "material": "Bricks",
            "estimated_quantity": "100,000 units"
        },
        {
            "material": "Aggregates",
            "estimated_quantity": "1200 cubic yards"
        },
        {
            "material": "Electrical materials",
            "estimated_quantity": "15000 feet wiring, 200 units of lighting and panels"
        },
        {
            "material": "Plumbing materials",
            "estimated_quantity": "5000 feet piping, 50 sets of fixtures"
        }
    ],
    "cost_estimation": {
        "materials_cost": "2000000",
        "labor_cost": "2200000",
        "equipment_cost": "500000",
        "total_cost": "4700000"
    },
    "risks": [
        {
            "risk": "Weather delays",
            "impact": "Delay in structural framework and roofing schedule.",
            "mitigation": "Include a weather buffer in the schedule; utilize proper protective covers."
        },
        {
            "risk": "Labor shortages",
            "impact": "Delays across multiple tasks, especially specialized MEP and masonry.",
            "mitigation": "Lock in subcontractor agreements early and offer competitive wages."
        },
        {
            "risk": "Material price fluctuations",
            "impact": "Exceeding the materials budget (especially for steel and cement).",
            "mitigation": "Procure large quantities of major materials early and establish fixed-price contracts."
        },
        {
            "risk": "Safety hazards",
            "impact": "Potential for worker injuries leading to work stoppages and liability.",
            "mitigation": "Strict enforcement of OSHA safety regulations, daily safety briefings, and proper PPE."
        }
    ],
    "optimization": [
        "Adopt Building Information Modeling (BIM) to identify and resolve clashes during the design and planning phase.",
        "Schedule parallel task execution where dependencies permit, such as starting lower floor MEP rough-ins while framework continues on upper floors.",
        "Use pre-fabricated or precast concrete elements to reduce on-site construction time.",
        "Implement Just-in-Time (JIT) material delivery to minimize site clutter and storage costs."
    ]
}

def display_project_overview(data):
    print("=" * 60)
    print("PROJECT OVERVIEW")
    print("=" * 60)
    print(data["project_overview"])
    print("\n")

def display_schedule(data):
    print("=" * 60)
    print("PROJECT SCHEDULE")
    print("=" * 60)
    for item in data["schedule"]:
        print(f"- {item['task']}: {item['duration_days']} days (Depends on: {item['depends_on']})")
    print("\n")

def calculate_costs(data):
    print("=" * 60)
    print("COST ESTIMATION")
    print("=" * 60)
    costs = data["cost_estimation"]
    print(f"Materials Cost: ${int(costs['materials_cost']):,}")
    print(f"Labor Cost:     ${int(costs['labor_cost']):,}")
    print(f"Equipment Cost: ${int(costs['equipment_cost']):,}")
    print("-" * 30)
    print(f"TOTAL COST:     ${int(costs['total_cost']):,}")
    print("\n")

def display_risks(data):
    print("=" * 60)
    print("PROJECT RISKS & MITIGATION")
    print("=" * 60)
    for item in data["risks"]:
        print(f"RISK: {item['risk']}")
        print(f"  Impact: {item['impact']}")
        print(f"  Mitigation: {item['mitigation']}")
        print()

if __name__ == "__main__":
    display_project_overview(project_data)
    display_schedule(project_data)
    calculate_costs(project_data)
    display_risks(project_data)

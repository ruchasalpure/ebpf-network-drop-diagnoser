from crewai import Agent

ebpf_network_drop_diagnoser = Agent(
    role="Ebpf Network Drop Diagnoser",
    goal="Deliver high-precision autonomous Ebpf Network Drop Diagnoser operations",
    backstory="Engineered under OpenGAP governance standards.",
    verbose=True,
    allow_delegation=False
)

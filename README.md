# CI/CD Pipeline Project

## Project Name
CI/CD Pipeline Implementation with GitHub Actions and OpenShift

## Description
This project demonstrates the implementation of Continuous Integration and Continuous Deployment (CI/CD) pipelines using GitHub Actions and OpenShift Tekton Pipelines.

## Features
- Automated linting with flake8/ESLint
- Automated unit testing with nose/Jest
- Docker container builds with Buildah
- Automated deployment to OpenShift
- Persistent volume claims for pipeline workspaces

## Technologies Used
- GitHub Actions
- OpenShift Tekton Pipelines
- Python/Node.js
- Docker/Buildah
- Kubernetes/OpenShift

## Project Structure
```
.
├── .github/
│   └── workflows/
│       └── workflow.yml
├── .tekton/
│   └── tasks.yml
├── README.md
└── src/
```

## Setup Instructions
1. Clone this repository
2. Configure GitHub Actions secrets
3. Set up OpenShift cluster access
4. Create PersistentVolumeClaim with storage class `skills-network-learner`
5. Deploy the Tekton pipeline

## Pipeline Steps
- **Cleanup**: Remove previous build artifacts
- **Git Clone**: Fetch source code
- **Lint**: Code quality checks (flake8/ESLint)
- **Test**: Run unit tests (nose/Jest)
- **Build**: Create container image with Buildah
- **Deploy**: Deploy to OpenShift cluster

## License
MIT License

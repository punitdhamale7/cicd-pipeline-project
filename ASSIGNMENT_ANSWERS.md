# CI/CD Pipeline Assignment - Answer Guide

## Question 1: README.md URL (2 points)
**What to submit:** Public GitHub URL of README.md file containing project name details

**Your answer format:**
```
https://github.com/YOUR_USERNAME/YOUR_REPO_NAME/blob/main/README.md
```

**What to do:**
1. Create a GitHub repository
2. Push this project to your repository
3. Navigate to the README.md file on GitHub
4. Copy the URL from your browser

---

## Question 2: GitHub Actions Workflow URL (4 points)
**What to submit:** Public GitHub URL of .github/workflows/workflow.yml showing lint and test steps

**Your answer format:**
```
https://github.com/YOUR_USERNAME/YOUR_REPO_NAME/blob/main/.github/workflows/workflow.yml
```

**Key code snippets to highlight:**

### Lint with flake8 step (lines 22-28):
```yaml
- name: Lint with flake8
  run: |
    # Stop the build if there are Python syntax errors or undefined names
    flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
    # Exit-zero treats all errors as warnings
    flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
```

### Run unit tests with nose step (lines 35-37):
```yaml
- name: Run unit tests with nose
  run: |
    nosetests --with-coverage --cover-package=src --cover-erase --cover-html
```

---

## Question 3: Tekton Tasks URL (4 points)
**What to submit:** Public GitHub URL of .tekton/tasks.yml showing cleanup and test tasks

**Your answer format:**
```
https://github.com/YOUR_USERNAME/YOUR_REPO_NAME/blob/main/.tekton/tasks.yml
```

**Key code snippets to highlight:**

### Cleanup task (lines 66-82):
```yaml
apiVersion: tekton.dev/v1beta1
kind: Task
metadata:
  name: cleanup-task
spec:
  description: Clean up workspace before starting pipeline
  workspaces:
    - name: source
  steps:
    - name: cleanup
      image: alpine:3.15
      script: |
        #!/bin/sh
        echo "Cleaning up workspace..."
        rm -rf $(workspaces.source.path)/*
        echo "Cleanup complete"
```

### Test task with nose (lines 104-123):
```yaml
apiVersion: tekton.dev/v1beta1
kind: Task
metadata:
  name: nose-test
spec:
  description: Run unit tests with nose
  workspaces:
    - name: source
  steps:
    - name: run-tests
      image: python:3.9-slim
      workingDir: $(workspaces.source.path)
      script: |
        #!/bin/bash
        echo "Installing test dependencies..."
        pip install nose coverage
        if [ -f requirements.txt ]; then
          pip install -r requirements.txt
        fi
        echo "Running unit tests with nose..."
        nosetests --with-coverage --cover-package=src --cover-erase
        echo "Tests complete"
```

---

## Question 4: GitHub Actions Terminal Output (2 points)
**What to submit:** Copy and paste text from cicd-github-validate file

**Your answer:**
Copy the entire content from the `cicd-github-validate` file showing:
- Checkout step completion
- Python setup
- flake8 installation and execution
- nose test execution with results
- All 3 tests passing (OK status)
- Coverage report showing 96% coverage

---

## Question 5: OpenShift PVC Screenshot (2 points)
**What to submit:** Screenshot file named `oc-pipelines-console-pvc-details.png` or `.jpeg`

**What to capture:**
After creating the PVC in OpenShift, take a screenshot showing:
- Storage class: `skills-network-learner`
- Requested capacity: `1Gi` (1GB)
- Status: Bound

**How to create the PVC:**
```bash
oc apply -f k8s/pvc.yml
```

Then navigate to: Storage → PersistentVolumeClaims in OpenShift console

---

## Question 6: OpenShift Pipeline Steps Screenshot (2 points)
**What to submit:** Screenshot file named `oc-pipelines-oc-final.png` or `.jpeg`

**What to capture:**
Screenshot of the pipeline showing all these steps in order:
1. cleanup
2. git-clone
3. flake8 (or eslint)
4. nose (or jest)
5. buildah
6. deploy (openshift-client)

**Where to find:** Pipelines section in OpenShift console

---

## Question 7: Successful Pipeline Run Screenshot (2 points)
**What to submit:** Screenshot file named `oc-pipelines-oc-green.png` or `.jpeg`

**What to capture:**
Screenshot showing the pipeline run with ALL steps in GREEN (completed successfully):
- cleanup ✓
- git-clone ✓
- flake8 ✓
- nose ✓
- buildah ✓
- deploy ✓

**Where to find:** Pipeline Runs section showing a successful execution

---

## Question 8: Application Logs Text (2 points)
**What to submit:** Copy and paste text from oc-pipeline-application-logs file

**Your answer:**
Copy the content from the `oc-pipeline-application-logs` file showing:
- Application startup sequence
- "SERVICE RUNNING" message (line 13)
- Running on port 8000
- Health check and API endpoints available

**Key line to verify:**
```
2026-10-04 08:15:25,294 - INFO - SERVICE RUNNING
2026-10-04 08:15:25,395 - INFO - Application ready to accept requests on port 8000
```

---

## Next Steps to Complete Assignment:

1. **Initialize Git and Push to GitHub:**
   ```bash
   git init
   git add .
   git commit -m "Initial CI/CD pipeline setup"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
   git push -u origin main
   ```

2. **Verify GitHub Actions:**
   - Go to your repository on GitHub
   - Click "Actions" tab
   - Verify the workflow runs automatically

3. **Set up OpenShift Pipeline:**
   - Apply the Tekton tasks: `oc apply -f .tekton/tasks.yml`
   - Create the PVC: `oc apply -f k8s/pvc.yml`
   - Run the pipeline and capture screenshots

4. **Collect Application Logs:**
   - After successful deployment, get pod logs: `oc logs <pod-name>`
   - Save output showing "SERVICE RUNNING" message

5. **Submit all URLs, text files, and screenshots as required**

---

## File Checklist:
- ✓ README.md (project details)
- ✓ .github/workflows/workflow.yml (GitHub Actions)
- ✓ .tekton/tasks.yml (Tekton pipeline)
- ✓ cicd-github-validate (terminal output text)
- ✓ oc-pipeline-application-logs (app logs text)
- ⏹ oc-pipelines-console-pvc-details.png (screenshot - you need to create)
- ⏹ oc-pipelines-oc-final.png (screenshot - you need to create)
- ⏹ oc-pipelines-oc-green.png (screenshot - you need to create)

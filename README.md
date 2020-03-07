# Starter Kit for FastAPI on Google App Engine

Starter project template for running a FastAPI-based application on
Google App Engine Standard Python 3 Runtime.

## Scope of this starter kit

The scope of this starter kit is fairly small, punting on the front-end UI implementation
to avoid bloating the code and keeping the list of opinionated choices fairly minimal.

### In scope and already implemented

This starter kit includes the following:

- Production-ready App Engine configuration (in `app.yaml`) with FastAPI ASGI app running via gunicorn and uvicorn
- Continuous Integration (CI) workflow via GitHub Actions (see `.github/workflows/continous-integration.yaml`)
- Unit tests via pytest (see `tests/test_api.py`)

### Not yet implemented

The starter kit does not yet include the following (PRs are welcome):

- Continous deployment (CD) workflow via GitHub Actions, leveraging https://github.com/GoogleCloudPlatform/github-actions
- Acceptance/smoke tests hitting API endpoints on App Engine post-deployment
- Sample integration with Cloud Datastore or Cloud Firestore
- Sample auth integration


## Technologies

- [FastAPI](https://fastapi.tiangolo.com/) - High-performance Python [ASGI](https://asgi.readthedocs.io/en/latest/) web framework
- [pytest](https://docs.pytest.org/en/latest/) - Modern testing framework for Python
- [uvicorn](https://www.uvicorn.org) - ASGI server (for local development and production, runs cross-platform)


## Development Setup Requirements

- Python 3.7 or later
- Windows, MacOS, and Linux development environments are supported


## Development Setup Instructions

Assuming the development setup requirements above have been satisfied,
run the following in a terminal (git-bash is recommended on Windows) after cloning the repo
to set up your local development environment.

```bash 
# Install local dev requirements, ideally in an isolated Python 3.7 (or later) environment
pip install -r requirements-dev.txt
```


## Running the Development Server

The local dev server runs via uvicorn...

```bash
# Cross-platform, works on Windows, MacOS and Linux
uvicorn app.main:application --reload

# Alternate method of running local dev server via npm
npm start
```

The app is viewable at http://localhost:8000

### Running Development Server in Production-emulation Mode

If you're on Linux or macOS, you can run the local dev server in a mode that more closely resembles production
by using gunicorn with uvicorn workers as follows...

```bash
# Only works on Linux and macOS
gunicorn --workers 1 --worker-class uvicorn.workers.UvicornWorker --bind :9000 app.main:application

# Alternate method of running production-emulated dev server via npm
npm run start:prod

```

The production-emulated app is viewable at http://localhost:9000

### Customizing the HTTP Port

The app runs on port 8000 by default for local development.

To customize the port, pass the `--port` option (for uvicorn) 

```bash
# Set uvicorn port to 9000
uvicorn --port=:9000 app.main:application --reload

```


## Running Tests

The tests are run via `pytest`, with the configuration file at `pytest.ini`.

Ensure the proper dependencies are installed via `pip install -r requirements-test.txt` prior to running the tests.

```bash
# Run all tests
pytest

# Alternate method of running tests via npm
npm test

# Run only a particular test
pytest tests/test_api.py::test_hello

```


## Google Cloud Setup Instructions

1. Create an App Engine Project at https://console.cloud.google.com/appengine
2. Download and install the [Google Cloud SDK](https://cloud.google.com/sdk/docs/)
3. If on Windows, run the "Google Cloud SDK Shell" application (keep option selected during SDK install)
4. Type `gcloud init` in a terminal or in the Cloud SDK Shell (or keep option selected during install)
5. Log in via `gcloud auth login` in the Cloud SDK Shell if necessary
6. Set the active project (created in step 1) via `gcloud config set project PROJECT_ID`
7. If on Windows, install the App Engine components via `gcloud components install app-engine-python`

See the platform-specific Quickstart guides at https://cloud.google.com/sdk/docs/quickstarts

## Deploying to Google App Engine

Run the following command at the repo root (where the `app.yaml` config file is located) to deploy to App Engine...

```bash
# Deploy to App Engine
gcloud app deploy
```


## CI/CD

A GitHub Actions continuous integration (CI) workflow is provided in the `.github/workflows` folder, running
unit tests when a non-master branch is pushed to GitHub.

Perform the following steps to configure the CI workflow to be enforced on GitHub pull requests (PRs) against
the repo's master branch:

1. In the GitHub UI for your forked repo, click the "Settings" tab at top and click the "Branches" nav item at left.
2. In the "Branch protection rules" section, click the Add rule button if there is no rule for the master branch.
3. If there is a protection rule for the master branch, click the "Edit" button for that rule.
4. Enable the checkbox for the "Require status checks to pass before merging".
5. If "Run unit tests" is a visible option for the "Status checks found in the last week for this repository", use that.
6. If the "Run unit tests" option isn't displayed yet, it will display after a non-master branch has been pushed.
7. Create a branch with a test commit to confirm the above has enabled status checks for PRs in your repo.

A Continuous Deployment (CD) pipeline via GitHub Actions will likely land in this starter kit to complement the
CI workflow noted above.


## Related Projects

### Starter Kit for Flask on Google App Engine

See https://github.com/kamalgill/cloud-starterkit-flask-appengine

# AZX - Backend Python Developer Test

## Table of Contents

- [Setup](#setup)
  - [Prerequisites](#prerequisites)
  - [Virtual Environment](#virtual-environment)
  - [Install Dependencies](#install-dependencies)
- [Running Unit Tests](#running-unit-tests)
- [Running Flask Apps](#running-flask-apps)
- [Exercise 3 Solution](#exercise-3-solution)

## Setup

### Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.10+
- Poetry (see installation details [here](https://python-poetry.org/docs/#installation))

### Virtual Environment

It's a good practice to use a virtual environment to isolate your project dependencies. Here's how to set up a virtual environment using Poetry:

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/carlos-da-costa/azx-backend-test.git
   ```

2. Navigate to the project directory:

   ```bash
   cd azx_test
   ```

3. Create a virtual environment:

   ```bash
   poetry env use python3
   ```

### Install Dependencies

To install the project's dependencies, run the following command inside your virtual environment:

```bash
poetry install
```

This will install all the required packages, including Flask, PyJWT, and pytest.

# Exercise 1 and 5

## Running Unit Tests

You can run the unit tests using pytest. Make sure you are in the virtual environment where you installed the project dependencies. Run the following commands:

```bash
cd exercise_1_and_5
poetry run pytest tests.py
```

# Exercise 2

Although the exercise statement has not specified anything about storage,
I decided to implement storage of tasks using Sqlite database.
Also as arbitrary decision for the matter of exercising, a mix of DAL (database abastraction layer) and a micro ORM (object relation model) was implemented.
Such implementation decisions were taken based on the fact that it is an exercise and not a real world product. If it was the case, using well stabilished libraries for all cases is generally a better idea.

## Running Flask App

If you want to run Flask app, navigate to the respective app directory (e.g., `exercise_2`) and run the app:

```bash
cd exercise_2
poetry run python app.py
```

This will start the Flask app, and you can access it in your browser or via HTTP requests.

### Bonus
A Postman collection is provided here so you can easily test the application.
Change the base_url current value variable on collection Variables to test locally.

[![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/17396514-e8b6feeb-73e8-4907-94f1-db27f5a188c1?action=collection%2Ffork&source=rip_markdown&collection-url=entityId%3D17396514-e8b6feeb-73e8-4907-94f1-db27f5a188c1%26entityType%3Dcollection%26workspaceId%3D0f5f08b2-1be3-420b-b949-39cdee04194d)

# Exercise 3 Solution

### SQL Query

[Click here to see the solution](exercise_3/query.md)


# Exercise 4

This one was implemented as a CLI (command line interface)

## Running the CLI
```bash
cd exercise_2
$ poetry run python token_manager.py 
Usage: token_manager.py [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  generate
  verify
```

## Running a token generation
```bash
$ poetry run python token_manager.py generate carlos
Generated Token: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiY2FybG9zIiwiZXhwIjoxNjk0MTM5MjQxfQ.pkTq8rxD_bvF4lWEiALg7XpwvpqY0lXg1cq7YA448rY
```

## Running a token verification
```bash
$ poetry run python token_manager.py verify eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoi
Y2FybG9zIiwiZXhwIjoxNjk0MTM5MjQxfQ.pkTq8rxD_bvF4lWEiALg7XpwvpqY0lXg1cq7YA448rY
Verified User ID: carlos
```

## Running Tests
```bash
poetry run pytest tests.py
```
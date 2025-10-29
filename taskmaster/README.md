# TaskMaster CLI Application

TaskMaster is a command-line interface (CLI) application designed for efficient task management. It allows users to add, list, complete, and delete tasks using a rich user interface. The application is built with Python 3.12 and utilizes the `uv` library for enhanced functionality.

## Features

- **Task Management**: Easily add, list, complete, and delete tasks.
- **Rich UI**: Enjoy a beautiful table interface for displaying tasks.
- **JSON Storage**: Tasks are stored in a JSON file located at `~/.taskmaster.json`.
- **Minimal Dependencies**: The project is designed to have minimal external dependencies, ensuring a lightweight application.

## Project Structure

```
taskmaster
├── src
│   └── taskmaster
│       └── main.py          # Entry point for the TaskMaster CLI application
├── tests
│   ├── test_main.py         # Unit tests for main functionality
│   └── test_cli.py          # Tests for command-line interface
├── pyproject.toml           # Project configuration and dependencies
├── README.md                # Documentation for the TaskMaster project
├── .gitignore               # Files and directories to ignore by Git
└── tox.ini                  # Configuration for Tox testing automation
```

## Installation

To get started with TaskMaster, clone the repository and install the required dependencies:

```bash
git clone <repository-url>
cd taskmaster
pip install -r requirements.txt
```

## Usage

To run the TaskMaster CLI application, execute the following command:

```bash
python src/taskmaster/main.py
```

You can use the following commands within the CLI:

- `add <task>`: Add a new task.
- `list`: List all tasks.
- `complete <task_id>`: Mark a task as complete.
- `delete <task_id>`: Delete a task.

## Contribution

Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
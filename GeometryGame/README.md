# How to run the Python code?

Here is an overview of methods to run your Python code when working with **packages** and **modules**:

---

### 1. **Running the Script Directly**
   - **How**: Execute the file directly using `python` command.
   - **Example**:
     ```bash
     python square.py
     ```
   - **Problem**: Relative imports fail because Python doesn't treat the script as part of a package.

   - **When to Use**:
     - For small standalone scripts without any relative imports.
     - **Not ideal** for package-based code.

---

### 2. **Running as a Module with `-m` Flag** (Recommended for Packages)
   - **How**: Run the script as part of a package using the `-m` flag.
   - **Command**:
     ```bash
     python -m geometry.square
     ```
   - **Why It Works**:
     - Treats the entire folder as a package.
     - Relative imports (`from .point`) are resolved properly.
   - **Requirements**:
     - Run the command from the **parent directory** of the package.
     - The package folder must contain an `__init__.py` file.

---

### 3. **Adding Parent Directory to `sys.path`**
   - **How**: Add the parent directory to Python's module search path (`sys.path`) dynamically.
   - **Code** (Inside `square.py`):
     ```python
     import sys
     import os
     sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
     from geometry.rectangle import Rectangle
     ```
   - **Why It Works**:
     - Explicitly tells Python to include the parent directory in the module search path.
   - **Pros**:
     - Allows you to run the script directly using `python square.py`.
   - **Cons**:
     - It's less clean and not considered the most Pythonic approach.

---

### 4. **Setting the PYTHONPATH Environment Variable**
   - **How**: Set the `PYTHONPATH` environment variable to include the parent directory.
   - **Command** (On Windows):
     ```bash
     set PYTHONPATH=D:\GITHUB\OOPythonic\GeometryGame
     python geometry\square.py
     ```
   - **Command** (On Linux/macOS):
     ```bash
     export PYTHONPATH=/path/to/GeometryGame
     python geometry/square.py
     ```
   - **Why It Works**:
     - Adds the project root to Python's search path globally for the session.
   - **When to Use**:
     - For larger projects where you need flexibility to run scripts directly.

---

### 5. **Using an IDE or Editor**
   - Most modern IDEs like **VS Code** or **PyCharm** allow you to configure the **working directory**.
   - **Steps in VS Code**:
     1. Open the project root folder (`GeometryGame`).
     2. Set `"cwd"` (current working directory) in `launch.json`:
        ```json
        {
            "name": "Python: Module",
            "type": "python",
            "request": "launch",
            "module": "geometry.square",
            "cwd": "${workspaceFolder}"
        }
        ```
     3. Run the module directly within the IDE.

---

### Summary of Methods

| **Method**                      | **Command**                            | **Pros**                                 | **Cons**                                      |
|---------------------------------|---------------------------------------|-----------------------------------------|---------------------------------------------|
| **Run Directly**                | `python square.py`                    | Simple for standalone scripts           | Fails with relative imports                 |
| **Run as Module**               | `python -m geometry.square`           | Pythonic, works well with packages      | Must run from the parent directory          |
| **Modify `sys.path`**           | Add parent dir in code                | Allows direct execution                 | Adds boilerplate, less clean                |
| **Set PYTHONPATH**              | Set environment variable              | Works globally for the session          | Requires manual configuration               |
| **Using IDE**                   | Configure project in IDE              | Clean and flexible for development      | IDE dependent                               |

---

### Recommendation:
For package-based code:
1. **Preferred**: Use `python -m` to run modules (Method 2).
2. If you need direct execution: Add the parent directory to `sys.path` dynamically (Method 3).
# 🧱 Project Template Setup Guide

This guide provides step-by-step instructions to set up your project using Git Bash on Windows.

---

## 🚀 Quick Start

1. **Fork the Repository**  
   Navigate to the [project-template repository](https://github.com/Mayukh-Haldar/project-template) and click on the **Fork** button to create your own copy.

2. **Set as Template Repository**  
   In your forked repository:

   - Go to **Settings**.
   - Scroll down to the **Template repository** section.
   - Check the box to mark it as a template.

3. **Generate a New Repository from Template**

   - Click on **Use this template**.
   - Provide a unique name for your new repository.
   - Click **Create repository from template**.

4. **Clone the Repository Locally**  
   Open Git Bash and run:

   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```

5. **Run the Setup Script**  
   Execute the initialization script:

   ```bash
   bash init_setup.sh
   ```

   This script will:

   - Create a virtual environment using `python -m venv env`.
   - Install the required dependencies from `requirements.txt`.

6. **Activate the Virtual Environment**  
   If the environment isn't activated automatically, activate it manually:

   ```bash
   source env/Scripts/activate
   ```

   _Note: In Git Bash on Windows, use `source env/Scripts/activate` to activate the virtual environment._

7. **Run the Project Structure Script**  
   Execute the script to set up your project structure:

   ```bash
   python projectstructure.py
   ```

   When prompted, provide a unique name for your project.

8. **Organize Your Project Code**

   - After the project structure is created, copy the existing code from the `src` folder (specifically exception.py and logger.py) into your newly created project folder.
   - Once copied, you can remove the default `src` folder to avoid redundancy.

9. **Install the Project as a Package**  
   Install your project locally to make it accessible as a package:

   ```bash
   python setup.py install
   ```

   This allows you to import your project modules from anywhere within your virtual environment.

---

## 📌 Notes

- Ensure you have Python 3.8 or higher installed on your system.
- It's recommended to use Visual Studio Code (VS Code) for development. When using VS Code:
  - Open the project folder.
  - If the virtual environment isn't detected automatically, you can select it manually:
    - Press `Ctrl + Shift + P` to open the command palette.
    - Type `Python: Select Interpreter` and choose the interpreter from the `env` folder.

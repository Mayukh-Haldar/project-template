echo [$(date)]: "START"

echo [$(date)]: "Creating virtual environment with python -m venv"
python -m venv env

if [ ! -d "env" ]; then
    echo [$(date)]: "ERROR: Virtual environment was not created."
    exit 1
fi

echo [$(date)]: "Activating virtual environment"
source ./env/Scripts/activate

echo [$(date)]: "Upgrading pip"
python -m pip install --upgrade pip

echo [$(date)]: "Installing requirements"
python -m pip install -r requirements.txt

echo [$(date)]: "END"

# Create a new directory for your game
mkdir simple-game

# Change into the directory
cd simple-game

# Initialize a Git repository
git init

# Create a README file
echo "# Simple Game" >> README.md

# Create a main game file (e.g., game.py)
touch game.py

# Add and commit the changes
git add .
git commit -m "Initial commit"

# Create a new repository on GitHub (replace 'your-username' with your GitHub username)
git remote add origin https://github.com/tiijaay1/simple-game.git
git branch -M main
git push -u origin main

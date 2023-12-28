
mkdir simple-game

cd simple-game 
git init

echo "# Simple Game" >> README.md

touch game.py

git add .
git commit -m "Initial commit"

git remote add origin https://github.com/tiijaay1/simple-game.git
git branch -M main
git push -u origin main

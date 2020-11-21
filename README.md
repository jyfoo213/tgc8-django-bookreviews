## Django Demo Project

### To run

1. At the terminal, install Django
```
pip3 install django`
```

### To get latest checkpoints

At the terminal (open a new terminal is best):

1. `git fetch upstream`

2. `git checkout checkpointX` (where X is the checkpoint numbeer)

3. When you want to push, type:

    `git push --set-upstream origin checkpointX` (where X is the checkpoint number)

  Afterwards you can push normally

4. Merge with master

  ```
  git checkout master
  git merge checkpointX
  ```
  


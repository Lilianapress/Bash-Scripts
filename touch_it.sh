#!/bin/bash
echo "Getting the list of to-b-deleted files in scratch"
cp /home/scratch_to_delete/$USER scratch_to_delete
file="/home/$USER/scratch_to_delete"
echo "*****************************************"
echo " Touching [with consent - lol] "
echo " It's going to take a few minutes, depending "
echo " on how big the number of files is "
echo " Thanks for your patience " 
echo "*****************************************"

while IFS= read -r line
do 
  touch $line
  #printf '%s\n' "$line"
done < "$file"
rm scratch_to_delete
echo "removed list of scratch_to_delete"
echo " BY ANA - June 2021 @Carleton Universiy "

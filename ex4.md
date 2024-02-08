 1. I would make it so if you are looking for a room <= 130 turn left. Which then you will be starting from room EY100. Then if it's greater turn right. You would be starting from EY138 and reverse searching. Then do a linear search of each room until you find the selected room.

 2. It would take 13 steps as each step is passing a room.

 3. This would be neither as there are worse cases.

 4. The best cases would EY100 or EY138 as either direction you take you will have run in to it on the first room. The worst case would be EY130 as you would turn left it would take 16 steps to run in to it and that would be the most of every other selected room. 

 5. I would make the middle point EY118 as it seems to be in the middle. So if looking for a room <= 118 turn left and then if it's room > 118 turn right. Then just do a linear search of the rooms until you find your selected room.As then the worst case would be 10 steps. 
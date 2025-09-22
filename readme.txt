This is a Python Script to allow for switching between various games on a PC98 Emulator by utilizing save states. This particular version was built for RTF25 (https://familyteam.neocities.org/rtf25). Please wait warmly, and enjoy!

Installation:
 1: It is wise to back up your NP setup before making modifications. Navigate to your NP folder. Open the Configuration Setting called "np21". Scroll until you find the line called "Function". It should largely be pairs of 00s. Replace the entire Function line with the following (copy your function line elsewhere if you want to revert to your old mappings later), and save:

Function=00 5d 3c 9e 00 60 3b 9d 00 61 3c 9d 00 62 3d 9d 00 63 3e 9d 00 64 3f 9d 00 65 09 9d 00 66 0a 9d 00 67 0b 9d 00 68 0c 9d 00 69 0d 9d 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00

This maps your NP save/load states to the number pad, where the load command for Slots 1, 2, 3, 4, and 5 are mapped to Num0, Num1, Num2, Num3, and Num4. The save command is mapped to Num5, Num6, Num7, Num8, and Num9. If you have any other commands mapped to these buttons (ending blockers, etc.), consider remapping them, as these buttons will be pressed frequently.

 2: In Github, navigate to the green "<> Code" button, click it, and click "Download ZIP". Place the zip near your NP folder (location does not actually matter), and extract.

 3: Open your np21, and open your desired game(s) to swap. This will use Mystic Square as an example. Open Mystic Square, and navigate to the shot selection screen (where you choose between Reimu, Marisa, Mima, and Yuuka). Press Num5, Num6, Num7, Num8, and Num9. You can test to ensure that the save state mappings are correct by pressing Num0-4.


Usage:

 1: In the PC98-Switcher folder, navigate to dist/PC98SaveStateSwapper.
 2: Run PC98SaveStateSwapper.
 3: Tab back into NP21, and when you are ready, press "B". A countdown will begin, and after you swap for the first time, begin!


Resetting runs:

Resetting a run is fairly simple. Unless you are playing five games at once, your fifth slot is your reset slot.    1: Close the python script.
 2: Tab into NP21. Press Num4, and then Num5, Num6, Num7, and Num8. You are now reset, and can refer to the Usage section.


Modifying settings:
 Coming soon.

Misc thoughts:
 - There were major issues with inputs getting stuck when swapping between games (simulated key would be stuck down until it was tapped). This was truly unplayable, and adding game pauses when switching fixed most of it. I do occasionally have focus getting stuck, but only rarely.
 - Since the game is pausing when switching, there is a risk where you could menu and quit game. The sound effect plays to warn you to be careful with your inputs, since I have not yet figured out a good way to fix this.
 - Also note that you will have to begin shooting again after switching games, as the pause stops you from firing.
 - The one time that Mystic Square cannot be paused is in the transition between stages. It is advised to wait on the end dialogue of a fight, and allow for a swap cycle to happen before progressing to the next stage. If you get stuck swapping on a load, you may need to manually unpause to proceed.
 - Very rarely, holding multiple keys when pausing will cause a delay in the pause menu appearing. If this happens, press all of your inputs once. The stuck key should eventually clear, and you can manually unpause to proceed.
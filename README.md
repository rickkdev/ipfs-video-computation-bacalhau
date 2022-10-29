# Description

This project processes videos on IPFS and converts them into pngs which are then resized into a suitable format for Ai to make further computations on the images.

Possible subsequent computations would be AIs that recognize and mark NSFW content that has already been uploaded to IPFS.

Although videos are made up of a number of frames, employing them all for video categorization would demand a great computational effort.In order to make this experiment more managable we are chosing a sampling of frames. We selected a frame sampling rate of frame rate of one second (1 fps) which should allow us to maintain a consistent effectiveness for comparison.

The computations for resizing and converting the video are made via Bacalhau which ensures simple and low costs CoD.

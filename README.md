For Minecraft 26.4

This resource pack makes every single block in the world render as a completely random block model. This does not just shuffle block models, so that Oak Logs look like Diamond Ore, and Cobblestone looks like Crafting Tables; EVERY single individual block in the world can be any other random block, so one Oak Log can look like a Furnace, while the Oak Log right on top of it looks like a Cactus.

Since this shuffles every single block model in the game's files, this means there are states of blocks that are normally impossible in vanilla Minecraft, such as he block model which JUST contains an individual book from a Chiseled Bookshelf, or he block model that JUST contains the connecting bars of a Fence.

### How does it work?
The entire resource pack gets generated with `random_block_models.py`, which uses several methods from my generalized Minecraft pack creation script [bldp](https://github.com/blockerlocker/bldp) in order to grab the list of block models, and generate the blockstate files. If you download this repo and run `random_block_models.py`, it should automatically generate the pack for the most recent snapshot of the game (unless you replace `latest-snapshot` on line 9 with a specific version).
import os, sys, urllib.request, json, random
from pathlib import Path


if len(sys.argv) > 1:
    MCVERSION = sys.argv[1]
else:
#### SET MINECRAFT VERSION MANUALLY HERE ####
    MCVERSION = "latest-snapshot"


os.chdir(os.path.dirname(os.path.abspath(__file__)))

if not Path.cwd().name == "assets":
    print(f"Working directory not named 'assets'! Instead got '{Path.cwd().name}'. This script must be stored within the 'assets' folder of your pack to generate correctly!")
    input("Press Enter to exit program...")
    sys.exit()

if not Path("bldp.py").is_file():
    with open("bldp.py", "w", encoding="utf-8") as bldp_main:
        bldp_main.write(urllib.request.urlopen("https://raw.githubusercontent.com/blockerlocker/bldp/main/data/bldp.py").read().decode('utf-8'))

import bldp

MCVERSION = bldp.get_version(MCVERSION)

TEMP_DIR = "temp_bldp"

bldp.remove_path(TEMP_DIR)
bldp.remove_path("minecraft")
bldp.remove_path("../pack.mcmeta")

bldp.unpack_client(MCVERSION,TEMP_DIR,("assets/minecraft/blockstates","assets/minecraft/models/block"))

print("--Generating pack, this may take a moment...")
blockstate_dir = f"{TEMP_DIR}/assets/minecraft/blockstates/"
models_dir = f"{TEMP_DIR}/assets/minecraft/models/block/"

blockstate_template = {
    "variants": {}
}

print("--Collecting list of block models")
all_models = []
for model in os.listdir(models_dir):
    model_name = str(model).replace(".json","")
    
    with open(f"{models_dir}/{model}", "r") as model_json:
        model_raw = json.load(model_json)

    has_texture = False

    if "textures" in model_raw and not "template" in model_name:
        for key in model_raw["textures"]:
            if key != "particle" and not "#" in model_raw["textures"][key]:
                has_texture = True

    if model_name in ["flower_pot_cross","flower_pot_cross_emissive","tinted_flower_pot_cross","redstone_dust_side","redstone_dust_side_alt"]:
        has_texture = False

    if has_texture == True:
        all_models.append({"model":f"block/{model_name}"})

print("--Randomizing order of block models for each block")
for block in os.listdir(blockstate_dir):
    model_list = all_models.copy()
    random.Random(str(block)).shuffle(model_list)
    bldp.json_to_file({"variants":{"":model_list}},"minecraft/blockstates",block)

resource_pack_format = bldp.get_version_data(MCVERSION)["resource_pack_version"]

pack = {
    "pack": {
        "description": "Makes every block render as a completely random block model.",
        "min_format": resource_pack_format,
        "max_format": resource_pack_format
    }
}

bldp.string_to_file(json.dumps(pack, indent=4),"../","pack.mcmeta")

bldp.remove_path(TEMP_DIR)
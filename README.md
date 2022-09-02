# Growtopia Info
Welcome to growtopia-info! This code can search any info in Growtopia, like sprite, description, server status and more!

## Download
If you want to try this code, you can download it by writing this on CMD or PowerShell
```powershell
PS> pip install Growtopia-Info==1.0.1
```

## Benefit
Once you install the package, you can use the package to search any items in Growtopia Fandom (ID/EN/ES)* and Server Status in Growtopia!

### Example Code
#### Server Status
If you want to know about server, you can use this code:
```python
import GTInformation
print(GTInformation.GameData())
```

The output will look like this:
```json
{'Online_User': '68056', 'WOTDLink': 'https://www.growtopiagame.com/worlds/(current_WOTD).png', 'WOTDName': '(current WOTD)', 'GTTime': '09:53:00', 'GTDate': '09/02/22'}
```

#### Item Sprite
The next code is Item Sprite, yes! You can use this package to search Item Sprite! Lets search Dirt:
```python
import GTInformation
print(GTInformation.ItemSprite("Dirt"))
```

And here's the output:
```json
{'Item': 'https://static.wikia.nocookie.net/growtopia/images/8/8f/ItemSprites.png/revision/latest/window-crop/width/32/x-offset/640/y-offset/1440/window-width/32/window-height/32?format=webp&fill=cb-20220902090823', 'Tree': 'https://static.wikia.nocookie.net/growtopia/images/e/e5/TreeSprites.png/revision/latest/window-crop/width/32/x-offset/640/y-offset/1440/window-width/32/window-height/32?format=webp&fill=cb-20220902090824', 'Seed': 'https://static.wikia.nocookie.net/growtopia/images/9/9c/SeedSprites.png/revision/latest/window-crop/width/16/x-offset/320/y-offset/720/window-width/16/window-height/16?format=webp&fill=cb-20220902090823'}
```

**Note! This link is not from Growtopia or Ubisoft, we use web scraping on growtopia.fandom.com to get this data! But don't worry, you don't need a Fandom.com account to use this package!

#### Item Data
What about Item Data? You can use ItemData to get the Item Data:
```python
import GTInformation
print(GTInformation.ItemData("Dirt"))
```

The output:
```json
{'Rarity': 1, 'Description': "Yep, it's dirt.", 'Properties': 'None', 'Type': 'Foreground Block - Foreground', 'Chi': 'Earth', 'Texture Type': '8 Directional', 'Collision Type': 'Full Collision', 'Hardness': '3 Hits 3 HitsRestores after 8s of inactivity.', 'Seed Color': '#603913 #A67C52', 'Grow Time': '31s', 'Default Gems Drop': '0 - 1'}
```

#### Item Recipe
Yeah yeah cool... but, can we get the item recipe? Yes you can! here:
```python
import GTInformation
print(GTInformation.ItemRecipe("Water Bucket"))
```

The output:
```json
{'Treasure Blast': '[ It can be found naturally generated in Treasure-blasted worlds.]', 'Undersea Blast': '[ It can be found naturally generated in Undersea-blasted worlds.]', 'Beach Blast': '[ It can be found naturally generated in Beach-blasted worlds.]', 'Summer Surprise': '[ Chance to be dropped from breaking a: • Summer Surprise • Treasure Chest naturally-generated in a beach-blasted world , May yield 1 item each time.]', 'Splicing': '[ The tree of this item can be made by mixing the following seeds:, Aqua Block Seed Toilet Seed , ]', 'Provider': '[ Drops in sets of 1-2 from harvesting a/an: Well ]', 'Special Event': '[ Found in the Beat The Heat! special event ., One has unlimited time to find\xa0? dropped Water Bucket.]'}
```

## Bugs
Yeah...... i hate bug, especially cockroaches! Here's the list of bugs I found in this package

#### Server Status
* Sometimes you will get 403 Forbidden error (i cant fix this, because this is Growtopia's fault)

#### Item Sprite
* Page with tabber, tabview still not working

#### Item Data
* Page with tabber, tabview still not working

#### Item Recipe
* Page with tabber, tabview still not working
* Duplicate template not working (ex: Pocong Clothes, Mine Laser Drill, and more)
* Require template not working (ex: Rift Cape, Pegasus Chest, and more)

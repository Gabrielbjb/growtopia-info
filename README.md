# Growtopia Info
![Banner](https://user-images.githubusercontent.com/111344809/189955249-85b71512-574e-47a3-8288-b0d4bc38d693.png)
Welcome to growtopia-info! This code can search any info in Growtopia, like sprite, description, server status and more!

## Download
If you want to try this code, you can download it by writing this on CMD or PowerShell
## Stable
```powershell
PS> pip install Growtopia-Info==2.0.2
```
## Development (not recommended!)
```powershell
PS> pip install Growtopia-Info
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
{
    "Online_User":"67767",
    "WOTDLink":"https://www.growtopiagame.com/worlds/oillao.png",
    "WOTDName":"OILLAO",
    "GTTime":"09:42:09",
    "GTDate":"09/13/22"
}
```

#### Item Sprite
The next code is Item Sprite, yes! You can use this package to search Item Sprite! Lets find Dirt:
```python
import GTInformation
print(GTInformation.ItemSprite("Dirt"))
```

And here's the output:
```json
{
    "Item":"https://static.wikia.nocookie.net/growtopia/images/8/8f/ItemSprites.png/revision/latest/window-crop/width/32/x-offset/32/y-offset/1152/window-width/32/window-height/32?format=webp&fill=cb-20220909151519",
    "Tree":"https://static.wikia.nocookie.net/growtopia/images/e/e5/TreeSprites.png/revision/latest/window-crop/width/32/x-offset/32/y-offset/1152/window-width/32/window-height/32?format=webp&fill=cb-20220909151522",
    "Seed":"https://static.wikia.nocookie.net/growtopia/images/9/9c/SeedSprites.png/revision/latest/window-crop/width/16/x-offset/16/y-offset/576/window-width/16/window-height/16?format=webp&fill=cb-20220909151520",
    "Title":"Dirt"
}
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
{
    "Description":"Yep, it's dirt.",
    "Properties":[
        "None"
    ],
    "Rarity":1,
    "Type":[
        "Foreground Block",
        "Foreground"
    ],
    "Chi":"Earth",
    "Texture Type":"8 Directional",
    "Collision Type":"Full Collision",
    "Hardness":{
        "Fist":"3",
        "Pickaxe":"3",
        "Restore":"8"
    },
    "Seed Color":[
        "#603913",
        "#A67C52"
    ],
    "Grow Time":"31s",
    "Default Gems Drop":"0 - 1",
    "Title":"Dirt"
}
```

#### Item Recipe
Yeah yeah cool... but, can we get the item recipe? Yes you can! here:
```python
import GTInformation
print(GTInformation.ItemRecipe("Water Bucket"))
```

The output:
```json
{
    "Treasure Blast":[
        [
            "It can be found naturally generated in Treasure-blasted worlds.",
            ""
        ]
    ],
    "Undersea Blast":[
        [
            "It can be found naturally generated in Undersea-blasted worlds.",
            ""
        ]
    ],
    "Beach Blast":[
        [
            "It can be found naturally generated in Beach-blasted worlds.",
            ""
        ]
    ],
    "Summer Surprise":[
        [
            "Chance to be dropped from breaking a: • Summer Surprise • Treasure Chest naturally-generated in a beach-blasted world",
            "May yield 1 item each time."
        ]
    ],
    "Splicing":[
        [
            "The tree of this item can be made by mixing the following seeds:",
            "Aqua Block Seed Toilet Seed",
            ""
        ]
    ],
    "Provider":[
        [
            "Drops in sets of 1-2 from harvesting a/an: Well"
        ]
    ],
    "Special Event":[
        [
            "Found in the Beat The Heat! special event .",
            "One has unlimited time to find? dropped Water Bucket."
        ]
    ],
    "Title":"Water Bucket"
}
```
## Features
* You can also change different languages (if the page exists), here's some example code:
```python
import GTInformation
print(GTInformation.ItemRecipe("Water Bucket", "id"))
```

The output:
```json
{
    "Pencampuran":[
        [
            "Pohonnya dapat dibuat dengan cara Pencampuran :",
            "Aqua Block Seed Toilet Seed",
            ""
        ]
    ],
    "Summer Surprise":[
        [
            "Kemungkinan didapat dengan cara menghanucrkan Summer Surprise atau dari Treasure Chest biasanya muncul secara alami di world pantai .",
            "Player mungkin akan mendapatkan 1 item"
        ]
    ],
    "Produksi":[
        [
            "1-2 Item ini diproduksi dari Well ."
        ]
    ],
    "Special Event":[
        [
            "Dapat ditemukan di Beat The Heat! special event .",
            "Player memiliki waktu tidak terbatas untuk menemukan? Water Bucket."
        ]
    ],
    "Muncul Secara Alami":[
        [
            "Item ini muncul secara alami di world yang menggunakan: • Undersea Blast • Beach Blast • Treasure Blast"
        ]
    ],
    "Tidak Tersedia Lagi":{
        "Peluang Saat Menghancurkan":[
            [
                "1 item ini didapat dengan cara menghancurkan • Fishing Supply Crate"
            ]
        ]
    },
    "Title":"Water Bucket"
}
```
Language code can be found in: https://community.fandom.com/wiki/Help:Language_code

## Bugs
Yeah...... i hate bug, especially cockroaches! Here's the list of bugs I found in this package

#### Server Status
* Sometimes you will get 403 Forbidden error (i cant fix this, because this is Growtopia's fault)

#### Item Sprite
* Page with tabber, tabview still not working (fixed! (only tabber!))

#### Item Data
* Page with tabber, tabview still not working (fixed! (only tabber!))

#### Item Recipe
* Page with tabber, tabview still not working (fixed! (only tabber!))
* Duplicate template not working (ex: Pocong Clothes, Mine Laser Drill, and more) (fixed!)
* Require template not working (ex: Rift Cape, Pegasus Chest, and more) (fixed!)

# Growtopia Item Info

This code can search any info in Growtopia, like sprite, description, server status and more!

## Example Usage

```python
from growtopiaitem import GrowtopiaItem

item = GrowtopiaItem("Dirt")
print(item.get_item_data())
print(item.get_item_sprite())
```

## Example response:
```json
{
    "Chi": "Earth",
    "CollisionType": "Full Collision",
    "DefaultGemsDrop": "0 - 1",
    "Description": "Yep, it's dirt.",
    "GrowTime": "31s",
    "Hardness": {
        "Fist": "3",
        "Pickaxe": "3",
        "Restore": "8"
    },
    "Properties": "None",
    "Rarity": 1,
    "SeedColor": ["#603913", "#A67C52"],
    "Sprite": {
        "Item": "https://static.wikia.nocookie.net/growtopia/images/8/8f/ItemSprites.png/revision/latest/window-crop/width/32/x-offset/3456/y-offset/160/window-width/32/window-height/32?format=png&fill=cb-20241001123445",
        "Seed": "https://static.wikia.nocookie.net/growtopia/images/9/9c/SeedSprites.png/revision/latest/window-crop/width/16/x-offset/1728/y-offset/80/window-width/16/window-height/16?format=png&fill=cb-20241001123445",
        "Tree": "https://static.wikia.nocookie.net/growtopia/images/e/e5/TreeSprites.png/revision/latest/window-crop/width/32/x-offset/3456/y-offset/160/window-width/32/window-height/32?format=png&fill=cb-20241001123445"
    },
    "TextureType": "8 Directional",
    "Title": "Dirt",
    "Type": ["Foreground Block", "Foreground"],
    "URL": "https://growtopia.fandom.com/wiki/Dirt"
}
```

## Installation

To install the required package, use pip:

```sh
pip install requirements.txt
```

## License

This project is licensed under the MIT License.

## Contributing

We welcome contributions! Please submit a pull request or open an issue to get started.

# Periodic-Table-CN
This Periodic Table Json is based on https://github.com/Bowserinator/Periodic-Table-JSON.


Temperatures such as boiling points and melting points are given in degrees kelvin.
Densities are given in g/L and molar heat in (mol*K)
Information that is missing is repersented as null. Some elements may have an image link to their spectral bands.
All elements have a three sentence summary from wikipedia. Currently the color tag is useless, so please use appearance instead.

Electron shells are given as an array, the first item is the number of electrons in the first shell, the 2nd item is the number of electrons in the second shell, etc...

A link to the source where the information was from is provided in each element under the key "source"

Now add some chinese values for the key whick has "_zh", so that we can see the json more conveniently.
New keys such as: "appearance_zh", "category_zh", "discovered_by_zh", "name_zh", "phase_zh", "summary_zh".

### 中英对照
name: 名字

symbol: 符号

number: 序号

period: 期数

category: 类别

atomic_mass: 原子质量

color: 颜色

appearance: 状态

phase: 形态

melt: 熔点

boil: 沸点

density: 密度

discovered_by: 发现者

molar_heat: 摩尔热量

source: 出处

named_by: 命名者

spectral_img: 光谱图

summary: 概要

xpos: 周期表横向位置

ypos: 周期表纵向位置

shells: 原子核外分布

#
Here's an example of how it's formatted:
```json
{
    "elements": [
        {
            "appearance": "colorless gas", 
            "appearance_zh": "无色气体", 
            "atomic_mass": 1.008, 
            "boil": 20.271, 
            "category": "diatomic nonmetal", 
            "category_zh": "双原子 非金属", 
            "color": null, 
            "density": 0.08988, 
            "discovered_by": "Henry Cavendish", 
            "discovered_by_zh": "亨利·卡文迪许", 
            "melt": 13.99, 
            "molar_heat": 28.836, 
            "name": "Hydrogen", 
            "name_zh": "氢", 
            "named_by": "Antoine Lavoisier", 
            "named_by_zh": "安托万·拉瓦锡", 
            "number": 1, 
            "period": 1, 
            "phase": "Gas", 
            "phase_zh": "气体", 
            "shells": [
                1
            ], 
            "source": "https://en.wikipedia.org/wiki/Hydrogen", 
            "spectral_img": "https://en.wikipedia.org/wiki/File:Hydrogen_Spectra.jpg", 
            "summary": "Hydrogen is a chemical element with chemical symbol H and atomic number 1. With an atomic weight of 1.00794 u, hydrogen is the lightest element on the periodic table. Its monatomic form (H) is the most abundant chemical substance in the Universe, constituting roughly 75% of all baryonic mass.", 
            "summary_zh": "氢是原子序数为1的化学元素，化学符号为H，在元素周期表中位于第一位。其原子质量为1.00794u，是最轻的元素，也是宇宙中含量最多的元素，大约占据宇宙质量的75%。", 
            "symbol": "H", 
            "xpos": 1, 
            "ypos": 1
        }
]}

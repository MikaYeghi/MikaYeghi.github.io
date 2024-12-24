---
layout: page
title: SatAdv
description: Disabling ground vehicle detectors in aerial and satellite imagery.
img: assets/img/projects/SatAdv/preview.png
importance: 1
category: work
related_publications: false
---

## Project Description

How can individuals protect their vehicles from being detected by satellites or drones? Since accessing and manipulating aerial system images is not feasible, alternative methods are needed. One approach is to use [adversarial stickers](https://arxiv.org/abs/2108.11765), but these are often ineffective against low-resolution systems typically employed in aerial surveillance. A more promising strategy involves modifying the vehicle itself to evade detection, even at lower resolutions. This project explores practical ways to achieve this goal.

## Method

We make vehicles harder to detect by aerial systems in three steps. First, we change their **texture** (coloring) with some practical constraints, such as limiting the color palette or limiting the area occupied by the adversarial coloring. Then, we make small changes to their **shape**. Finally, we **combine** these texture and shape changes to create the most effective attack. See the figure below for an overview.

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/projects/SatAdv/teaser.png" title="Pipeline overview" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    Pipeline overview illustrating the trade-off between attack performance and practical feasibility.
</div>

## Results

<!-- Our experiments revealed a trade-off between the performance and practicality of adversarial modifications. Our results suggest that it is most beneficial to combine texture modifications with very minor shape modifications. This allows to avoid making too large modifications to the original vehicle, but achieves almost 100% performance in fooling the vehicle detectors in aerial systems. See example adversarial vehicles below. -->
Our experiments demonstrated a clear trade-off between the performance and practicality of adversarial modifications. See example adversarial vehicles below.

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/projects/SatAdv/texture_attacks.png" title="Pipeline overview" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    Various texture attacks.
</div>

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/projects/SatAdv/shape_attacks.png" title="Pipeline overview" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    Shape and combined attacks.
</div>

The coding scheme used in our experiments is as follows:

- **A**: Adversarially optimized
- **R**: Randomly generated
- **U**: Unconstrained
- **Ma**: Masked, meaning the area of adversarial textures was restricted
- **Fc**: Fixed colors, where the color palette was limited to five pre-selected colors
- **Lc**: Limited colors, where the number of colors was fixed but optimized during adversarial optimization
- **Pix**: Pixelization applied to textures
- **seq**.: Sequential attack, where the adversarial texture was optimized first, followed by the shape
- **par**.: Parallel attack, where both texture and shape were optimized simultaneously

## Publication

<!-- [Download PDF](../../assets/pdf/CV.pdf) -->
You can access the PDF version of this work [here](../../publications).
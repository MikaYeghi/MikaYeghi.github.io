---
layout: page
title: AirTaxiSim
description: High-fidelity simulator for air taxis in cluttered urban environments.
img: assets/img/projects/AirTaxiSim/AirTaxiSim.png
importance: 2
category: work
related_publications: false
---

## Project Description

The goal of this project is to develop a simulator for air taxis in urban environments. Our team is building the simulator on top of [CARLA](https://carla.org/). An overview of the pipeline is shown in the figure below.

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/projects/AirTaxiSim/Pipeline_Overview.png" title="Pipeline overview" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    Overview of the pipeline.
</div>

The environment comprises various elements, including the ego vehicle, adversarial vehicles, ground vehicles, and buildings. The perception module is responsible for processing sensor data, while the planning component generates paths for the ego vehicle. The vehicle model simulates the ego vehicle's physics, capturing its dynamic behavior. Finally, the simulation control oversees the overall simulation process and collects data to evaluate safety and performance metrics.

## Example Figures

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/projects/AirTaxiSim/Landing_in_Traffic.png" title="Landing at an intersection" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    An air taxi landing in an urban environment. Its slow descent allows ground vehicles to stop and avoid collision, eventually leading to a traffic jam.
</div>

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/projects/AirTaxiSim/Air_Tax_on_Helipad.png" title="Air taxi resting on a helipad" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    An example simulation of an air taxi resting on a rooftop helipad.
</div>

## Publication

This work has been submitted as an abstract to the [AIAA Aviation Forum 2025](https://www.aiaa.org/aviation) and is under review. The code will be made public upon acceptance.
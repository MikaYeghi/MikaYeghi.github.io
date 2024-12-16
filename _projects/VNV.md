---
layout: page
title: VTOL Landing Verification
description: Verification and validation of a vision-based landing system for an autonomous VTOL vehicle.
img: assets/img/projects/VNV/Preview_Image.jpg
importance: 3
category: work
related_publications: false
---

## Project Description

This project aims to use the verification and validation (V&V) framework from [Verse](https://arxiv.org/abs/2301.08714) to ensure the safety of the landing procedure for the [MiniHawk](https://github.com/StephenCarlson/MiniHawk-VTOL) vertical take-off and landing (VTOL) vehicle in urban environments where other vehicles may be present.

## Method

We verify the safety of the landing system by calculating the reachable set of the MiniHawk during the landing action. This set is generated from 10 trajectories per scenario (described below) using the AirTaxiSim simulator. After computing the reachable set, we check for intersections with obstacles. If no overlap is found, the landing procedure is considered safe. If an overlap is detected, we cannot provide safety guarantees.

## Experiments

We design the following scenarios to verify the landing system:
- **Scenario 1.** The landing target is precisely known in advance, so no vision-based detection is required. The starting point is perturbed to simulate various approach directions, and no obstacles are present.
- **Scenario 2.** The exact landing target is unknown, and only an approximate target point is provided. This point is sampled from a normal distribution centered on the helipad located on the rooftop.
- **Scenario 3.** A larger aircraft intrudes into MiniHawk's landing path, requiring MiniHawk to navigate around the intruding vehicle.
- **Scenario 4.** Similar to *Scenario 2*, but in this case, no approximate target point is known. Instead, an onboard helipad detector is used to locate the landing point.
- **Scenario 5.** A combination of *Scenarios 3 and 4*, where no landing target is provided, and another vehicle is present in MiniHawk's landing path.

## Results

In all scenarios, MiniHawk's landing system successfully demonstrated its ability to navigate safely in potentially cluttered environments while avoiding obstacles. The reachability analysis validated this by generating reachable sets that did not overlap with any obstacles. The figures below show the resulting reachable sets along each dimension, as well as their 3D representation.

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/projects/VNV/Scenarios_3D.png" title="Scenarios" class="img-fluid rounded z-depth-1" %}
    </div>
</div>

## Conclusion

In conclusion, the MiniHawk is able to safely navigate urban environments, even with obstacles or other vehicles present. The reachability analysis confirms that the landing system can avoid obstacles in various scenarios. These results demonstrate the safety and reliability of the landing procedure, making the MiniHawk suitable for real-world autonomous VTOL applications.

## Publication

This work has been published in [AIAA SciTech Forum and Exposition 2025](https://www.aiaa.org/SciTech). See the paper in the [publications page](../../publications).
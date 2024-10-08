# -*- coding: utf-8 -*-

# (C) Copyright 2020, 2021, 2022, 2023 IBM. All Rights Reserved.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

"""Legacy location of the utils module. Please import from parameter.utils / enum in future."""

# pylint: disable=unused-import

from aihwkit.simulator.parameters import (
    IOParameters,
    UpdateParameters,
    WeightModifierParameter,
    WeightClipParameter,
    WeightRemapParameter,
    SimpleDriftParameter,
    DriftParameter,
    MappingParameter,
    InputRangeParameter,
    PrePostProcessingParameter,
)

from aihwkit.simulator.parameters.enums import (
    BoundManagementType,
    NoiseManagementType,
    WeightNoiseType,
    PulseType,
    WeightModifierType,
    WeightClipType,
    WeightRemapType,
    VectorUnitCellUpdatePolicy,
    AnalogMVType,
)

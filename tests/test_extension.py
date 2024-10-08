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

# pylint: disable=invalid-name, no-name-in-module, import-error

"""Tests for the AIHWKIT extension module ."""

from unittest import skipIf
from torch import Tensor
from aihwkit.extension import EXTENSION_COMPILED
from .helpers.testcases import AihwkitTestCase, SKIP_CUDA_TESTS

if EXTENSION_COMPILED:
    from aihwkit.extension.aihwkit_extension.ops import float_precision_cast


class FloatPrecisionCastTest(AihwkitTestCase):
    """Tests float precision cast."""

    @skipIf(not EXTENSION_COMPILED, "extension not compiled")
    def test_float_prec_cast(self) -> None:
        """Test float precision."""
        x = 1 + Tensor([1.0, 1.0 / 2.0, 1.0 / 4.0, 1.0 / 8.0, 1.0 / 16.0, 1.0 / 32.0, 1.0 / 64.0])

        y = float_precision_cast(x, 3, 4, False)
        y_ref = Tensor([2.0000, 1.5000, 1.2500, 1.1250, 1.0625, 1.0625, 1.0000])

        self.assertTensorAlmostEqual(y, y_ref)

    @skipIf(SKIP_CUDA_TESTS or not EXTENSION_COMPILED, "not compiled with CUDA support")
    def test_float_prec_cast_cuda(self) -> None:
        """Test float precision."""
        x = 1 + Tensor([1.0, 1.0 / 2.0, 1.0 / 4.0, 1.0 / 8.0, 1.0 / 16.0, 1.0 / 32.0, 1.0 / 64.0])

        y = float_precision_cast(x.cuda(), 3, 4, False)
        y_ref = Tensor([2.0000, 1.5000, 1.2500, 1.1250, 1.0625, 1.0625, 1.0000])

        self.assertTensorAlmostEqual(y.cpu(), y_ref)

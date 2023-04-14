# Copyright (c) 2023, NVIDIA CORPORATION & AFFILIATES. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import numpy as np
import pickle

try:
    import pymesh
except ImportError:
    Warning("pymesh is not installed. Please install it to use icosphere.")

# TODO apply a transformation to make faces parallel to ploes


def generate_and_save_icospheres(
    save_path: str = "icospheres.pickle",
) -> None:  # pragma: no cover
    """enerate icospheres from level 0 to 6 (inclusive) and save them to a pickle file.

    Parameters
    ----------
    path : str
        Path to save the pickle file.
    """
    radius = 1
    center = np.array((0, 0, 0))
    icospheres = {"vertices": [], "faces": []}

    # Generate icospheres from level 0 to 6 (inclusive)
    for order in range(6 + 1):
        icosphere = pymesh.generate_icosphere(radius, center, refinement_order=order)
        icospheres["order_" + str(order) + "_vertices"] = icosphere.vertices
        icospheres["order_" + str(order) + "_faces"] = icosphere.faces
        icosphere.add_attribute("face_centroid")
        icospheres[
            "order_" + str(order) + "_face_centroid"
        ] = icosphere.get_face_attribute("face_centroid")

    # save icosphere vertices and faces to a pickle file
    with open(save_path, "wb") as f:
        pickle.dump(icospheres, f, pickle.HIGHEST_PROTOCOL)